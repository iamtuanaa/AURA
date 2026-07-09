import customtkinter as ctk

def create_memory(parent):

    frame = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(
        frame,
        text="🧠 Memory",
        font=("Helvetica", 28, "bold")
    )
    title.pack(pady=30)

    label = ctk.CTkLabel(
        frame,
        text="AURA's memory will appear here."
    )
    label.pack()

    return frame