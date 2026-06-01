# LinkedIn AI Auto Job Applier
### Built by Ashutosh Verma — IIT Jammu

An intelligent automation bot that applies to LinkedIn jobs with **AI-customized resumes** tailored per job description. Built on top of an open-source base with extensive modifications for AI-driven resume generation, smart filtering, and automated application tracking.

---

## Features

### Core Automation
- Searches LinkedIn for jobs matching your titles and location
- Auto-fills Easy Apply forms (text fields, dropdowns, checkboxes, radio buttons)
- Logs all applications to CSV with job details, company, HR info, date applied
- Tracks failed applications separately for review

### AI Resume Customization (per job)
- Reads the job description using **Gemini AI**
- Selects the **best 3–4 projects** from your master project list that match the job
- Injects those projects into your **LaTeX resume template**
- Compiles a **single-page PDF** named `Resume_<CompanyName>.pdf`
- Saves each resume in `all resumes/<CompanyName>/`
- Logs which resume + projects were used in `all excels/resume_log.xlsx`

### Smart Filters (before applying)
| Filter | Logic |
|---|---|
| **Skills-Match Filter** | Gemini scores resume vs job requirements (0–100). Skip if < 40. Apply even if LinkedIn profile says "missing qualifications" — match is based on actual skills/projects |
| **Experience Filter** | Auto-applies to 0–1 yr / fresher / entry-level roles. Skips 2+ yr roles. MTech degree counts if master's is mentioned |
| **Applicant Count Filter** | Flags < 50 applicants as HIGH PRIORITY. Skips ≥ 200 applicants |
| **Recency Filter** | Prioritizes jobs posted in last 24 hours |
| **Bad Words Filter** | Skips jobs with irrelevant keywords (SAP, PHP, 10+ years, etc.) |

### Dynamic Salary
Automatically answers salary questions based on job seniority:
- Fresher / entry-level → ₹1,20,000
- Standard roles → ₹1,52,000
- Senior / research / 5G specialist → ₹2,20,000

### Single-Page Resume Enforcement
Compiles with N projects → checks pdflatex page count → drops last project if > 1 page → recompiles until exactly 1 page (minimum 2 projects).

---

## Project Structure

```
├── runAiBot.py                    # Main bot — entry point
├── app.py                         # Flask dashboard (localhost:5000)
├── config/
│   ├── personals.py               # Your name, phone, address
│   ├── questions.py               # Application answers, salary, cover letter
│   ├── search.py                  # Job titles, location, filters
│   ├── secrets.py                 # LinkedIn credentials + Gemini API key
│   ├── settings.py                # Bot behavior settings
│   └── projects.py                # Your 19 projects with LaTeX entries
├── modules/
│   ├── resume_customizer.py       # AI project selection + LaTeX compilation
│   ├── resume_logger.py           # Excel log of resumes used per job
│   ├── ai/
│   │   ├── geminiConnections.py   # Gemini AI (project selection, job match, Q&A)
│   │   ├── openaiConnections.py   # OpenAI / local LLM support
│   │   └── prompts.py             # All AI prompts
│   ├── clickers_and_finders.py    # Selenium element interaction
│   ├── helpers.py                 # Utility functions
│   ├── open_chrome.py             # Chrome session setup
│   └── validator.py               # Config validation at startup
├── all resumes/
│   ├── template/
│   │   └── resume_template.tex    # Your LaTeX resume template
│   └── <CompanyName>/
│       └── Resume_<CompanyName>.pdf  # Generated per job
└── all excels/
    ├── all_applied_applications_history.csv
    ├── all_failed_applications_history.csv
    └── resume_log.xlsx            # Which resume + projects used per job
```

---

## Setup

### 1. Install Requirements

```bash
# Python 3.10+
pip install undetected-chromedriver pyautogui setuptools openai flask-cors flask openpyxl requests google-genai

# LaTeX (for PDF compilation)
winget install MiKTeX.MiKTeX     # Windows
```

### 2. Configure Your Details

**`config/personals.py`** — name, phone, address

**`config/secrets.py`**
```python
username  = "your_linkedin_email@gmail.com"
password  = "your_linkedin_password"
use_AI    = True
ai_provider = "gemini"
llm_api_key = "YOUR_GEMINI_API_KEY"   # Get free key: https://aistudio.google.com/app/apikey
llm_model   = "gemini-flash-lite-latest"
```

**`config/questions.py`** — years of experience, salary, cover letter, LinkedIn/GitHub URLs

**`config/search.py`** — job titles to search, location, experience level, filters

### 3. Add Your Projects

Open `config/projects.py` and add your projects. Each entry:
```python
{
    "name": "Your Project Title",
    "description": "2-3 sentence plain-English description for AI matching",
    "domains": ["Machine Learning", "Signal Processing"],
    "tech_stack": ["Python", "PyTorch", "MATLAB"],
    "date_range": "2025-01",
    "latex_entry": r"""\resumeSubItem{Your Project Title (Tags) \hfill {\normalsize Date}}{
    Description paragraph for resume.
    }"""
}
```

