'''
Ollama Connections — Local LLM Integration
==========================================
Ollama exposes an OpenAI-compatible REST API at http://localhost:11434/v1/
This module wraps it with the same interface as geminiConnections.py so
the rest of the bot calls work identically regardless of AI provider.

Advantages over cloud APIs:
  - Unlimited tokens / no rate limits
  - No API cost
  - Privacy — job descriptions stay on your machine
  - Works offline

Setup:
  1. Install Ollama: winget install Ollama.Ollama
  2. Pull a model:   ollama pull llama3.1:8b
  3. Set in secrets.py:
       ai_provider  = "ollama"
       llm_model    = "llama3.1:8b"
       llm_api_url  = "http://localhost:11434/v1/"
       llm_api_key  = "not-needed"
'''

import re
import json
import requests as _req
from typing import Literal
from modules.helpers import print_lg, critical_error_log
from modules.ai.prompts import *
from config.secrets import llm_model, llm_api_url, llm_api_key

OLLAMA_BASE = "http://localhost:11434"


# --------------------------------------------------------------------------- #
#  Client                                                                      #
# --------------------------------------------------------------------------- #

def ollama_create_client():
    '''
    Verifies Ollama is running and the configured model is available.
    Returns the model name string on success, None on failure.
    '''
    try:
        print_lg("Checking Ollama server...")
        resp = _req.get(f"{OLLAMA_BASE}/api/tags", timeout=5)
        if resp.status_code != 200:
            raise ConnectionError(f"Ollama server not responding (HTTP {resp.status_code}). Is Ollama running?")

        available = [m["name"] for m in resp.json().get("models", [])]
        print_lg(f"Ollama models available: {available}")

        # Exact match or prefix match (e.g. "llama3.1:8b" matches "llama3.1:8b")
        matched = next((m for m in available if m == llm_model or m.startswith(llm_model.split(":")[0])), None)
        if not matched:
            raise ValueError(
                f"Model '{llm_model}' not found in Ollama.\n"
                f"Available: {available}\n"
                f"Pull it with: ollama pull {llm_model}"
            )

        print_lg(f"---- OLLAMA READY — Model: {matched} ----")
        return matched   # return the exact model name found

    except _req.exceptions.ConnectionError:
        critical_error_log(
            "Cannot connect to Ollama. Make sure Ollama is running.\n"
            "Start it with: ollama serve", Exception("Connection refused")
        )
        return None
    except Exception as e:
        critical_error_log(f"Ollama setup error: {e}", e)
        return None


# --------------------------------------------------------------------------- #
#  Core completion                                                             #
# --------------------------------------------------------------------------- #

def ollama_completion(client_model: str, prompt: str, is_json: bool = False) -> str:
    '''
    Sends a prompt to Ollama's generate endpoint and returns the response text.
    client_model: the exact model name returned by ollama_create_client()
    '''
    if not client_model:
        raise ValueError("Ollama model not initialized.")

    try:
        payload = {
            "model": client_model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.1,
                "num_predict": 512,
            }
        }
        if is_json:
            payload["format"] = "json"

        resp = _req.post(
            f"{OLLAMA_BASE}/api/generate",
            json=payload,
            timeout=120
        )
        resp.raise_for_status()
        result = resp.json().get("response", "").strip()
        print_lg(f"Ollama response (first 200): {result[:200]}")
        return result

    except _req.exceptions.Timeout:
        critical_error_log("Ollama request timed out (120s). Try a smaller model.", Exception("Timeout"))
        return ""
    except Exception as e:
        critical_error_log(f"Ollama completion error: {e}", e)
        return ""


# --------------------------------------------------------------------------- #
#  Task-specific functions (same interface as geminiConnections.py)           #
# --------------------------------------------------------------------------- #

