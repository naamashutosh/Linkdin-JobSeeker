'''
Resume Customizer Module
Selects best-matching projects via AI and generates a per-job LaTeX resume.

Flow:
  1. select_projects_with_ai()  -> asks AI to pick best N projects for the job
  2. generate_custom_resume()   -> injects projects into the LaTeX template and
                                   enforces STRICT SINGLE PAGE by recompiling
                                   with fewer projects if overflow is detected
  3. _compile_once()            -> compiles .tex → .pdf and returns page count
  4. The resulting 1-page PDF path is returned for upload in the apply flow.

Single-Page Enforcement:
  - After every compilation pdflatex prints:
        "Output written on file.pdf (N pages, X bytes)."
  - This module parses that line and, if N > 1, drops the last project and
    recompiles.  Minimum 2 projects are always kept.
  - The template also uses \\enlargethispage to give LaTeX extra squeeze room.

LaTeX Template Requirements:
  Your template must contain exactly these two marker lines:
      %%PROJECTS_START%%
      %%PROJECTS_END%%
  Everything between them is replaced with the selected project latex_entry blocks.
'''

import os
import re
import json
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    import requests as _req
    _REQUESTS_OK = True
except ImportError:
    _REQUESTS_OK = False

from modules.helpers import print_lg


# Minimum number of projects that will always appear on the resume
_MIN_PROJECTS = 2


# --------------------------------------------------------------------------- #
#  AI Project Selection                                                        #
# --------------------------------------------------------------------------- #

def select_projects_with_ai(
    job_title: str,
    job_description: str,
    projects_list: list,
    ai_client,
    ai_provider: str = "openai",
    n: int = 4
) -> list:
    '''
    Calls the configured AI provider to choose the N best projects from
    projects_list for this job.  Returns a list of project name strings.
    Falls back to the first N projects in the list if AI fails.
    '''
    if not projects_list:
        print_lg("CustomResume: projects_list is empty — skipping project selection.")
        return []

    from modules.ai.prompts import select_projects_prompt

    projects_summary = [
        {
            "name": p["name"],
            "description": p.get("description", ""),
            "domains": p.get("domains", []),
            "tech_stack": p.get("tech_stack", [])
        }
        for p in projects_list
    ]

    prompt = select_projects_prompt.format(
        n=n,
        job_title=job_title,
        job_description=job_description[:3000],
        projects_json=json.dumps(projects_summary, indent=2)
    )

    try:
        messages = [{"role": "user", "content": prompt}]

        if ai_provider.lower() == "openai":
            from modules.ai.openaiConnections import ai_completion
            raw = ai_completion(ai_client, messages, stream=False)
        elif ai_provider.lower() == "deepseek":
            from modules.ai.deepseekConnections import deepseek_completion
            raw = deepseek_completion(ai_client, messages)
        elif ai_provider.lower() == "gemini":
            from modules.ai.geminiConnections import gemini_completion
            raw = gemini_completion(ai_client, messages)
        else:
            from modules.ai.openaiConnections import ai_completion
            raw = ai_completion(ai_client, messages, stream=False)

        match = re.search(r'\[.*?\]', str(raw), re.DOTALL)
        if match:
            selected = json.loads(match.group())
            valid_names = {p["name"] for p in projects_list}
            selected = [name for name in selected if name in valid_names]
            if selected:
                print_lg(f"CustomResume: AI selected projects → {selected}")
                return selected[:n]

        print_lg(f"CustomResume: AI response could not be parsed: {str(raw)[:300]}")
    except Exception as e:
        print_lg(f"CustomResume: AI project selection error — {e}")

    fallback = [p["name"] for p in projects_list[:n]]
    print_lg(f"CustomResume: Using fallback projects → {fallback}")
    return fallback


# --------------------------------------------------------------------------- #
#  LaTeX Resume Generation  (single-page enforced)                            #
# --------------------------------------------------------------------------- #

