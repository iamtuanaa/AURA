import os

HISTORY_FILE = "data/chat_history.txt"


def load_history():

    if not os.path.exists(HISTORY_FILE):
        return ""

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        return file.read()


def save_message(sender, message):

    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"{sender}: {message}\n")