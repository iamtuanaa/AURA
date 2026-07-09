from datetime import datetime
from modules.ui import show_logo
from modules.memory import load_user, save_user
from modules.notes import add_note, show_notes
from modules.chat import chat
from modules.config import load_config

# ===== COLORS =====
PINK = "\033[95m"
WHITE = "\033[97m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# ===== CONFIG =====
config = load_config()

config = load_config()
show_logo(config)

# ===== USER =====
name = load_user()

if name == "":
    name = input(CYAN + "What is your name? " + RESET)
    save_user(name)
    print(GREEN + f"\n🚀 Welcome, {name}!" + RESET)
else:
    print(WHITE + f"\n✨ Welcome back, {name}! 🌸" + RESET)

# ===== MAIN MENU =====
while True:

    print(PINK)
    print("╔════════════════ MENU ════════════════╗")
    print("║                                      ║")
    print("║  1️⃣  Say Hello                      ║")
    print("║  2️⃣  Tell Time                      ║")
    print("║  3️⃣  Add Note                       ║")
    print("║  4️⃣  Show Notes                     ║")
    print("║  5️⃣  Chat with AURA                 ║")
    print("║  6️⃣  Exit                           ║")
    print("║                                      ║")
    print("╚══════════════════════════════════════╝")
    print(RESET)

    choice = input(CYAN + "➜ Choose an option: " + RESET)

    if choice == "1":
        print(GREEN + f"\n👋 Hello, {name}!" + RESET)

    elif choice == "2":
        now = datetime.now()
        print(YELLOW + f"\n🕒 Current Time: {now.strftime('%H:%M:%S')}" + RESET)

    elif choice == "3":
        add_note()

    elif choice == "4":
        show_notes()

    elif choice == "5":
        chat()

    elif choice == "6":
        print(RED + "\n👋 Goodbye! See you soon." + RESET)
        break

    else:
        print(RED + "\n❌ Invalid option!" + RESET)