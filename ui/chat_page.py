import customtkinter as ctk
from modules.brain import get_answer


def create_chat(parent):

    frame = ctk.CTkFrame(parent)
    frame.pack(side="right", expand=True, fill="both")

    title = ctk.CTkLabel(
        frame,
        text="Hello, Tuana! 🌸",
        font=("Helvetica", 30, "bold")
    )
    title.pack(pady=20)

    chat_box = ctk.CTkTextbox(
    frame,
    corner_radius=15,
    font=("Helvetica", 15)
)
    chat_box.pack(fill="both", expand=True, padx=30, pady=20)

    chat_box.insert(
    "end",
    "🌸 Welcome back, Tuana!\n\n"
    "🤖 Hi! I'm AURA.\n"
    "How can I help you today?\n\n"
)

    # Alt bölüm
    bottom = ctk.CTkFrame(frame, fg_color="transparent")
    bottom.pack(fill="x", padx=30, pady=(0, 20))

    entry = ctk.CTkEntry(
    bottom,
    height=40,
    corner_radius=12,
    placeholder_text="Ask AURA anything..."
)
    entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

    def send():

        message = entry.get().strip()

        if not message:
            return

        chat_box.insert("end", f"👤 You: {message}\n")
        print("Mesaj:", message)
        answer = get_answer(message)
        print("Cevap:", answer)
        chat_box.insert("end", f"🤖 AURA: {answer}\n\n")

        entry.delete(0, "end")
        chat_box.see("end")

    button = ctk.CTkButton(
    bottom,
    text="💖 Send",
    command=send,
    width=120,
    fg_color="#ff66cc",
    hover_color="#ff4db8",
    corner_radius=12
)
    
    button.pack(side="right")

    # Enter tuşuyla gönder
    entry.bind("<Return>", lambda event: send())

    return frame