'''
CREDENTIALS & AI CONFIGURATION — Fill in your details here.
Copy this file to secrets.py and replace all placeholder values.

   cp config/secrets.example.py config/secrets.py

WARNING: Never commit secrets.py to GitHub. It is in .gitignore.
'''


# LinkedIn credentials
username = "your_linkedin_email@gmail.com"
password = "your_linkedin_password"


## AI Configuration ##

use_AI = True                           # True or False

# AI Provider — choose one: "openai", "deepseek", "gemini", "ollama"
ai_provider = "ollama"

# API URL
# Ollama (local):  "http://localhost:11434/v1/"
# OpenAI:          "https://api.openai.com/v1/"
# Gemini:          "https://generativelanguage.googleapis.com/v1beta/"
llm_api_url = "http://localhost:11434/v1/"

# API Key
# Ollama:  "not-needed"
# OpenAI:  "sk-..."
# Gemini:  Get free key at https://aistudio.google.com/app/apikey
llm_api_key = "not-needed"

# Model name
# Ollama:  "llama3.2:1b", "llama3.1:8b", "mistral:7b"
# OpenAI:  "gpt-4o-mini", "gpt-4o"
# Gemini:  "gemini-flash-lite-latest", "gemini-2.0-flash"
llm_model = "llama3.2:1b"

llm_spec = "openai-like"

# Stream AI output? (False = faster, True = shows output live)
stream_output = False
