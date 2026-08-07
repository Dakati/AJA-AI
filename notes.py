import json
import os

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2)

def add_note(note):
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    return "Note saved."

def show_notes():
    notes = load_notes()

    if not notes:
        return "No notes found."

    text = ""

    for i, note in enumerate(notes, 1):
        text += f"{i}. {note}\n"

    return text

def delete_note(index):
    notes = load_notes()

    if index < 1 or index > len(notes):
        return "Invalid note number."

    notes.pop(index - 1)

    save_notes(notes)

    return "Note deleted."