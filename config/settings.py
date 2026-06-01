'''


License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            


version:    26.01.20.5.08
'''


###################################################### CONFIGURE YOUR BOT HERE ######################################################

# >>>>>>>>>>> LinkedIn Settings <<<<<<<<<<<

# Keep the External Application tabs open?
close_tabs = False                  # True or False, Note: True or False are case-sensitive
'''
Note: RECOMMENDED TO LEAVE IT AS `True`, if you set it `False`, be sure to CLOSE ALL TABS BEFORE CLOSING THE BROWSER!!!
'''

# Follow easy applied companies
follow_companies = False            # True or False, Note: True or False are case-sensitive

## Upcoming features (In Development)
# # Send connection requests to HR's 
# connect_hr = True                  # True or False, Note: True or False are case-sensitive

# # What message do you want to send during connection request? (Max. 200 Characters)
# connect_request_message = ""       # Leave Empty to send connection request without personalized invitation (recommended to leave it empty, since you only get 10 per month without LinkedIn Premium*)

# Do you want the program to run continuously until you stop it? (Beta)
run_non_stop = False                # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
alternate_sortby = True             # True or False, Note: True or False are case-sensitive
cycle_date_posted = True            # True or False, Note: True or False are case-sensitive
stop_date_cycle_at_24hr = True      # True or False, Note: True or False are case-sensitive


# >>>>>>>>>>> RESUME GENERATOR (Experimental & In Development) <<<<<<<<<<<

# Give the path to the folder where all the generated resumes are to be stored
generated_resume_path = "all resumes/" # (In Development)


# >>>>>>>>>>> Custom Resume (AI Project Selector) <<<<<<<<<<<

# Enable AI-powered per-job resume customization.
# Requires use_AI = True in secrets.py and a valid LaTeX template below.
enable_custom_resume = True             # True or False

# Path to your base LaTeX resume template (.tex).
# The template MUST contain these two marker lines exactly as shown:
#     %%PROJECTS_START%%
#     %%PROJECTS_END%%
# Everything between them is replaced with the AI-selected projects.
latex_template_path = "all resumes/template/resume_template.tex"

# How many projects to include per resume (3 or 4 recommended).
num_projects_in_resume = 4             # Positive integer

# Path to the Excel log that records which resume was used for each application.
resume_log_path = "all excels/resume_log.xlsx"


# >>>>>>>>>>> Dynamic Salary <<<<<<<<<<<

# Maximum expected salary for senior / specialist / research roles.
# The bot picks a salary between desired_salary (in questions.py) and this value
# based on seniority keywords found in the job description.
max_desired_salary = 220000        # 2,20,000 INR upper ceiling

# >>>>>>>>>>> Skills-Match Filter <<<<<<<<<<<

# When True, uses Gemini AI to check if your resume skills cover the job requirements
# before applying. Apply if match score >= min_job_match_score (below).
# Prevents wasting applications on truly irrelevant roles (e.g., finance, law)
# while ensuring you apply to any role your skills actually fulfill.
enable_job_match_filter = True     # True or False

# Minimum relevance score (0-100) required to apply.
# 40 = apply if resume covers ~40% or more of requirements (recommended — generous)
# 60 = stricter match required
min_job_match_score = 40           # 0 to 100


# >>>>>>>>>>> Global Settings <<<<<<<<<<<

# Directory and name of the files where history of applied jobs is saved (Sentence after the last "/" will be considered as the file name).
file_name = "all excels/all_applied_applications_history.csv"
failed_file_name = "all excels/all_failed_applications_history.csv"
logs_folder_path = "logs/"

# Set the maximum amount of time allowed to wait between each click in secs
click_gap = 1                       # Enter max allowed secs to wait approximately. (Only Non Negative Integers Eg: 0,1,2,3,....)

# If you want to see Chrome running then set run_in_background as False (May reduce performance). 
run_in_background = False           # True or False, Note: True or False are case-sensitive ,   If True, this will make pause_at_failed_question, pause_before_submit and run_in_background as False

# If you want to disable extensions then set disable_extensions as True (Better for performance)
disable_extensions = False          # True or False, Note: True or False are case-sensitive

# Run in safe mode. Set this true if chrome is taking too long to open or if you have multiple profiles in browser. This will open chrome in guest profile!
safe_mode = False                   # False = uses your real Chrome profile (LinkedIn stays logged in)

# Do you want scrolling to be smooth or instantaneous? (Can reduce performance if True)
smooth_scroll = False               # True or False, Note: True or False are case-sensitive

# If enabled (True), the program would keep your screen active and prevent PC from sleeping. Instead you could disable this feature (set it to false) and adjust your PC sleep settings to Never Sleep or a preferred time. 
keep_screen_awake = True            # True or False, Note: True or False are case-sensitive (Note: Will temporarily deactivate when any application dialog boxes are present (Eg: Pause before submit, Help needed for a question..))

# Run in undetected mode to bypass anti-bot protections (Preview Feature, UNSTABLE. Recommended to leave it as False)
stealth_mode = True                # True or False, Note: True or False are case-sensitive

# Do you want to get alerts on errors related to AI API connection?
showAiErrorAlerts = True             # True or False, Note: True or False are case-sensitive

# Use ChatGPT for resume building (Experimental Feature can break the application. Recommended to leave it as False) 
# use_resume_generator = False       # True or False, Note: True or False are case-sensitive ,   This feature may only work with 'stealth_mode = True'. As ChatGPT website is hosted by CloudFlare which is protected by Anti-bot protections!


############################################################################################################
'''


Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

'''
############################################################################################################