from datetime import datetime

# ==============================
# AJA AI MODULES
# ==============================

from ai import ask_ai

from memory import load_memory, save_memory

from voice import speak, listen

from planner import create_plan

from commands import run_command

from browser_control import BrowserController

from vision import open_image, read_text, describe_image

from notes import add_note, show_notes, delete_note

from system_info import get_system_status


# ==============================
# BROWSER
# ==============================

browser = BrowserController()


# ==============================
# STARTUP
# ==============================

print("=" * 60)
print("🤖 AJA AI ASSISTANT v2.0")
print("=" * 60)

messages = load_memory()

mode = "text"


# ==============================
# MAIN LOOP
# ==============================

while True:

    # --------------------------
    # INPUT
    # --------------------------

    if mode == "voice":

        try:
            user = listen()
        except Exception as e:
            print("AJA Voice Error:", e)
            continue

        if not user:
            continue

    else:

        try:
            user = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print("\nAJA: Goodbye!")
            break

    user = user.strip()

    if not user:
        continue

    cmd = user.lower().strip()


    # =========================================================
    # EXIT
    # =========================================================

    if cmd == "exit" or cmd == "quit":

        try:
            save_memory(messages)
        except Exception as e:
            print("Memory save error:", e)

        print("AJA: Goodbye!")
        
        try:
            speak("Goodbye Aja")
        except Exception:
            pass

        try:
            browser.close()
        except Exception:
            pass

        break


    # =========================================================
    # VOICE MODE
    # =========================================================

    if cmd == "voice":

        mode = "voice"

        print("AJA: Voice mode enabled.")

        try:
            speak("Voice mode enabled")
        except Exception:
            pass

        continue


    # =========================================================
    # TEXT MODE
    # =========================================================

    if cmd == "text":

        mode = "text"

        print("AJA: Text mode enabled.")

        continue


    # =========================================================
    # TIME
    # =========================================================

    if cmd == "time":

        now = datetime.now().strftime("%I:%M %p")

        print("AJA:", now)

        try:
            speak(now)
        except Exception:
            pass

        continue


    # =========================================================
    # DATE
    # =========================================================

    if cmd == "date":

        today = datetime.now().strftime("%d-%m-%Y")

        print("AJA:", today)

        try:
            speak(today)
        except Exception:
            pass

        continue


    # =========================================================
    # SYSTEM STATUS
    # =========================================================

    if cmd == "system status":

        try:
            result = get_system_status()
        except Exception as e:
            result = f"System status error: {e}"

        print(result)

        try:
            speak("Here is your system status")
        except Exception:
            pass

        continue


    # =========================================================
    # GOOGLE SEARCH
    # =========================================================

    if cmd.startswith("search google for "):

        query = user[len("search google for "):].strip()

        if not query:
            print("AJA: Please tell me what to search.")
            continue

        result = browser.search_google(query)

        print("AJA:", result)

        try:
            speak(result)
        except Exception:
            pass

        continue


    # =========================================================
    # YOUTUBE SEARCH
    # =========================================================

    if cmd.startswith("search youtube for "):

        query = user[len("search youtube for "):].strip()

        if not query:
            print("AJA: Please tell me what to search on YouTube.")
            continue

        result = browser.search_youtube(query)

        print("AJA:", result)

        try:
            speak(result)
        except Exception:
            pass

        continue


    # =========================================================
    # OPEN WEBSITE
    # =========================================================

    if cmd.startswith("open website "):

        website = user[len("open website "):].strip()

        if not website:
            print("AJA: Please provide a website.")
            continue

        result = browser.open(website)

        print("AJA:", result)

        try:
            speak(result)
        except Exception:
            pass

        continue


    # =========================================================
    # REFRESH
    # =========================================================

    if cmd == "refresh":

        result = browser.refresh()

        print("AJA:", result)

        try:
            speak(result)
        except Exception:
            pass

        continue


    # =========================================================
    # GO BACK
    # =========================================================

    if cmd == "go back":

        result = browser.back()

        print("AJA:", result)

        try:
            speak(result)
        except Exception:
            pass

        continue


    # =========================================================
    # GO FORWARD
    # =========================================================

    if cmd == "go forward":

        result = browser.forward()

        print("AJA:", result)

        try:
            speak(result)
        except Exception:
            pass

        continue


    # =========================================================
    # CLOSE TAB
    # =========================================================

    if cmd == "close tab":

        result = browser.close_tab()

        print("AJA:", result)

        try:
            speak(result)
        except Exception:
            pass

        continue


    # =========================================================
    # CURRENT URL
    # =========================================================

    if cmd in ("current url", "what is the current url"):

        result = browser.current_url()

        print("AJA:", result)

        continue


    # =========================================================
    # OPEN IMAGE
    # =========================================================

    if cmd.startswith("read image "):

        path = user[len("read image "):].strip()

        try:
            result = read_text(path)
        except Exception as e:
            result = f"Image reading error: {e}"

        print("AJA:", result)

        try:
            speak(result)
        except Exception:
            pass

        continue


    # =========================================================
    # DESCRIBE IMAGE
    # =========================================================

    if cmd.startswith("describe image "):

        path = user[len("describe image "):].strip()

        try:
            result = describe_image(path)
        except Exception as e:
            result = f"Image description error: {e}"

        print("AJA:", result)

        try:
            speak(result)
        except Exception:
            pass

        continue


    # =========================================================
    # NOTES - ADD
    # =========================================================

    if cmd.startswith("add note "):

        note = user[len("add note "):].strip()

        try:
            result = add_note(note)
        except Exception as e:
            result = f"Note error: {e}"

        print("AJA:", result)

        continue


    # =========================================================
    # NOTES - SHOW
    # =========================================================

    if cmd in ("show notes", "notes"):

        try:
            result = show_notes()
        except Exception as e:
            result = f"Notes error: {e}"

        print("AJA:", result)

        continue


    # =========================================================
    # NOTES - DELETE
    # =========================================================

    if cmd.startswith("delete note "):

        note = user[len("delete note "):].strip()

        try:
            result = delete_note(note)
        except Exception as e:
            result = f"Note delete error: {e}"

        print("AJA:", result)

        continue


    # =========================================================
    # PLANNER
    # =========================================================

    try:

        plan = create_plan(user)

        print("\n===== AJA PLAN =====")

        for i, step in enumerate(plan, 1):
            print(f"{i}. {step}")

        print("====================\n")

    except Exception as e:

        print("Planner error:", e)


    # =========================================================
    # COMMAND EXECUTION
    # =========================================================

    try:

        result = run_command(user)

    except Exception as e:

        result = None
        print("Command error:", e)


    if result:

        print("AJA:", result)

        try:
            speak(result)
        except Exception:
            pass

        continue


    # =========================================================
    # AI
    # =========================================================

    try:

        messages.append({
            "role": "user",
            "content": user
        })

        response = ask_ai(messages)

        print("\nAJA:", response)

        try:
            speak(response)
        except Exception:
            pass

        messages.append({
            "role": "assistant",
            "content": response
        })

        try:
            save_memory(messages)
        except Exception:
            pass

    except Exception as e:

        print("AJA AI Error:", e)