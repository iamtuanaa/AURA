import customtkinter as ctk
from modules.notes import add_note, show_notes


def create_notes(parent):

    frame = ctk.CTkFrame(parent)
    frame.pack(expand=True, fill="both")

    title = ctk.CTkLabel(
        frame,
        text="📝 Notes",
        font=("Helvetica", 28, "bold")
    )
    title.pack(pady=20)

    textbox = ctk.CTkTextbox(frame)
    textbox.pack(expand=True, fill="both", padx=30, pady=20)

    # Notları yükle
    try:
        with open("data/notes.txt", "r") as file:
            textbox.insert("end", file.read())
    except FileNotFoundError:
        textbox.insert("end", "No notes yet.")

    def save_note():

        note = textbox.get("1.0", "end").strip()

        with open("data/notes.txt", "w") as file:
            file.write(note)

    button = ctk.CTkButton(
        frame,
        text="💖 Save Notes",
        command=save_note,
        fg_color="#ff66cc",
        hover_color="#ff4db8"
    )

    button.pack(pady=20)

    return frame