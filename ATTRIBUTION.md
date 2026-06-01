# Attribution

This project is built on top of the open-source
[Auto Job Applier LinkedIn](https://github.com/GodsScion/Auto_job_applier_linkedIn)
by Sai Vignesh Golla, licensed under AGPL-3.0.

## Changes Made by Ashutosh Verma (IIT Jammu)

### New Files Added
| File | Description |
|---|---|
| `config/projects.py` | Master project list with 19 real projects, domain tags, tech stack, and LaTeX entries |
| `modules/resume_customizer.py` | AI-powered resume customization — selects best projects via Gemini, compiles LaTeX to PDF, enforces single page |
| `modules/resume_logger.py` | Excel logger — records which resume + projects used per job application |
| `modules/ai/geminiConnections.py` | Complete Gemini AI integration (new google.genai SDK) with job matching, project selection, Q&A |
| `all resumes/template/resume_template.tex` | LaTeX resume template with project injection markers |

### Modified Files
| File | Changes |
|---|---|
| `runAiBot.py` | AI resume generation pipeline, skills-match filter, dynamic salary, applicant count filter, experience filter |
| `modules/ai/prompts.py` | Added `select_projects_prompt`, `job_match_prompt` |
| `modules/ai/openaiConnections.py` | Added `ai_select_projects()` |
| `modules/helpers.py` | Fixed Chrome profile path for Windows |
| `modules/validator.py` | Validation for all new config settings |
| `config/search.py` | Smart experience filter, applicant filter, recency priority, relevant job titles |
| `config/settings.py` | New settings: custom resume, job match filter, dynamic salary |
| `config/questions.py` | Profile-specific answers for Ashutosh Verma |
| `README.md` | Completely rewritten |

## License
AGPL-3.0 — see LICENSE file.
