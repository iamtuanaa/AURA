def add_note():
    note = input("Write your note: ")

    dosya = open("data/notes.txt", "a")
    dosya.write(note + "\n")
    dosya.close()

    print("✅ Note saved!")


def show_notes():
    dosya = open("data/notes.txt", "r")
    notes = dosya.read()
    dosya.close()

    if notes == "":
        print("📭 No notes found.")
    else:
        print("\n===== YOUR NOTES =====")
        print(notes)