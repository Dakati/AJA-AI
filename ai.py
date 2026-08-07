from openai import OpenAI
from config import API_KEY

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)


def ask_ai(messages):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=messages
    )

    return response.choices[0].message.content