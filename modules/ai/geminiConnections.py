from google import genai
from google.genai import types
from config.secrets import llm_model, llm_api_key
from config.settings import showAiErrorAlerts
from modules.helpers import print_lg, critical_error_log, convert_to_json
from modules.ai.prompts import *
from pyautogui import confirm
from typing import Literal


def gemini_create_client():
    """
    Creates and returns a Gemini client using the new google.genai SDK.
    """
    try:
        print_lg("Configuring Gemini client...")
        if not llm_api_key or llm_api_key in ("not-needed", "YOUR_GEMINI_API_KEY_HERE"):
            raise ValueError("Gemini API key is not set. Please set it in config/secrets.py.")

        client = genai.Client(api_key=llm_api_key)

        print_lg("---- SUCCESSFULLY CONFIGURED GEMINI CLIENT! ----")
        print_lg(f"Using Model: {llm_model}")
        print_lg("Check './config/secrets.py' for more details.")
        print_lg("---------------------------------------------")
        return client

    except Exception as e:
        error_message = "Error configuring Gemini client. Check your API key and model name."
        critical_error_log(error_message, e)
        if showAiErrorAlerts:
            if "Pause AI error alerts" == confirm(f"{error_message}\n{str(e)}", "Gemini Connection Error", ["Pause AI error alerts", "Okay Continue"]):
                showAiErrorAlerts = False
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
        return {"error": str(e)}


def gemini_extract_skills(client, job_description: str):
    """Extracts skills from a job description using Gemini."""
    try:
        print_lg("Extracting skills from job description using Gemini...")
        prompt = extract_skills_prompt.format(job_description) + "\n\nImportant: Respond with only the JSON object, no markdown."
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
        print_lg(f"Answering question using Gemini: {question}")
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
        return {"error": str(e)}
