'''
Resume Customizer Module
Selects best-matching projects via AI and generates a per-job LaTeX resume.

Flow:
  1. select_projects_with_ai()  -> asks AI to pick best N projects for the job
  2. generate_custom_resume()   -> injects those projects into the LaTeX template
  3. compile_latex_to_pdf()     -> compiles .tex → .pdf (pdflatex or online API fallback)
  4. The resulting PDF path is returned for upload in the bot's apply flow.

LaTeX Template Requirements:
  Your template file must contain exactly these two marker lines:
      %%PROJECTS_START%%
      %%PROJECTS_END%%
  Everything between them is replaced with the selected projects' latex_entry blocks.
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

        # Extract JSON array from response
        match = re.search(r'\[.*?\]', str(raw), re.DOTALL)
        if match:
            selected = json.loads(match.group())
            # Validate that every returned name exists in our list
            valid_names = {p["name"] for p in projects_list}
            selected = [name for name in selected if name in valid_names]
            if selected:
                print_lg(f"CustomResume: AI selected projects → {selected}")
                return selected[:n]

        print_lg(f"CustomResume: AI response could not be parsed: {str(raw)[:300]}")
    except Exception as e:
        print_lg(f"CustomResume: AI project selection error — {e}")

    # Fallback: first N by list order
    fallback = [p["name"] for p in projects_list[:n]]
    print_lg(f"CustomResume: Using fallback projects → {fallback}")
    return fallback


# --------------------------------------------------------------------------- #
#  LaTeX Resume Generation                                                     #
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
    Replaces the %%PROJECTS_START%% … %%PROJECTS_END%% block in the LaTeX
    template with the selected projects, compiles to PDF, and saves the result
    in:  <output_base_dir>/<Company>/<Company>_<JobTitle>_resume.pdf

    Returns the absolute path to the PDF, or None on failure.
    '''
    try:
        # --- Read template ---
        if not os.path.exists(template_path):
            print_lg(
                f"CustomResume: Template not found at '{template_path}'.\n"
                "  → Place your LaTeX template at that path and add the markers:\n"
                "       %%PROJECTS_START%%\n"
                "       %%PROJECTS_END%%"
            )
            return None

        with open(template_path, 'r', encoding='utf-8') as fh:
            tex = fh.read()

        if "%%PROJECTS_START%%" not in tex or "%%PROJECTS_END%%" not in tex:
            print_lg(
                "CustomResume: Template is missing %%PROJECTS_START%% / %%PROJECTS_END%% markers.\n"
                "  → Add these two comment lines around your projects section in the .tex file."
            )
            return None

        # --- Build project LaTeX block (preserve AI-ranked order) ---
        project_map = {p["name"]: p for p in projects_list}
        ordered = [project_map[name] for name in selected_project_names if name in project_map]

        if not ordered:
            print_lg("CustomResume: None of the selected project names matched the projects_list.")
            return None

        projects_block = "\n".join(p.get("latex_entry", "").strip() for p in ordered)

        # --- Inject into template ---
        modified_tex = re.sub(
            r'%%PROJECTS_START%%.*?%%PROJECTS_END%%',
            f'%%PROJECTS_START%%\n{projects_block}\n%%PROJECTS_END%%',
            tex,
            flags=re.DOTALL
        )

        # --- Create output folder: all resumes/<CompanyName>/ ---
        safe_company = _safe_name(company_name)
        safe_title   = _safe_name(job_title)
        output_dir   = os.path.join(output_base_dir, safe_company)
        os.makedirs(output_dir, exist_ok=True)

        # --- Save .tex ---
        tex_name = f"{safe_company}_{safe_title}_resume.tex"
        tex_path = os.path.join(output_dir, tex_name)
        with open(tex_path, 'w', encoding='utf-8') as fh:
            fh.write(modified_tex)

        print_lg(f"CustomResume: Saved .tex → {tex_path}")

        # --- Compile to PDF ---
        pdf_path = _compile_latex(tex_path, output_dir)

        if pdf_path and os.path.exists(pdf_path):
            print_lg(f"CustomResume: PDF ready → {pdf_path}")
            return os.path.abspath(pdf_path)

        print_lg("CustomResume: PDF compilation failed — will use default resume.")
        return None

    except Exception as e:
        print_lg(f"CustomResume: Unexpected error in generate_custom_resume — {e}")
        return None


# --------------------------------------------------------------------------- #
#  LaTeX Compilation                                                           #
# --------------------------------------------------------------------------- #

def _compile_latex(tex_path: str, output_dir: str) -> Optional[str]:
    '''
    Tries to compile tex_path → PDF.
      1. pdflatex  (if installed)
      2. latexonline.cc online API  (fallback, requires internet)
    Returns PDF path on success, None on failure.
    '''
    pdf_path = os.path.join(output_dir, Path(tex_path).stem + ".pdf")

    # --- Attempt 1: local pdflatex ---
    if shutil.which("pdflatex"):
        try:
            result = subprocess.run(
                [
                    "pdflatex",
                    "-interaction=nonstopmode",
                    f"-output-directory={os.path.abspath(output_dir)}",
                    os.path.abspath(tex_path)
                ],
                capture_output=True,
                text=True,
                timeout=90
            )
            # Run twice so cross-references resolve
            if result.returncode == 0:
                subprocess.run(
                    [
                        "pdflatex",
                        "-interaction=nonstopmode",
                        f"-output-directory={os.path.abspath(output_dir)}",
                        os.path.abspath(tex_path)
                    ],
                    capture_output=True, text=True, timeout=90
                )
            if os.path.exists(pdf_path):
                print_lg("CustomResume: Compiled with local pdflatex.")
                return pdf_path
            else:
                print_lg(f"CustomResume: pdflatex returned code {result.returncode}.")
                _log_latex_errors(result.stdout)
        except FileNotFoundError:
            pass
        except Exception as e:
            print_lg(f"CustomResume: pdflatex error — {e}")
    else:
        print_lg(
            "CustomResume: pdflatex not found.\n"
            "  → To compile locally, install MiKTeX (Windows): https://miktex.org/download\n"
            "    Or run:  winget install MiKTeX.MiKTeX\n"
            "  → Trying online compilation..."
        )

    # --- Attempt 2: latexonline.cc API ---
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
                print_lg("CustomResume: Compiled via latexonline.cc.")
                return pdf_path
            else:
                print_lg(
                    f"CustomResume: Online compilation failed — "
                    f"HTTP {resp.status_code}, content-type: {content_type}\n"
                    f"Response: {resp.text[:300]}"
                )
        except Exception as e:
            print_lg(f"CustomResume: Online compilation error — {e}")
    else:
        print_lg("CustomResume: 'requests' not installed — cannot use online fallback.")

    return None


def _log_latex_errors(stdout: str) -> None:
    '''Prints lines from pdflatex stdout that contain errors or warnings.'''
    for line in stdout.splitlines():
        if any(tag in line for tag in ["! ", "Error", "Warning", "Undefined"]):
            print_lg(f"  LaTeX: {line}")


def _safe_name(text: str) -> str:
    '''Strips characters that are unsafe in folder/file names.'''
    return re.sub(r'[^\w\-]', '_', text.strip())[:60]
