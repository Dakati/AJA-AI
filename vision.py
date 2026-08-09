from PIL import Image
import pytesseract
import base64
from openai import OpenAI
from config import OPENROUTER_API_KEY

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def open_image(path):
    try:
        img = Image.open(path)

        print(f"\n📷 Image Loaded Successfully")
        print(f"📂 File : {path}")
        print(f"📐 Size : {img.size}")
        print(f"🎨 Mode : {img.mode}")

        img.show()

        return "Image opened successfully."

    except Exception as e:
        return f"Error: {e}"


def read_text(path):
    try:
        img = Image.open(path)

        text = pytesseract.image_to_string(img)

        if not text.strip():
            return "No text found."

        return text

    except Exception as e:
        return f"Error: {e}"


def describe_image(path):
    try:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY
        )

        with open(path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode("utf-8")

        response = client.chat.completions.create(
            model="openai/gpt-4.1-mini",
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Describe this image in detail."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_data}"
                            }
                        }
                    ]
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"