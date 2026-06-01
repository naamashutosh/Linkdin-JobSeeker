'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

Support me: https://github.com/sponsors/GodsScion

version:    26.01.20.5.08
'''


###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "all resumes/default/resume.pdf"

# What do you want to answer for questions that ask about years of experience you have?
years_of_experience = "1"          # 1 year — Teaching Assistant at IIT Jammu (Aug 2024–Present)

# Do you need visa sponsorship now or in future?
require_visa = "No"                # Applying to India-based roles; no sponsorship needed

# What is the link to your portfolio website / GitHub
website = "https://github.com/ashutoshverma"

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/ashutoshverma"

# What is the status of your citizenship?
# Valid options: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer",
# "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization",
# "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Non-citizen allowed to work for any employer"


## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# Expected CTC / desired salary (in INR for India roles)
# 10 LPA is a reasonable expectation for a fresh IIT M.Tech graduate
desired_salary = 1000000           # 10,00,000 INR = 10 LPA. Do NOT use quotes.
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs),
then it will add '.' before last 5 digits and answer. Examples:
* 2400000 will be answered as "24.00"
* 1000000 will be answered as "10.00"
And if asked in months, then it will divide by 12 and answer.
'''

# Current CTC — student/TA stipend (IIT Jammu TA stipend ~12,400/month)
current_ctc = 0                    # 0 as currently a full-time M.Tech student. Do NOT use quotes.
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs),
then it will add '.' before last 5 digits and answer.
'''

# What is your notice period in days?
notice_period = 0                  # 0 — student, available to join immediately after completion.
'''
Note: If question has 'month' or 'week' in it, it will divide by 30 or 7 respectively.
'''

# Your LinkedIn headline
linkedin_headline = "M.Tech @ IIT Jammu | Signal Processing & AI/ML | 2 Accepted Publications (IEEE EMBC 2026, NCC)"

# Your summary / about section
linkedin_summary = """
M.Tech student at IIT Jammu specializing in Signal Processing and Communication Engineering (CGPA: 8.16), with hands-on research in Audio ML, Deep Learning, and Embedded AI systems. Published two accepted papers at IEEE EMBC 2026 and NCC India on speech-based oral cancer detection using multi-modal attention networks. Experienced in PyTorch, TensorFlow, Python, MATLAB, Whisper, Vision Transformers, and ONNX Runtime. Passionate about building production-grade AI systems at the intersection of signal processing, deep learning, and embedded deployment. Teaching Assistant for Digital Signal Processing Lab at IIT Jammu since Aug 2024.
"""

'''
Note: If left empty as "", the tool will not answer the question.
'''

# Your cover letter
cover_letter = """
Dear Hiring Team,

I am Ashutosh Verma, an M.Tech student at IIT Jammu specializing in Signal Processing and Communication Engineering (CGPA: 8.16). My research focuses on Audio ML, Deep Learning, and Embedded AI, with two accepted publications at IEEE EMBC 2026 and NCC India on speech-based oral cancer detection.

I have strong hands-on experience with PyTorch, TensorFlow, Python, MATLAB, Whisper, Vision Transformers, and edge deployment via ONNX Runtime and PyTorch C++. My projects span clinical AI, 5G protocol simulation, RF signal classification, NLP pipelines, and bare-metal embedded systems on STM32 and TI C6748.

As Teaching Assistant for the DSP Lab at IIT Jammu, I have guided 40+ students in ML-integrated signal analysis and production-ready inference pipelines. I am eager to bring this research depth and engineering rigour to your team.

Thank you for considering my application.

Regards,
Ashutosh Verma
+91-8439447732 | 2024psp0004@iitjammu.ac.in
"""

##> ------ Dheeraj Deshwal : dheeraj9811 - Feature ------
# Full profile info passed to AI to auto-answer unknown application questions
user_information_all = """
Name: Ashutosh Verma
Email: 2024psp0004@iitjammu.ac.in
Phone: +91-8439447732
Location: Jammu, Jammu & Kashmir, India
LinkedIn: https://www.linkedin.com/in/ashutoshverma
GitHub: https://github.com/ashutoshverma

EDUCATION:
- M.Tech, Signal Processing and Communication Engineering (SPCOM), IIT Jammu — CGPA: 8.16 (2024–Present)
- B.Tech, Electronics and Communication Engineering, Galgotias College of Engineering & Technology — CGPA: 8.07 (2017–2021)

CURRENT ROLE:
- Teaching Assistant, Digital Signal Processing Lab, IIT Jammu (Aug 2024–Present)
  Guiding 40+ students in ML-integrated signal analysis, FFT, FIR/IIR design, PyTorch model development.

EXPERIENCE: ~1 year (Teaching Assistant). Fresher / Entry-Level candidate.

SKILLS:
- Languages: Python, MATLAB, C/C++, SQL
- ML & DL: PyTorch, TensorFlow, CNNs, Transformers, BERT, Whisper, Vision Transformers (ViT), Wav2Vec2, Scikit-Learn
- Signal Processing: STFT, MFCC, PSD, WST-1D/2D, FIR/IIR Design, FFT, Spectrograms
- Wireless & RF: Modulation Classification, RadioML, SDR, SNR Estimation, 5G NR PHY/MAC (3GPP)
- Embedded: Embedded C, STM32, FreeRTOS, TI TMDSLCDK6748, UART, ONNX Runtime, PyTorch C++
- Tools: Git, Linux, Jupyter, Docker, ONNX Runtime, MATLAB Simulink, CCS, ADS

PUBLICATIONS (Accepted):
1. "Exploiting Wavelet Scattering and Spectral Features in Tri-Modal Cross-Attention for Oral Cancer Detection" — IEEE EMBC 2026
2. "Speech-Driven Early Oral Cancer Screening Using Adaptive VMD and Multi-Modal Attention Network" — NCC India

CERTIFICATIONS:
- Machine Learning Specialization — Andrew Ng, Coursera
- Qualcomm 5G Introductory Level Certification — Qualcomm
- Crash Course on Python — Google, Coursera

KEY PROJECTS:
- Embedded Oral Cancer Detection on Raspberry Pi 4B (sub-200ms inference, ONNX Runtime)
- 5G NR L1/L2 Protocol Stack Simulator (PHY: LDPC, OFDM, HARQ; MAC: MCS, scheduling; 3GPP 38.xxx)
- RF Signal Classification on RadioML (92%+ accuracy, 11 modulation types, 220K I/Q samples)
- FreeRTOS Multi-Task Scheduler on STM32; Bare-Metal UART Bootloader with CRC32
- YOLOv8 Vehicle Detection (mAP@0.5 = 0.89, ONNX/TensorRT FP16 for Jetson, 60+ FPS)
- End-to-End NLP Pipeline with DistilBERT (93%+ accuracy, ONNX + FastAPI deployment)

AVAILABILITY: Immediate (student, 0 days notice period)
EXPECTED CTC: 10 LPA (INR)
NATIONALITY: Indian
WORK AUTHORIZATION: Authorized to work in India. Would require visa sponsorship for international roles.
HIGHEST DEGREE: M.Tech (Master of Technology) — in progress
UNDERGRADUATE DEGREE: B.Tech in Electronics and Communication Engineering
"""
##<

'''
Note: If left empty as "", the tool will not answer the question.
'''

# Name of your most recent employer
recent_employer = "IIT Jammu"      # Teaching Assistant role

# Confidence level for skill-based questions (1–10)
confidence_level = "7"             # Strong foundation, research publications, but fresher level
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = True         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive







############################################################################################################
'''
THANK YOU for using my tool 😊! Wishing you the best in your job hunt 🙌🏻!

Sharing is caring! If you found this tool helpful, please share it with your peers 🥺. Your support keeps this project alive.

Support my work on <PATREON_LINK>. Together, we can help more job seekers.

As an independent developer, I pour my heart and soul into creating tools like this, driven by the genuine desire to make a positive impact.

Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours 🙏🏻,
Sai Vignesh Golla
'''
############################################################################################################