def generate_custom_resume(
    template_path: str,
    projects_list: list,
    selected_project_names: list,
    company_name: str,
    job_title: str,
    output_base_dir: str = "all resumes"
) -> Optional[str]:
    '''
    Generates a one-page custom resume by:
      1. Injecting selected projects into the LaTeX template.
      2. Compiling to PDF and checking the page count.
      3. If the PDF is > 1 page, dropping the last project and recompiling.
      4. Repeating until the resume is exactly 1 page (min 2 projects kept).

    Returns the absolute path to the 1-page PDF, or None on failure.
    '''
    try:
        if not os.path.exists(template_path):
            print_lg(
                f"CustomResume: Template not found at '{template_path}'.\n"
                "  → Add %%PROJECTS_START%% and %%PROJECTS_END%% markers to your .tex file."
            )
            return None

        with open(template_path, 'r', encoding='utf-8') as fh:
            template_tex = fh.read()

        if "%%PROJECTS_START%%" not in template_tex or "%%PROJECTS_END%%" not in template_tex:
            print_lg(
                "CustomResume: Template missing %%PROJECTS_START%% / %%PROJECTS_END%% markers."
            )
            return None

        # Build ordered project list (AI-ranked order preserved)
        project_map = {p["name"]: p for p in projects_list}
        ordered = [project_map[n] for n in selected_project_names if n in project_map]

        if not ordered:
            print_lg("CustomResume: None of the selected project names matched projects_list.")
            return None

        # Output folder: all resumes/<Company>/
        safe_company = _safe_name(company_name)
        safe_title   = _safe_name(job_title)
        output_dir   = os.path.join(output_base_dir, safe_company)
        os.makedirs(output_dir, exist_ok=True)

        tex_name = f"{safe_company}_{safe_title}_resume.tex"
        tex_path = os.path.join(output_dir, tex_name)
        pdf_path = os.path.join(output_dir, Path(tex_name).stem + ".pdf")

        # ------------------------------------------------------------------ #
        # Single-page enforcement loop                                        #
        # Start with all selected projects; drop one from the end each time  #
        # a compilation produces more than 1 page.                           #
        # ------------------------------------------------------------------ #
        current = list(ordered)

        while len(current) >= _MIN_PROJECTS:
            modified_tex = _inject_projects(template_tex, current)
            _write_tex(tex_path, modified_tex)

            pages, success = _compile_once(tex_path, output_dir)

            if not success:
                print_lg("CustomResume: Compilation failed — trying with one fewer project.")
                current = current[:-1]
                continue

            if pages == 1:
                names_used = [p["name"] for p in current]
                print_lg(
                    f"CustomResume: 1-page PDF confirmed with {len(current)} project(s): "
                    f"{names_used}"
                )
                print_lg(f"CustomResume: PDF ready → {pdf_path}")
                return os.path.abspath(pdf_path)

            # Page overflow — drop the last (least relevant) project
            print_lg(
                f"CustomResume: PDF is {pages} page(s) with {len(current)} projects — "
                f"dropping '{current[-1]['name']}' and recompiling..."
            )
            current = current[:-1]

        # Minimum reached — compile whatever is left and return it even if
        # it's still slightly over (very unlikely with this template style)
        if current:
            modified_tex = _inject_projects(template_tex, current)
            _write_tex(tex_path, modified_tex)
            pages, success = _compile_once(tex_path, output_dir)
            if success:
                if pages > 1:
                    print_lg(
                        f"CustomResume: WARNING — resume is still {pages} page(s) "
                        f"with minimum {len(current)} project(s). "
                        "Consider tightening the template margins or shortening project descriptions."
                    )
                return os.path.abspath(pdf_path) if os.path.exists(pdf_path) else None

        print_lg("CustomResume: Could not produce a valid PDF.")
        return None

    except Exception as e:
        print_lg(f"CustomResume: Unexpected error — {e}")
        return None


# --------------------------------------------------------------------------- #
#  Internal helpers                                                            #
# --------------------------------------------------------------------------- #

def _inject_projects(template_tex: str, projects: list) -> str:
    '''Replaces the %%PROJECTS_START%% … %%PROJECTS_END%% block with project entries.'''
    block = "\n".join(p.get("latex_entry", "").strip() for p in projects)
    return re.sub(
        r'%%PROJECTS_START%%.*?%%PROJECTS_END%%',
        f'%%PROJECTS_START%%\n{block}\n%%PROJECTS_END%%',
        template_tex,
        flags=re.DOTALL
    )


