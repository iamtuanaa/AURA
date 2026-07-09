import customtkinter as ctk

from modules.chat import process_message
from modules.history import load_history, save_message


def create_chat(parent):

    frame = ctk.CTkFrame(parent)
    frame.pack(expand=True, fill="both")

    # Başlık
    title = ctk.CTkLabel(
        frame,
        text="Hello, Tuana! 🌸",
        font=("Helvetica", 30, "bold")
    )
    title.pack(pady=20)

    # Sohbet kutusu
    chat_box = ctk.CTkTextbox(
        frame,
        corner_radius=15,
        font=("Helvetica", 15)
    )

    chat_box.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=20
    )

    # Geçmişi yükle
    history = load_history()

    if history:
        chat_box.insert("end", history)
    else:
        chat_box.insert(
            "end",
            "🌸 Welcome back, Tuana!\n\n"
            "🤖 Hi! I'm AURA.\n"
            "How can I help you today?\n\n"
        )

    # Sohbet kutusunu kilitle
    chat_box.configure(state="disabled")

    # Alt bölüm
    bottom = ctk.CTkFrame(
        frame,
        fg_color="transparent"
    )

    bottom.pack(
        fill="x",
        padx=30,
        pady=(0, 20)
    )

    # Mesaj kutusu
    entry = ctk.CTkEntry(
        bottom,
        height=40,
        corner_radius=12,
        placeholder_text="Ask AURA anything..."
    )

    entry.pack(
        side="left",
        fill="x",
        expand=True,
        padx=(0, 10)
    )

    def send():

        message = entry.get().strip()

        if message == "":
            return

        # Yazılabilir yap
        chat_box.configure(state="normal")

        # Kullanıcı mesajı
        chat_box.insert(
            "end",
            f"\n👤 You\n{message}\n\n"
        )

        save_message("👤 You", message)

        # AURA cevabı
        answer = process_message(message)

        chat_box.insert(
            "end",
            f"🤖 AURA\n{answer}\n\n"
        )

        save_message("🤖 AURA", answer)

        # En alta kaydır
        chat_box.see("end")

        # Tekrar kilitle
        chat_box.configure(state="disabled")

        # Giriş kutusunu temizle
        entry.delete(0, "end")

    # Gönder butonu
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

    # Enter ile gönder
    entry.bind("<Return>", lambda event: send())

    return frame