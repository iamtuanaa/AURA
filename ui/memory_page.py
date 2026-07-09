import customtkinter as ctk

from modules.memory import load_user
from modules.brain import get_memory


def create_memory(parent):

    frame = ctk.CTkFrame(parent)
    frame.pack(expand=True, fill="both")

    title = ctk.CTkLabel(
        frame,
        text="🧠 AURA MEMORY",
        font=("Helvetica", 30, "bold")
    )
    title.pack(pady=20)

    username = load_user()

    user_label = ctk.CTkLabel(
        frame,
        text=f"👤 User: {username}",
        font=("Helvetica", 18)
    )
    user_label.pack()

    chat_box = ctk.CTkTextbox(
        frame,
        font=("Helvetica", 15)
    )

    chat_box.pack(
        expand=True,
        fill="both",
        padx=30,
        pady=20
    )

    memory = get_memory()

    if len(memory) == 0:

        chat_box.insert(
            "end",
            "🌸 AURA hasn't learned anything yet."
        )

    else:

        for question, answer in memory.items():

            chat_box.insert(
                "end",
                f"❓ {question}\n"
                f"💖 {answer}\n\n"
            )

    chat_box.configure(state="disabled")

    return frame