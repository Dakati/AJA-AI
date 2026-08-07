import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

MODEL = "openai/gpt-oss-20b:free"