import os
import time
import mss
from PIL import Image

from vision import read_text, describe_image


def capture_screen():

    try:
        os.makedirs("screenshots", exist_ok=True)

        filename = time.strftime(
            "screenshots/screen_%Y%m%d_%H%M%S.png"
        )

        with mss.mss() as sct:

            monitor = sct.monitors[1]

            screenshot = sct.grab(monitor)

            image = Image.frombytes(
                "RGB",
                screenshot.size,
                screenshot.rgb
            )

            image.save(filename)

        return filename

    except Exception as e:

        return f"Screen capture error: {e}"


def get_screen_size():

    try:

        with mss.mss() as sct:

            monitor = sct.monitors[1]

            width = monitor["width"]
            height = monitor["height"]

            return width, height

    except Exception as e:

        return f"Screen size error: {e}"


def analyze_screen():

    try:

        image_path = capture_screen()

        if image_path.startswith("Screen capture error"):
            return image_path

        text = read_text(image_path)

        return {
            "image": image_path,
            "text": text
        }

    except Exception as e:

        return f"Screen analysis error: {e}"