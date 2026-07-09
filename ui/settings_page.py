import customtkinter as ctk

def create_settings(parent):

    frame = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(
        frame,
        text="⚙️ Settings",
        font=("Helvetica", 28, "bold")
    )
    title.pack(pady=30)

    label = ctk.CTkLabel(
        frame,
        text="Settings page"
    )
    label.pack()

    return frame