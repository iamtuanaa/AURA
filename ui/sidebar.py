import customtkinter as ctk
from ui.colors import *


def create_sidebar(parent):

    sidebar = ctk.CTkFrame(
        parent,
        width=220,
        fg_color=SIDEBAR,
        corner_radius=0
    )

    sidebar.pack(side="left", fill="y")

    logo = ctk.CTkLabel(
        sidebar,
        text="💖 AURA",
        font=("Helvetica", 28, "bold"),
        text_color=PINK
    )

    logo.pack(pady=(30, 40))

    pages = [
        "💬 Chat",
        "📝 Notes",
        "🧠 Memory",
        "⚙️ Settings"
    ]

    for page in pages:
        button = ctk.CTkButton(
            sidebar,
            text=page,
            fg_color=PINK,
            hover_color=HOVER,
            corner_radius=12
        )

        button.pack(fill="x", padx=20, pady=10)

    return sidebar