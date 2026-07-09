import customtkinter as ctk

from modules.memory import load_user
from modules.brain import get_memory


def create_memory(parent):

    frame = ctk.CTkFrame(parent)
    frame.pack(expand=True, fill="both")

    title = ctk.CTkLabel(
        frame,
        text="🧠 AURA MEMORY",
        font=("Helvetica", 28, "bold")
    )

    title.pack(pady=20)

    name = load_user()

    user = ctk.CTkLabel(
        frame,
        text=f"👤 User: {name}",
        font=("Helvetica", 18)
    )

    user.pack(pady=10)

    textbox = ctk.CTkTextbox(frame)
    textbox.pack(expand=True, fill="both", padx=30, pady=20)

    knowledge = get_memory()

    if knowledge:

        for question, answer in knowledge.items():

            textbox.insert(
                "end",
                f"{question} ➜ {answer}\n\n"
            )

    else:

        textbox.insert(
            "end",
            "AURA hasn't learned anything yet."
        )

    textbox.configure(state="disabled")

    return frame