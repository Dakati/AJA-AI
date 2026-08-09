import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env
load_dotenv()

# Get OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# AI model
MODEL = "openai/gpt-oss-20b:free"

# OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)