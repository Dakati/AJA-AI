import time
import pyautogui


# ============================================================
# MOUSE POSITION
# ============================================================

def get_mouse_position():
    try:
        x, y = pyautogui.position()
        return f"Mouse position: ({x}, {y})"
    except Exception as e:
        return f"Mouse error: {e}"


# ============================================================
# MOVE MOUSE
# ============================================================

def move_mouse(x, y, duration=0.3):
    try:
        pyautogui.moveTo(x, y, duration=duration)
        return f"Moved mouse to ({x}, {y})"
    except Exception as e:
        return f"Mouse move error: {e}"


# ============================================================
# CLICK
# ============================================================

def click(x=None, y=None):
    try:
        if x is not None and y is not None:
            pyautogui.click(x, y)
        else:
            pyautogui.click()

        return "Mouse clicked."

    except Exception as e:
        return f"Click error: {e}"


# ============================================================
# DOUBLE CLICK
# ============================================================

def double_click(x=None, y=None):
    try:
        if x is not None and y is not None:
            pyautogui.doubleClick(x, y)
        else:
            pyautogui.doubleClick()

        return "Double-clicked."

    except Exception as e:
        return f"Double-click error: {e}"


# ============================================================
# TYPE TEXT
# ============================================================

def type_text(text, interval=0.02):
    try:
        pyautogui.write(text, interval=interval)
        return "Text typed."

    except Exception as e:
        return f"Typing error: {e}"


# ============================================================
# PRESS KEY
# ============================================================

def press_key(key):
    try:
        pyautogui.press(key)
        return f"Pressed {key}."

    except Exception as e:
        return f"Key press error: {e}"


# ============================================================
# HOTKEY
# ============================================================

def hotkey(*keys):
    try:
        pyautogui.hotkey(*keys)
        return f"Pressed {' + '.join(keys)}."

    except Exception as e:
        return f"Hotkey error: {e}"


# ============================================================
# SCROLL
# ============================================================

def scroll(amount):
    try:
        pyautogui.scroll(amount)
        return f"Scrolled {amount}."

    except Exception as e:
        return f"Scroll error: {e}"


# ============================================================
# SCREENSHOT
# ============================================================

def take_screenshot(filename="computer_control_test.png"):
    try:
        image = pyautogui.screenshot()
        image.save(filename)

        return f"Screenshot saved: {filename}"

    except Exception as e:
        return f"Screenshot error: {e}"


# ============================================================
# WAIT
# ============================================================

def wait(seconds=1):
    try:
        time.sleep(seconds)
        return f"Waited {seconds} second(s)."

    except Exception as e:
        return f"Wait error: {e}"