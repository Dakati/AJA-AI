from datetime import datetime
from system_info import get_system_status, health_check, get_system_info
from ai import ask_ai
from memory import load_memory, save_memory
from commands import run_command
from voice import speak, listen
from browser import google, youtube
from notes import add_note, show_notes, delete_note
from planner import create_plan
from vision import open_image, read_text, describe_image

print("=" * 60)
print("🤖 AJA AI Assistant v2.0")
print("=" * 60)

messages = load_memory()
mode = "text"

while True:

    # ---------------- INPUT ----------------

    if mode == "voice":

        user = listen()

        if not user:
            continue

    else:

        user = input("You: ")

    user = user.strip()

    # ---------------- PLANNER ----------------

    plan = create_plan(user)

    print("\n===== AJA PLAN =====")

    for i, step in enumerate(plan, 1):
        print(f"{i}. {step}")

    print("====================\n")
    # ---------------- PLAN EXECUTION ----------------

if "chrome" in user.lower() and "search" in user.lower():

    result = run_command(user)

    if result:
        print("AJA:", result)
        speak(result)

    continue

    # ---------------- EXIT ----------------

    if user.lower() == "exit":

        save_memory(messages)

        speak("Goodbye Aja")

        break

    # ---------------- MODE ----------------

    if user.lower() == "voice":

        mode = "voice"

        speak("Voice mode enabled")

        continue

    if user.lower() == "text":

        mode = "text"

        print("Text mode enabled")

        continue

    # ---------------- TIME ----------------

    if user.lower() == "time":

        now = datetime.now().strftime("%I:%M %p")

        print("AJA:", now)

        speak(now)

        continue

    # ---------------- DATE ----------------

    if user.lower() == "date":

        today = datetime.now().strftime("%d-%m-%Y")

        print("AJA:", today)

        speak(today)

        continue
        # ---------------- SYSTEM STATUS ----------------

    if user.lower() == "system status":

        status = get_system_status()

        print(status)

        speak("Here is your system status.")

        continue
        # ---------------- HEALTH CHECK ----------------

    if user.lower() == "health check":

        report = health_check()

        print(report)

        speak("System health check completed.")

        continue
        # ---------------- SYSTEM INFO ----------------

    if user.lower() == "system info":

        info = get_system_info()

        print(info)

        speak("Showing system information.")

        continue
        # ---------------- VISION ----------------

    if user.lower().startswith("vision "):

        path = user[7:].strip()

        result = open_image(path)

        print(result)

        speak(result)

        continue
        # ---------------- OCR ----------------

    if user.lower().startswith("read image "):

        path = user[11:].strip()

        text = read_text(path)

        print("\n===== OCR RESULT =====\n")
        print(text)
        print("\n======================\n")

        speak("Image text reading completed.")

        continue
        # ---------------- AI IMAGE DESCRIPTION ----------------

    if user.lower().startswith("describe "):

        path = user[9:].strip()

        print("\nAnalyzing image... Please wait.\n")

        result = describe_image(path)

        print("\n===== IMAGE DESCRIPTION =====\n")
        print(result)
        print("\n=============================\n")

        speak("Image analysis completed.")

        continue
        # ---------------- WINDOWS COMMANDS ----------------

    result = run_command(user)

    if result:
        print("AJA:", result)
        speak(result)
        continue

    # ---------------- GOOGLE SEARCH ----------------

    if user.lower().startswith("google "):

        query = user[7:]

        msg = google(query)

        print("AJA:", msg)

        speak(msg)

        continue

    # ---------------- YOUTUBE SEARCH ----------------

    if user.lower().startswith("youtube "):

        query = user[8:]

        msg = youtube(query)

        print("AJA:", msg)

        speak(msg)

        continue

    # ---------------- NOTES ----------------

    if user.lower().startswith("note "):

        msg = add_note(user[5:])

        print("AJA:", msg)

        speak(msg)

        continue

    if user.lower() == "show notes":

        msg = show_notes()

        print(msg)

        speak("Showing notes.")

        continue

    if user.lower().startswith("delete note "):

        try:
            number = int(user.split()[-1])
            msg = delete_note(number)

        except:

            msg = "Invalid note number."

        print("AJA:", msg)

        speak(msg)

        continue
        # ---------------- AI CHAT ----------------

    messages.append({
        "role": "user",
        "content": user
    })

    try:

        reply = ask_ai(messages)

        print("\nAJA:", reply, "\n")

        speak(reply)

        messages.append({
            "role": "assistant",
            "content": reply
        })

        save_memory(messages)

    except Exception as e:

        print("Error:", e)

        speak("Sorry Aja. Something went wrong.")