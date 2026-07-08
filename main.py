from datetime import datetime
from modules.memory import load_user, save_user

print("=" * 45)
print("🤖 Welcome to AURA")
print("=" * 45)

# Kullanıcıyı hafızadan oku
name = load_user()

# Hafıza boşsa isim iste
if name == "":
    name = input("What is your name? ")
    save_user(name)
    print(f"\nWelcome, {name}! 🚀")
else:
    print(f"\nWelcome back, {name}! 🌸")

# Ana menü
while True:

    print("\n===== MENU =====")
    print("1 - Say Hello")
    print("2 - Tell Time")
    print("3 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        print(f"\nHello {name}! 👋")

    elif choice == "2":
        now = datetime.now()
        print(f"\nCurrent Time: {now.strftime('%H:%M:%S')}")

    elif choice == "3":
        print("\nGoodbye! 👋")
        break

    else:
        print("\nInvalid option!")