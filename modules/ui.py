import os
import time

PINK = "\033[95m"
WHITE = "\033[97m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RESET = "\033[0m"


def clear():
    os.system("clear")


def typing(text, speed=0):
    print(text)


def show_logo(config):

    clear()

    print(PINK)

    print(r"""
               ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦

          ░█████╗░██╗░░░██╗██████╗░░█████╗░
          ██╔══██╗██║░░░██║██╔══██╗██╔══██╗
          ███████║██║░░░██║██████╔╝███████║
          ██╔══██║██║░░░██║██╔══██╗██╔══██║
          ██║░░██║╚██████╔╝██║░░██║██║░░██║
          ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝

               Artificial Intelligence
    """)

    print(WHITE + f"                 {config['name']} v{config['version']}")
    print(f"             Created by {config['creator']}")
    print(PINK + "──────────────────────────────────────────────")
    print(RESET)

    typing("💖 Initializing core modules...", 0.03)
    typing("🧠 Loading memory...", 0.03)
    typing("📚 Loading knowledge base...", 0.03)
    typing("⚡ Starting assistant...", 0.03)

    print()