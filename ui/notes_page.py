import customtkinter as ctk

def create_notes(parent):

    frame = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(
        frame,
        text="📝 Notes",
        font=("Helvetica", 28, "bold")
    )
    title.pack(pady=30)

    textbox = ctk.CTkTextbox(frame)
    textbox.pack(expand=True, fill="both", padx=30, pady=20)

    return frame