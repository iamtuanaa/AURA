import customtkinter as ctk

from ui.sidebar import create_sidebar
from ui.chat_page import create_chat
from ui.notes_page import create_notes
from ui.memory_page import create_memory
from ui.settings_page import create_settings

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("💖 AURA")
app.geometry("1200x700")

# Sidebar
sidebar = ctk.CTkFrame(app, width=220)
sidebar.pack(side="left", fill="y")

# Main Content
content = ctk.CTkFrame(app)
content.pack(side="right", expand=True, fill="both")


def clear_content():
    for widget in content.winfo_children():
        widget.destroy()


def show_chat():
    clear_content()
    create_chat(content)


def show_notes():
    clear_content()
    create_notes(content)


def show_memory():
    clear_content()
    create_memory(content)


def show_settings():
    clear_content()
    create_settings(content)


create_sidebar(
    sidebar,
    show_chat,
    show_notes,
    show_memory,
    show_settings
)

show_chat()

app.mainloop()