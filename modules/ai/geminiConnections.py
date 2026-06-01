from google import genai
from google.genai import types
from config.secrets import llm_model, llm_api_key
from modules.helpers import print_lg, critical_error_log, convert_to_json
from modules.ai.prompts import *
from typing import Literal

# Module-level flag — avoids scope error when set inside functions
_show_ai_alerts = True


def gemini_create_client():
    """Creates and returns a Gemini client using the google.genai SDK."""
    try:
        print_lg("Configuring Gemini client...")
        if not llm_api_key or llm_api_key in ("not-needed", "YOUR_GEMINI_API_KEY_HERE"):
            raise ValueError("Gemini API key not set. Please set it in config/secrets.py.")

        client = genai.Client(api_key=llm_api_key)
        print_lg("---- SUCCESSFULLY CONFIGURED GEMINI CLIENT! ----")
        print_lg(f"Using Model: {llm_model}")
        print_lg("---------------------------------------------")
        return client

    except Exception as e:
        error_message = "Error configuring Gemini client. Check your API key and model name."
        critical_error_log(error_message, e)
        return None


def gemini_completion(client, prompt: str, is_json: bool = False):
    """Generates content using the Gemini model."""
    if not client:
        raise ValueError("Gemini client is not available!")
    try:
        response = client.models.generate_content(
            model=llm_model,
            contents=prompt,
            config=types.GenerateContentConfig(
                safety_settings=[
                    types.SafetySetting(category="HARM_CATEGORY_HARASSMENT",       threshold="BLOCK_NONE"),
                    types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH",       threshold="BLOCK_NONE"),
                    types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
                    types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
                ]
            )
        )
        result = response.text
        if is_json:
            if result.startswith("```json"):
                result = result[7:]
            if result.endswith("```"):
                result = result[:-3]
            return convert_to_json(result)
        return result
    except Exception as e:
        critical_error_log("Error in Gemini completion!", e)
        return ""


def gemini_extract_skills(client, job_description: str):
    """Extracts skills from a job description using Gemini."""
    try:
        print_lg("Extracting skills from job description using Gemini...")
        prompt = extract_skills_prompt.format(job_description) + \
                 "\n\nImportant: Respond with only the JSON object, no markdown."
        return gemini_completion(client, prompt, is_json=True)
    except Exception as e:
        critical_error_log("Error extracting skills with Gemini!", e)
        return {"error": str(e)}


def gemini_answer_question(
    client,
    question: str,
    options: list | None = None,
    question_type: Literal['text', 'textarea', 'single_select', 'multiple_select'] = 'text',
    job_description: str = None,
    about_company: str = None,
    user_information_all: str = None
) -> str:
    """Answers an application question using Gemini."""
    try:
        print_lg(f"Answering question using Gemini: {question[:80]}")
        user_info = user_information_all or ""
        prompt = ai_answer_prompt.format(user_info, question)

        if options and question_type in ['single_select', 'multiple_select']:
            options_str = "OPTIONS:\n" + "\n".join([f"- {o}" for o in options])
            prompt += f"\n\n{options_str}"
            if question_type == 'single_select':
                prompt += "\n\nSelect exactly ONE option."
            else:
                prompt += "\n\nYou may select MULTIPLE options if appropriate."

        if job_description:
            prompt += f"\n\nJOB DESCRIPTION:\n{job_description}"
        if about_company:
            prompt += f"\n\nABOUT COMPANY:\n{about_company}"

        return gemini_completion(client, prompt)
    except Exception as e:
        critical_error_log("Error answering question with Gemini!", e)
        return ""


def gemini_check_job_match(client, job_title: str, job_description: str, candidate_profile: str) -> int:
    """
    Rates how well the candidate's resume/skills match the job requirements.
    Returns integer 0-100. Returns 50 on error (neutral — don't skip).
    """
    import re
    try:
        from modules.ai.prompts import job_match_prompt
        prompt = job_match_prompt.format(
            candidate_profile=candidate_profile[:2000],
            job_title=job_title,
            job_description=job_description[:2500]
        )
        raw = gemini_completion(client, prompt)
        nums = re.findall(r'\d+', str(raw))
        score = min(100, max(0, int(nums[0]))) if nums else 50
        print_lg(f"Gemini job match score: {score}/100")
        return score
    except Exception as e:
        critical_error_log("Error in Gemini job match check!", e)
        return 50
