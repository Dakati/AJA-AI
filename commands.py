import os
import re
import webbrowser


def run_command(command):
    cmd = command.lower().strip()

    # Remove punctuation
    cmd = re.sub(r"[^\w\s]", "", cmd)

    # ---------- Chrome ----------
    if "chrome" in cmd:
        os.system("start chrome")
        return "Opening Chrome..."

    # ---------- Google ----------
    if "google" in cmd:
        webbrowser.open("https://www.google.com")
        return "Opening Google..."

    # ---------- YouTube ----------
    if "youtube" in cmd:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube..."

    # ---------- Notepad ----------
    if "notepad" in cmd:
        os.system("notepad")
        return "Opening Notepad..."

    # ---------- Calculator ----------
    if "calculator" in cmd or "calc" in cmd:
        os.system("calc")
        return "Opening Calculator..."

    # ---------- VS Code ----------
    if "vs code" in cmd or "vscode" in cmd:
        os.system("code")
        return "Opening VS Code..."

    # ---------- Screenshot ----------
    if "screenshot" in cmd:
        os.system("start ms-screenclip:")
        return "Opening Windows Snipping Tool..."

    # ---------- Downloads ----------
    if "downloads" in cmd:
        os.startfile(os.path.expanduser("~/Downloads"))
        return "Opening Downloads..."

    # ---------- Desktop ----------
    if "desktop" in cmd:
        os.startfile(os.path.join(os.path.expanduser("~"), "Desktop"))
        return "Opening Desktop..."

    # ---------- Documents ----------
    if "documents" in cmd:
        os.startfile(os.path.join(os.path.expanduser("~"), "Documents"))
        return "Opening Documents..."

    # ---------- C Drive ----------
    if "c drive" in cmd or "cdrive" in cmd:
        os.startfile("C:\\")
        return "Opening C Drive..."

    # ---------- Paint ----------
    if "paint" in cmd:
        os.system("mspaint")
        return "Opening Paint..."

    # ---------- File Explorer ----------
    if "explorer" in cmd or "file explorer" in cmd:
        os.system("explorer")
        return "Opening File Explorer..."

    # ---------- Task Manager ----------
    if "task manager" in cmd:
        os.system("taskmgr")
        return "Opening Task Manager..."

    # ---------- Command Prompt ----------
    if "command prompt" in cmd or "cmd" == cmd:
        os.system("start cmd")
        return "Opening Command Prompt..."

    return None