def _write_tex(tex_path: str, content: str) -> None:
    with open(tex_path, 'w', encoding='utf-8') as fh:
        fh.write(content)


def _compile_once(tex_path: str, output_dir: str) -> tuple[int, bool]:
    '''
    Compiles tex_path to PDF once (two pdflatex passes for cross-references).
    Returns (page_count, success).
    page_count is -1 if it cannot be determined.
    Tries local pdflatex first, then latexonline.cc as fallback.
    '''
    pdf_path = os.path.join(output_dir, Path(tex_path).stem + ".pdf")

    # --- Local pdflatex ---
    if shutil.which("pdflatex"):
        try:
            # First pass
            r1 = subprocess.run(
                [
                    "pdflatex", "-interaction=nonstopmode",
                    f"-output-directory={os.path.abspath(output_dir)}",
                    os.path.abspath(tex_path)
                ],
                capture_output=True, text=True, timeout=90
            )
            # Second pass (resolves cross-references)
            r2 = subprocess.run(
                [
                    "pdflatex", "-interaction=nonstopmode",
                    f"-output-directory={os.path.abspath(output_dir)}",
                    os.path.abspath(tex_path)
                ],
                capture_output=True, text=True, timeout=90
            )

            if os.path.exists(pdf_path):
                pages = _parse_page_count(r2.stdout) or _parse_page_count(r1.stdout)
                print_lg(f"CustomResume: pdflatex OK — {pages} page(s).")
                return pages, True
            else:
                print_lg(f"CustomResume: pdflatex exit code {r1.returncode}.")
                _log_latex_errors(r1.stdout)
                return -1, False

        except FileNotFoundError:
            pass
        except Exception as e:
            print_lg(f"CustomResume: pdflatex error — {e}")
    else:
        print_lg(
            "CustomResume: pdflatex not found. Install MiKTeX: winget install MiKTeX.MiKTeX\n"
            "  → Trying online compilation..."
        )

    # --- latexonline.cc fallback ---
    if _REQUESTS_OK:
        try:
            with open(tex_path, 'r', encoding='utf-8') as fh:
                tex_content = fh.read()

            resp = _req.post(
                "https://latexonline.cc/compile",
                files={"file": (Path(tex_path).name, tex_content.encode('utf-8'), "text/plain")},
                timeout=90
            )
            content_type = resp.headers.get("content-type", "")
            if resp.status_code == 200 and "application/pdf" in content_type:
                with open(pdf_path, 'wb') as fh:
                    fh.write(resp.content)
                # Online API doesn't return page count in headers — check PDF size
                # as a rough single-page heuristic (< 120 KB is almost always 1 page)
                size_kb = os.path.getsize(pdf_path) / 1024
                pages = 1 if size_kb < 150 else 2
                print_lg(f"CustomResume: latexonline.cc OK — estimated {pages} page(s).")
                return pages, True
            else:
                print_lg(
                    f"CustomResume: Online compilation failed — "
                    f"HTTP {resp.status_code}, {resp.text[:200]}"
                )
        except Exception as e:
            print_lg(f"CustomResume: Online compilation error — {e}")
    else:
        print_lg("CustomResume: 'requests' not installed — no online fallback available.")

    return -1, False


def _parse_page_count(stdout: str) -> int:
    '''
    Parses the line pdflatex always prints at the end:
        "Output written on file.pdf (2 pages, 12345 bytes)."
    Returns the page count, or 1 if not found (safe default).
    '''
    match = re.search(r'Output written on .+?\((\d+) page', stdout)
    if match:
        return int(match.group(1))
    # Fallback: count occurrences of page-break markers
    if stdout:
        return max(1, stdout.count('[') // 2)
    return 1


def _log_latex_errors(stdout: str) -> None:
    for line in stdout.splitlines():
        if any(tag in line for tag in ["! ", "Error", "Warning", "Undefined", "Missing"]):
            print_lg(f"  LaTeX: {line}")


def _safe_name(text: str) -> str:
    return re.sub(r'[^\w\-]', '_', text.strip())[:60]