def ollama_extract_skills(client_model: str, job_description: str) -> dict:
    '''Extracts skills from a job description using local Ollama model.'''
    try:
        print_lg("Extracting skills using Ollama...")
        prompt = extract_skills_prompt.format(job_description) + \
                 "\n\nReturn ONLY valid JSON. No markdown, no explanation."
        raw = ollama_completion(client_model, prompt, is_json=True)
        if raw:
            try:
                return json.loads(raw)
            except json.JSONDecodeError:
                # Try extracting JSON from response
                match = re.search(r'\{.*\}', raw, re.DOTALL)
                if match:
                    return json.loads(match.group())
        return {"tech_stack": [], "technical_skills": [], "other_skills": [],
                "required_skills": [], "nice_to_have": []}
    except Exception as e:
        critical_error_log("Ollama skill extraction error!", e)
        return {"error": str(e)}


def ollama_answer_question(
    client_model: str,
    question: str,
    options: list | None = None,
    question_type: Literal['text', 'textarea', 'single_select', 'multiple_select'] = 'text',
    job_description: str = None,
    about_company: str = None,
    user_information_all: str = None
) -> str:
    '''Answers an application question using local Ollama model.'''
    try:
        print_lg(f"Answering question with Ollama: {question[:80]}")
        user_info = user_information_all or ""
        prompt = ai_answer_prompt.format(user_info, question)

        if options and question_type in ['single_select', 'multiple_select']:
            prompt += "\n\nOPTIONS:\n" + "\n".join(f"- {o}" for o in options)
            if question_type == 'single_select':
                prompt += "\n\nSelect exactly ONE option from the list above."
            else:
                prompt += "\n\nSelect one or more options if appropriate."

        if job_description:
            prompt += f"\n\nJOB DESCRIPTION:\n{job_description[:1000]}"

        return ollama_completion(client_model, prompt)
    except Exception as e:
        critical_error_log("Ollama Q&A error!", e)
        return ""


def ollama_check_job_match(
    client_model: str,
    job_title: str,
    job_description: str,
    candidate_profile: str
) -> int:
    '''
    Rates how well the candidate's resume matches the job (0–100).
    Returns 50 on error (neutral — don't skip on failure).
    '''
    try:
        from modules.ai.prompts import job_match_prompt
        prompt = job_match_prompt.format(
            candidate_profile=candidate_profile[:2000],
            job_title=job_title,
            job_description=job_description[:2000]
        )
        raw = ollama_completion(client_model, prompt)
        nums = re.findall(r'\b(\d{1,3})\b', raw)
        score = min(100, max(0, int(nums[0]))) if nums else 50
        print_lg(f"Ollama job match score: {score}/100")
        return score
    except Exception as e:
        critical_error_log("Ollama job match error!", e)
        return 50


def ollama_select_projects(
    client_model: str,
    job_title: str,
    job_description: str,
    projects_list: list,
    n: int = 4
) -> list:
    '''
    Selects the N best projects for a job using local Ollama model.
    Returns list of project name strings.
    '''
    try:
        from modules.ai.prompts import select_projects_prompt
        projects_summary = [
            {"name": p["name"], "description": p.get("description", ""),
             "domains": p.get("domains", []), "tech_stack": p.get("tech_stack", [])}
            for p in projects_list
        ]
        prompt = select_projects_prompt.format(
            n=n,
            job_title=job_title,
            job_description=job_description[:2500],
            projects_json=json.dumps(projects_summary, indent=2)
        )
        raw = ollama_completion(client_model, prompt)
        print_lg(f"Ollama project selection raw: {raw[:300]}")

        match = re.search(r'\[.*?\]', raw, re.DOTALL)
        if match:
            selected = json.loads(match.group())
            valid = {p["name"] for p in projects_list}
            selected = [name for name in selected if name in valid]
            if selected:
                print_lg(f"Ollama selected projects: {selected[:n]}")
                return selected[:n]

        print_lg("Ollama: could not parse project list — using fallback")
    except Exception as e:
        critical_error_log("Ollama project selection error!", e)

    return [p["name"] for p in projects_list[:n]]
