'''
Resume Customizer Module
Selects best-matching projects via AI and generates a per-job LaTeX resume.

Flow:
  1. select_projects_with_ai()  -> AI picks best N projects for the job description
  2. generate_custom_resume()   -> injects projects into LaTeX template, enforces 1 page
  3. _compile_once()            -> compiles .tex → .pdf (pdflatex or online fallback)

Resume saved as:  all resumes/<CompanyName>/Resume_<CompanyName>.pdf

Single-Page Enforcement:
  Parses pdflatex "Output written on ... (N pages, ...)" after each compile.
  If N > 1 → drop last project → recompile (min 2 projects).

LaTeX Template Requirement:
  %%PROJECTS_START%%   ...   %%PROJECTS_END%%
  Everything between them is replaced with selected project latex_entry blocks.
'''

import os
import re
import json
import shutil
import subprocess
from pathlib import Path
from typing import Optional

try:
    import requests as _req
    _REQUESTS_OK = True
except ImportError:
    _REQUESTS_OK = False

from modules.helpers import print_lg


_MIN_PROJECTS = 4


# --------------------------------------------------------------------------- #
#  AI helper — works with OpenAI, Gemini, DeepSeek                           #
# --------------------------------------------------------------------------- #

def _call_ai(ai_client, ai_provider: str, prompt: str) -> str:
    '''Calls the correct AI backend with a plain string prompt. Returns raw text.'''
    provider = ai_provider.lower()
    if provider == "gemini":
        from modules.ai.geminiConnections import gemini_completion
        result = gemini_completion(ai_client, prompt)
        return str(result) if result else ""
    elif provider == "ollama":
        from modules.ai.ollamaConnections import ollama_completion
        result = ollama_completion(ai_client, prompt)
        return str(result) if result else ""
    elif provider == "deepseek":
        from modules.ai.deepseekConnections import deepseek_completion
        messages = [{"role": "user", "content": prompt}]
        result = deepseek_completion(ai_client, messages)
        return str(result) if result else ""
    else:  # openai / default
        from modules.ai.openaiConnections import ai_completion
        messages = [{"role": "user", "content": prompt}]
        result = ai_completion(ai_client, messages, stream=False)
        return str(result) if result else ""


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
    Uses AI to choose the N best projects from projects_list for this job.
    Returns a list of project name strings. Falls back to first N on failure.
    '''
    if not projects_list:
        print_lg("CustomResume: projects_list is empty.")
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
        raw = _call_ai(ai_client, ai_provider, prompt)
        print_lg(f"CustomResume: AI raw response (first 200 chars): {raw[:200]}")

        valid_names = {p["name"] for p in projects_list}

        # Extract the JSON array from the response (handles markdown/extra text)
        match = re.search(r'\[.*?\]', raw, re.DOTALL)
        if match:
            parsed = json.loads(match.group())

            # Handle both formats:
            #   Simple:  ["Project Name 1", "Project Name 2"]
            #   Verbose: [{"name": "Project Name 1", ...}, ...]
            if parsed and isinstance(parsed[0], dict):
                selected = [item.get("name", "") for item in parsed]
            else:
                selected = [str(item) for item in parsed]

            selected = [name for name in selected if name in valid_names]
            if selected:
                print_lg(f"CustomResume: AI selected → {selected}")
                return selected[:n]

        # Fallback: scan response for any valid project name mentioned
        found = [name for name in valid_names if name in raw]
        if found:
            print_lg(f"CustomResume: Extracted from text → {found[:n]}")
            return found[:n]

        print_lg("CustomResume: Could not parse AI project selection — using fallback.")
    except Exception as e:
        print_lg(f"CustomResume: AI project selection error — {e}")

    # Smart keyword-based fallback — scores each project against the job description
    print_lg("CustomResume: Using keyword-based scoring to select projects...")
    fallback = _keyword_select_projects(job_title, job_description, projects_list, n)
    print_lg(f"CustomResume: Keyword-selected projects → {fallback}")
    return fallback


# --------------------------------------------------------------------------- #
#  Resume Generation (single-page enforced)                                   #
# --------------------------------------------------------------------------- #

def generate_custom_resume(
    template_path: str,
    projects_list: list,
    selected_project_names: list,
    company_name: str,
    job_title: str,
    output_base_dir: str = "all resumes",
    job_description: str = "",
    conditional_certifications: list = None
) -> Optional[str]:
    '''
    Builds a custom resume PDF:
      1. Injects selected projects into the LaTeX template.
      2. Injects any conditional certifications whose domains match the job.
      3. Compiles and checks page count.
      4. Drops last project and recompiles if > 1 page (min _MIN_PROJECTS).

    PDF saved as: <output_base_dir>/<CompanyName>/Resume_<CompanyName>.pdf
    Returns absolute PDF path, or None on failure.
    '''
    try:
        if not os.path.exists(template_path):
            print_lg(f"CustomResume: Template not found at '{template_path}'.")
            return None

        with open(template_path, 'r', encoding='utf-8') as fh:
            template_tex = fh.read()

        if "%%PROJECTS_START%%" not in template_tex or "%%PROJECTS_END%%" not in template_tex:
            print_lg("CustomResume: Template missing %%PROJECTS_START%% / %%PROJECTS_END%% markers.")
            return None

        # --- Inject conditional certifications ---
        template_tex = _inject_conditional_certs(
            template_tex,
            conditional_certifications or [],
            job_title,
            job_description
        )

        project_map = {p["name"]: p for p in projects_list}
        ordered = [project_map[n] for n in selected_project_names if n in project_map]

        if not ordered:
            print_lg("CustomResume: None of the selected names matched projects_list.")
            return None

        # Folder: all resumes/<CompanyName>/
        safe_company = _safe_name(company_name)
        output_dir   = os.path.join(output_base_dir, safe_company)
        os.makedirs(output_dir, exist_ok=True)

        # File names:  Resume_<CompanyName>.tex / .pdf
        base_name = f"Resume_{safe_company}"
        tex_path  = os.path.join(output_dir, base_name + ".tex")
        pdf_path  = os.path.join(output_dir, base_name + ".pdf")

        # Single-page feedback loop
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
                    f"CustomResume: ✅ 1-page PDF with {len(current)} projects: {names_used}"
                )
                return os.path.abspath(pdf_path)

            print_lg(
                f"CustomResume: {pages} pages with {len(current)} projects — "
                f"dropping '{current[-1]['name']}' and recompiling..."
            )
            current = current[:-1]

        # Minimum reached — return whatever compiled
        if current:
            modified_tex = _inject_projects(template_tex, current)
            _write_tex(tex_path, modified_tex)
            pages, success = _compile_once(tex_path, output_dir)
            if success:
                if pages > 1:
                    print_lg(
                        f"CustomResume: ⚠️  Still {pages} pages with minimum {len(current)} projects."
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

def _keyword_select_projects(job_title: str, job_description: str, projects_list: list, n: int) -> list:
    '''
    Scores every project against the job title + description using keyword overlap.
    Returns names of the top N projects by score.
    Used as a reliable fallback when AI response cannot be parsed.
    '''
    job_text = (job_title + " " + job_description).lower()

    # Extract meaningful tokens (3+ chars, ignore common words)
    _stop = {'the','and','for','are','you','with','this','that','have','from','will',
             'our','your','not','but','can','all','any','its','been','has','was','was',
             'per','via','etc','also','into','more','each','some','such','both','they'}

    job_tokens = set(
        w for w in re.findall(r'[a-z]{3,}', job_text)
        if w not in _stop
    )

    scores = []
    for project in projects_list:
        score = 0
        # Score against domains (weight 3)
        for domain in project.get("domains", []):
            domain_tokens = set(re.findall(r'[a-z]{3,}', domain.lower()))
            score += len(job_tokens & domain_tokens) * 3

        # Score against tech stack (weight 2)
        for tech in project.get("tech_stack", []):
            tech_tokens = set(re.findall(r'[a-z]{3,}', tech.lower()))
            score += len(job_tokens & tech_tokens) * 2

        # Score against description (weight 1)
        desc_tokens = set(re.findall(r'[a-z]{3,}', project.get("description", "").lower()))
        score += len(job_tokens & desc_tokens)

        # Bonus: recent projects (date_range closer to today)
        date_range = project.get("date_range", "2020-01")
        try:
            year = int(date_range[:4])
            score += max(0, (year - 2020))  # +1 per year after 2020
        except Exception:
            pass

        scores.append((score, project["name"]))

    scores.sort(key=lambda x: -x[0])
    return [name for _, name in scores[:n]]


def _inject_conditional_certs(
    template_tex: str,
    conditional_certifications: list,
    job_title: str,
    job_description: str
) -> str:
    '''
    Checks each conditional certification against the job text.
    If ≥ min_keyword_matches domain keywords are found, appends the
    certification's latex_entry to the certifications section.

    Replaces %%CERTIFICATIONS_START%%...%%CERTIFICATIONS_END%% in the template.
    If no conditional certs qualify, the markers are simply removed.
    '''
    job_text = (job_title + " " + job_description).lower()
    matched_latex = []

    for cert in conditional_certifications:
        domains = [d.lower() for d in cert.get("domains", [])]
        threshold = cert.get("min_keyword_matches", 1)
        matches = sum(1 for d in domains if d in job_text)
        if matches >= threshold:
            matched_latex.append(cert.get("latex_entry", ""))
            print_lg(
                f"CertFilter: '{cert['name']}' MATCHED ({matches} keyword(s)) "
                f"— adding to certifications."
            )
        else:
            print_lg(
                f"CertFilter: '{cert['name']}' not relevant to this job — skipping."
            )

    extra = "".join(matched_latex)
    return re.sub(
        r'%%CERTIFICATIONS_START%%.*?%%CERTIFICATIONS_END%%',
        lambda _: f'%%CERTIFICATIONS_START%%{extra}%%CERTIFICATIONS_END%%',
        template_tex,
        flags=re.DOTALL
    )


def _inject_projects(template_tex: str, projects: list) -> str:
    block = "\n".join(p.get("latex_entry", "").strip() for p in projects)
    replacement = f'%%PROJECTS_START%%\n{block}\n%%PROJECTS_END%%'
    # Use a lambda so re.sub does NOT interpret backslashes in the LaTeX block
    # (e.g. \hfill, \textbf would be misread as regex escape sequences otherwise)
    return re.sub(
        r'%%PROJECTS_START%%.*?%%PROJECTS_END%%',
        lambda _: replacement,
        template_tex,
        flags=re.DOTALL
    )


def _write_tex(tex_path: str, content: str) -> None:
    with open(tex_path, 'w', encoding='utf-8') as fh:
        fh.write(content)


def _compile_once(tex_path: str, output_dir: str) -> tuple:
    '''Compiles tex_path → PDF. Returns (page_count, success).'''
    pdf_path = os.path.join(output_dir, Path(tex_path).stem + ".pdf")

    if shutil.which("pdflatex"):
        try:
            r1 = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode",
                 f"-output-directory={os.path.abspath(output_dir)}",
                 os.path.abspath(tex_path)],
                capture_output=True, text=True, timeout=90
            )
            r2 = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode",
                 f"-output-directory={os.path.abspath(output_dir)}",
                 os.path.abspath(tex_path)],
                capture_output=True, text=True, timeout=90
            )
            if os.path.exists(pdf_path):
                pages = _parse_page_count(r2.stdout) or _parse_page_count(r1.stdout)
                print_lg(f"CustomResume: pdflatex → {pages} page(s).")
                return pages, True
            else:
                print_lg(f"CustomResume: pdflatex failed (exit {r1.returncode}).")
                _log_latex_errors(r1.stdout)
                return -1, False
        except Exception as e:
            print_lg(f"CustomResume: pdflatex error — {e}")
    else:
        print_lg("CustomResume: pdflatex not found. Install MiKTeX: winget install MiKTeX.MiKTeX")

    if _REQUESTS_OK:
        try:
            with open(tex_path, 'r', encoding='utf-8') as fh:
                tex_content = fh.read()
            resp = _req.post(
                "https://latexonline.cc/compile",
                files={"file": (Path(tex_path).name, tex_content.encode('utf-8'), "text/plain")},
                timeout=90
            )
            if resp.status_code == 200 and "application/pdf" in resp.headers.get("content-type", ""):
                with open(pdf_path, 'wb') as fh:
                    fh.write(resp.content)
                size_kb = os.path.getsize(pdf_path) / 1024
                pages = 1 if size_kb < 150 else 2
                print_lg(f"CustomResume: latexonline.cc → ~{pages} page(s).")
                return pages, True
            print_lg(f"CustomResume: Online compile failed — HTTP {resp.status_code}")
        except Exception as e:
            print_lg(f"CustomResume: Online compile error — {e}")

    return -1, False


def _parse_page_count(stdout: str) -> int:
    # pdflatex wraps long paths across lines — join first, then search
    # Pattern: "(2 pages, 12345 bytes)" or "(1 page, 12345 bytes)"
    joined = stdout.replace('\n', ' ').replace('\r', ' ')
    match = re.search(r'\((\d+) page', joined)
    if match:
        return int(match.group(1))
    return 1


def _log_latex_errors(stdout: str) -> None:
    for line in stdout.splitlines():
        if any(t in line for t in ["! ", "Error", "Undefined", "Missing"]):
            print_lg(f"  LaTeX: {line}")


def _safe_name(text: str) -> str:
    return re.sub(r'[^\w\-]', '_', text.strip())[:60]
