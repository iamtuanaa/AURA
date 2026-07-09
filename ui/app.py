import customtkinter as ctk

from ui.sidebar import create_sidebar
from ui.chat_page import create_chat

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("🤖 AURA")
app.geometry("1200x700")

create_sidebar(app)
create_chat(app)

app.mainloop()