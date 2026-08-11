import os
import re
import webbrowser
import urllib.parse

from computer_control import (
    get_mouse_position,
    move_mouse,
    click,
    double_click,
    type_text,
    press_key,
    hotkey,
    scroll,
    take_screenshot,
    wait
)


def run_command(command):

    cmd = command.lower().strip()

    # Remove punctuation
    cmd = re.sub(r"[^\w\s:/.-]", "", cmd)


    # ==================================================
    # GOOGLE SEARCH
    # ==================================================

    if "search" in cmd and "youtube" not in cmd:

        query = cmd

        query = query.replace("open chrome", "")
        query = query.replace("google search", "")
        query = query.replace("search google", "")
        query = query.replace("search", "")
        query = query.replace("google", "")
        query = query.replace("chrome", "")

        query = query.strip()

        if query:

            os.system("start chrome")

            url = (
                "https://www.google.com/search?q="
                + urllib.parse.quote_plus(query)
            )

            webbrowser.open_new_tab(url)

            return f"Searching Google for {query}"

        return "What should I search for?"


    # ==================================================
    # YOUTUBE SEARCH
    # ==================================================

    if "youtube" in cmd and "search" in cmd:

        query = cmd

        query = query.replace("search youtube", "")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        query = query.replace("search", "")

        query = query.strip()

        if query:

            os.system("start chrome")

            url = (
                "https://www.youtube.com/results?search_query="
                + urllib.parse.quote_plus(query)
            )

            webbrowser.open_new_tab(url)

            return f"Searching YouTube for {query}"

        return "What should I search on YouTube?"


    # ==================================================
    # OPEN GOOGLE
    # ==================================================

    if cmd == "google" or cmd == "open google":

        webbrowser.open_new_tab(
            "https://www.google.com"
        )

        return "Opening Google..."


    # ==================================================
    # OPEN YOUTUBE
    # ==================================================

    if cmd == "youtube" or cmd == "open youtube":

        webbrowser.open_new_tab(
            "https://www.youtube.com"
        )

        return "Opening YouTube..."


    # ==================================================
    # OPEN CHROME
    # ==================================================

    if cmd == "chrome" or cmd == "open chrome":

        os.system("start chrome")

        return "Opening Chrome..."


    # ==================================================
    # OPEN WEBSITE
    # ==================================================

    if cmd.startswith("open website "):

        website = cmd.replace(
            "open website ",
            "",
            1
        ).strip()

        if website:

            if not website.startswith(("http://", "https://")):
                website = "https://" + website

            webbrowser.open_new_tab(website)

            return f"Opening {website}..."

        return "Please provide a website."


    # ==================================================
    # REFRESH
    # ==================================================

    if cmd == "refresh" or cmd == "refresh page":

        os.system(
            'powershell -command '
            '"$wshell = New-Object -ComObject WScript.Shell; '
            '$wshell.SendKeys(\'{F5}\')"'
        )

        return "Refreshing the current page..."


    # ==================================================
    # NOTEPAD
    # ==================================================

    if cmd == "notepad" or cmd == "open notepad":

        os.system("notepad")

        return "Opening Notepad..."


    # ==================================================
    # CALCULATOR
    # ==================================================

    if cmd == "calculator" or cmd == "calc":

        os.system("calc")

        return "Opening Calculator..."


    # ==================================================
    # PAINT
    # ==================================================

    if cmd == "paint" or cmd == "open paint":

        os.system("mspaint")

        return "Opening Paint..."


    # ==================================================
    # FILE EXPLORER
    # ==================================================

    if cmd == "explorer" or cmd == "file explorer":

        os.system("explorer")

        return "Opening File Explorer..."


    # ==================================================
    # TASK MANAGER
    # ==================================================

    if cmd == "task manager":

        os.system("taskmgr")

        return "Opening Task Manager..."


    # ==================================================
    # COMMAND PROMPT
    # ==================================================

    if cmd == "cmd" or cmd == "command prompt":

        os.system("start cmd")

        return "Opening Command Prompt..."


    # ==================================================
    # POWERSHELL
    # ==================================================

    if cmd == "powershell" or cmd == "open powershell":

        os.system("start powershell")

        return "Opening PowerShell..."


    # ==================================================
    # VS CODE
    # ==================================================

    if cmd == "vs code" or cmd == "vscode" or cmd == "open vs code":

        os.system("code")

        return "Opening VS Code..."


    # ==================================================
    # SCREENSHOT
    # ==================================================

    if cmd == "screenshot" or cmd == "take screenshot":

        os.system("start ms-screenclip:")

        return "Opening screenshot tool..."


    # ==================================================
    # DOWNLOADS
    # ==================================================

    if cmd == "downloads" or cmd == "open downloads":

        path = os.path.join(
            os.path.expanduser("~"),
            "Downloads"
        )

        if os.path.exists(path):

            os.startfile(path)

            return "Opening Downloads..."

        return "Downloads folder not found."


    # ==================================================
    # DESKTOP
    # ==================================================

    if cmd == "desktop" or cmd == "open desktop":

        path = os.path.join(
            os.path.expanduser("~"),
            "Desktop"
        )

        if os.path.exists(path):

            os.startfile(path)

            return "Opening Desktop..."

        return "Desktop folder not found."


    # ==================================================
    # DOCUMENTS
    # ==================================================

    if cmd == "documents" or cmd == "open documents":

        path = os.path.join(
            os.path.expanduser("~"),
            "Documents"
        )

        if os.path.exists(path):

            os.startfile(path)

            return "Opening Documents..."

        return "Documents folder not found."


    # ==================================================
    # C DRIVE
    # ==================================================

    if cmd == "c drive" or cmd == "cdrive":

        os.startfile("C:\\")

        return "Opening C Drive..."


    # ==================================================
    # WINDOWS SETTINGS
    # ==================================================

    if cmd == "settings" or cmd == "open settings":

        os.system("start ms-settings:")

        return "Opening Windows Settings..."


    # ==================================================
    # SYSTEM INFORMATION
    # ==================================================

    if cmd == "system info" or cmd == "computer info":

        os.system("msinfo32")

        return "Opening System Information..."


    # ==================================================
    # DEVICE MANAGER
    # ==================================================

    if cmd == "device manager":

        os.system("devmgmt.msc")

        return "Opening Device Manager..."


    # ==================================================
    # SERVICES
    # ==================================================

    if cmd == "services":

        os.system("services.msc")

        return "Opening Windows Services..."


    # ==================================================
    # CONTROL PANEL
    # ==================================================

    if cmd == "control panel":

        os.system("control")

        return "Opening Control Panel..."


    # ==================================================
    # MOUSE POSITION
    # ==================================================

    if cmd == "mouse position" or cmd == "where is my mouse":

        return get_mouse_position()


    # ==================================================
    # MOVE MOUSE
    # ==================================================

    if cmd.startswith("move mouse to "):

        try:

            values = cmd.replace(
                "move mouse to ",
                "",
                1
            ).strip().split()

            x = int(values[0])
            y = int(values[1])

            return move_mouse(x, y)

        except (ValueError, IndexError):

            return "Use: move mouse to X Y"


    # ==================================================
    # CLICK
    # ==================================================

    if cmd == "click" or cmd == "mouse click":

        return click()


    # ==================================================
    # CLICK AT COORDINATES
    # ==================================================

    if cmd.startswith("click at "):

        try:

            values = cmd.replace(
                "click at ",
                "",
                1
            ).strip().split()

            x = int(values[0])
            y = int(values[1])

            return click(x, y)

        except (ValueError, IndexError):

            return "Use: click at X Y"


    # ==================================================
    # DOUBLE CLICK
    # ==================================================

    if cmd == "double click" or cmd == "double-click":

        return double_click()


    # ==================================================
    # DOUBLE CLICK AT
    # ==================================================

    if cmd.startswith("double click at "):

        try:

            values = cmd.replace(
                "double click at ",
                "",
                1
            ).strip().split()

            x = int(values[0])
            y = int(values[1])

            return double_click(x, y)

        except (ValueError, IndexError):

            return "Use: double click at X Y"


    # ==================================================
    # TYPE TEXT
    # ==================================================

    if cmd.startswith("type "):

        text = command[5:].strip()

        if text:

            return type_text(text)

        return "What should I type?"


    # ==================================================
    # PRESS KEY
    # ==================================================

    if cmd.startswith("press "):

        key = cmd[6:].strip()

        if key:

            return press_key(key)

        return "Which key should I press?"


    # ==================================================
    # COMMON KEYS
    # ==================================================

    if cmd == "enter" or cmd == "press enter":

        return press_key("enter")


    if cmd == "escape" or cmd == "press escape":

        return press_key("esc")


    if cmd == "backspace" or cmd == "press backspace":

        return press_key("backspace")


    if cmd == "tab" or cmd == "press tab":

        return press_key("tab")


    # ==================================================
    # SCROLL
    # ==================================================

    if cmd.startswith("scroll "):

        try:

            amount = int(
                cmd.replace("scroll ", "", 1).strip()
            )

            return scroll(amount)

        except ValueError:

            return "Please provide a number for scrolling."


    # ==================================================
    # WAIT
    # ==================================================

    if cmd.startswith("wait "):

        try:

            seconds = float(
                cmd.replace("wait ", "")
                   .replace("seconds", "")
                   .strip()
            )

            return wait(seconds)

        except ValueError:

            return "Please provide the wait time."


    # ==================================================
    # TAKE SCREENSHOT
    # ==================================================

    if cmd == "take screenshot" or cmd == "screenshot":

        return take_screenshot()


    # ==================================================
    # COPY
    # ==================================================

    if cmd == "copy":

        return hotkey("ctrl", "c")


    # ==================================================
    # PASTE
    # ==================================================

    if cmd == "paste":

        return hotkey("ctrl", "v")


    # ==================================================
    # SELECT ALL
    # ==================================================

    if cmd == "select all":

        return hotkey("ctrl", "a")


    # ==================================================
    # SAVE
    # ==================================================

    if cmd == "save":

        return hotkey("ctrl", "s")


    # ==================================================
    # NO COMMAND
    # ==================================================

    return None