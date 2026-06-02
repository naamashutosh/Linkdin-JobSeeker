'''
APPLICATION INPUTS — Fill in your personal details here.
Copy this file to questions.py and replace all placeholder values.

   cp config/questions.example.py config/questions.py
'''


###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Path to your default resume PDF (used as fallback if AI resume generation fails)
default_resume_path = "all resumes/default/resume.pdf"

# Years of experience to answer in application forms
years_of_experience = "1"          # e.g. "0", "1", "2", "3"

# Do you need visa sponsorship?
require_visa = "No"                # "Yes" or "No"

# Your GitHub / portfolio URL
website = "https://github.com/YOUR_GITHUB_USERNAME"

# Your LinkedIn profile URL
linkedIn = "https://www.linkedin.com/in/YOUR_LINKEDIN_ID/"

# US Citizenship status (for US job applications)
us_citizenship = "Non-citizen allowed to work for any employer"
# Options: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer",
#          "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization",
#          "Canadian Citizen/Permanent Resident", "Other"


## SALARY SETTINGS ##

# Expected CTC / desired salary (in your local currency, as a number)
desired_salary = 120000            # e.g. 120000 for India (1.2 LPA INR). Do NOT use quotes.

# Current CTC (0 if student / not currently employed)
current_ctc = 100000               # Do NOT use quotes.

# Notice period in days (0 = immediate joiner)
notice_period = 0                  # Do NOT use quotes.


## PROFILE TEXT ##

# Your LinkedIn headline
linkedin_headline = "M.Tech @ YOUR_UNIVERSITY | YOUR_SPECIALIZATION | Key Skills"

# Your LinkedIn summary / about section
linkedin_summary = """
Write 2-3 sentences about your background, research, skills, and goals.
"""

# Your cover letter (used when applications ask for one)
cover_letter = """
Dear Hiring Team,

Write your cover letter here. Mention your degree, key skills, and why
you are a good fit for the role.

Regards,
Your Name
Your Phone | Your Email
"""

# Full profile info — AI uses this to answer unknown application questions
user_information_all = """
Name: YOUR FULL NAME
Email: your.email@example.com
Phone: +91-XXXXXXXXXX
Location: Your City, State, India
LinkedIn: https://www.linkedin.com/in/YOUR_LINKEDIN_ID/
GitHub: https://github.com/YOUR_GITHUB_USERNAME

EDUCATION:
- M.Tech, Your Specialization, Your University — CGPA: X.XX (Year–Present)
- B.Tech, Your Branch, Your College — CGPA: X.XX (Year–Year)

CURRENT ROLE:
- Your Role at Your Organization (Start Date–Present)

EXPERIENCE: ~N years

SKILLS:
- Languages: Python, C/C++, MATLAB, ...
- ML & DL: PyTorch, TensorFlow, ...
- Signal Processing: FFT, MFCC, ...

PUBLICATIONS (if any):
1. Title — Conference/Journal, Year.

CERTIFICATIONS:
- Certification Name — Issuer

AVAILABILITY: Immediate (0 days notice)
EXPECTED CTC: X LPA (INR)
NATIONALITY: Indian
WORK AUTHORIZATION: Authorized to work in India.
HIGHEST DEGREE: M.Tech (in progress)
"""

# Most recent employer name
recent_employer = "YOUR_INSTITUTION_OR_COMPANY"

# Confidence level for skill-based 1-10 questions
confidence_level = "7"


## SETTINGS ##

# Pause before submitting each application (True = review before submit)
pause_before_submit = True         # True or False

# Pause if the bot can't answer a question (True = ask for help)
pause_at_failed_question = True    # True or False

# Overwrite previously saved answers?
overwrite_previous_answers = False # True or False
