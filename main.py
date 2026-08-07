from datetime import datetime

from ai import ask_ai
from memory import load_memory, save_memory
from commands import run_command
from voice import speak, listen
from browser import google, youtube
from notes import add_note, show_notes, delete_note

print("=" * 50)
print("🤖 AJA AI Assistant")
print("=" * 50)

messages = load_memory()
mode = "text"

while True:

    if mode == "voice":
        user = listen()

        if not user:
            continue

    else:
        user = input("You: ")

    user = user.strip()

    if user.lower() == "exit":
        save_memory(messages)
        speak("Goodbye Aja")
        break

    if user.lower() == "voice":
        mode = "voice"
        speak("Voice mode enabled")
        continue

    if user.lower() == "text":
        mode = "text"
        print("Text mode enabled")
        continue

    if user.lower() == "time":
        now = datetime.now().strftime("%I:%M %p")
        print("AJA:", now)
        speak(now)
        continue

    if user.lower() == "date":
        today = datetime.now().strftime("%d-%m-%Y")
        print("AJA:", today)
        speak(today)
        continue
        # ---------------- WINDOWS COMMANDS ----------------

    result = run_command(user)

    if result:
        print("AJA:", result)
        speak(result)
        continue

    # ---------------- GOOGLE ----------------

    if user.lower().startswith("google "):

        query = user[7:]

        msg = google(query)

        print("AJA:", msg)

        speak(msg)

        continue

    # ---------------- YOUTUBE ----------------

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