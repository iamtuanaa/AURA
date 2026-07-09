import customtkinter as ctk

PINK = "#ff66cc"
HOVER = "#ff4db8"


def create_sidebar(parent, chat, notes, memory, settings):

    logo = ctk.CTkLabel(
        parent,
        text="💖 AURA",
        font=("Helvetica", 30, "bold"),
        text_color=PINK
    )

    logo.pack(pady=(40, 40))

    ctk.CTkButton(
        parent,
        text="💬 Chat",
        command=chat,
        fg_color=PINK,
        hover_color=HOVER
    ).pack(fill="x", padx=20, pady=10)

    ctk.CTkButton(
        parent,
        text="📝 Notes",
        command=notes,
        fg_color=PINK,
        hover_color=HOVER
    ).pack(fill="x", padx=20, pady=10)

    ctk.CTkButton(
        parent,
        text="🧠 Memory",
        command=memory,
        fg_color=PINK,
        hover_color=HOVER
    ).pack(fill="x", padx=20, pady=10)

    ctk.CTkButton(
        parent,
        text="⚙️ Settings",
        command=settings,
        fg_color=PINK,
        hover_color=HOVER
    ).pack(fill="x", padx=20, pady=10)