### 4. Set Up Your Resume Template

Place your LaTeX resume at `all resumes/template/resume_template.tex`.

**Required markers** in your projects section:
```latex
%%PROJECTS_START%%
... default projects here ...
%%PROJECTS_END%%
```

The bot replaces everything between these markers for each job.

### 5. Place Your Default Resume

Copy your resume PDF to:
```
all resumes/default/resume.pdf
```
Used as fallback if AI resume generation fails.

### 6. Run

```bash
python runAiBot.py
```

Chrome opens automatically. Since `safe_mode = False`, it uses your real Chrome profile — **no manual login needed** if you're already signed into LinkedIn in Chrome.

**View application history:**
```bash
python app.py
# Open http://localhost:5000
```

---

## Configuration Reference

### `config/settings.py`

| Setting | Default | Description |
|---|---|---|
| `enable_custom_resume` | `True` | Generate AI-customized resume per job |
| `latex_template_path` | `all resumes/template/resume_template.tex` | Path to LaTeX template |
| `num_projects_in_resume` | `4` | Projects to select per resume |
| `enable_job_match_filter` | `True` | Skip jobs where skills score < threshold |
| `min_job_match_score` | `40` | Minimum Gemini match score to apply |
| `max_desired_salary` | `220000` | Upper salary for senior roles |
| `safe_mode` | `False` | False = use real Chrome profile (stay logged in) |
| `stealth_mode` | `True` | Bypass LinkedIn bot detection |
| `pause_before_submit` | `True` | Pause for review before each submit |
| `run_in_background` | `False` | Hide Chrome window |

### `config/search.py`

| Setting | Default | Description |
|---|---|---|
| `search_terms` | 18 ML/RF/DSP/Embedded titles | Job titles to search |
| `search_location` | `"India"` | Search location |
| `experience_level` | `["Internship", "Entry level", "Associate"]` | LinkedIn filter |
| `smart_experience_filter` | `True` | Skip 2+ yr jobs, always apply to freshers |
| `max_experience_to_apply` | `1` | Max years experience to apply |
| `prefer_recent_24h_jobs` | `True` | Sort by most recent, past 24h |
| `skip_if_applicants_exceed` | `200` | Skip if ≥ 200 applicants |
| `priority_if_applicants_below` | `50` | Flag as HIGH PRIORITY if < 50 applicants |

### `config/questions.py`

| Setting | Value | Description |
|---|---|---|
| `years_of_experience` | `"1"` | For experience questions in forms |
| `current_ctc` | `100000` | Current salary (TA stipend) |
| `desired_salary` | `120000` | Minimum expected salary |
| `notice_period` | `0` | Immediate availability |
| `require_visa` | `"No"` | For India roles |

---

## How Resume Customization Works

```
Job found on LinkedIn
        │
        ▼
Gemini scores skills match (0-100)
        │
   Score < 40 → Skip (irrelevant role)
   Score ≥ 40 → Continue
        │
        ▼
Gemini reads job description
Selects best 3–4 projects from your 19
        │
        ▼
Injects projects into resume_template.tex
Compiles → checks page count
If > 1 page → drops last project → recompile
        │
        ▼
Saves: all resumes/<Company>/Resume_<Company>.pdf
Logs:  all excels/resume_log.xlsx
        │
        ▼
Uploads Resume_<Company>.pdf to Easy Apply
```

---

## Adding Your Own Projects

1. Open `config/projects.py`
2. Copy the template entry at the bottom
3. Fill in all fields including the `latex_entry`
4. The `latex_entry` must use `\resumeSubItem{Title \hfill Date}{Description}` format
5. Set `date_range` as `"YYYY-MM"` (start date)

---

## Application Tracking

After each run:
- **`all excels/all_applied_applications_history.csv`** — every job applied with full details
- **`all excels/resume_log.xlsx`** — which `Resume_<Company>.pdf` was used + which projects
- **`all excels/all_failed_applications_history.csv`** — skipped/failed jobs with reasons
- **`logs/`** — full console logs per run

When you get an interview call, open `resume_log.xlsx`, find the company, and open the exact resume you submitted.

---

## License

This project builds on open-source code licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

New features added by Ashutosh Verma (IIT Jammu):
- AI Custom Resume Generator (`modules/resume_customizer.py`, `modules/resume_logger.py`)
- Gemini AI integration (`modules/ai/geminiConnections.py`)
- Smart Experience Filter, Applicant Count Filter, Skills-Match Filter
- Dynamic Salary system
- LaTeX single-page enforcement
- Complete `config/projects.py` project management system

Original base: [Auto Job Applier LinkedIn](https://github.com/GodsScion/Auto_job_applier_linkedIn) — AGPL-3.0

---

*Built with ❤️ by Ashutosh Verma | M.Tech, IIT Jammu | Signal Processing & AI/ML*
