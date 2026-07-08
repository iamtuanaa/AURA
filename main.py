from datetime import datetime

print("=" * 45)
print("🤖 Welcome to AURA")
print("=" * 45)

# Kullanıcıyı hafızadan oku
dosya = open("memory/user.txt", "r")
name = dosya.read().strip()
dosya.close()

# Eğer hafıza boşsa kullanıcıdan isim al
if name == "":
    name = input("What is your name? ")

    dosya = open("memory/user.txt", "w")
    dosya.write(name)
    dosya.close()

    print(f"\nWelcome, {name}! 🚀")

# Hafızada isim varsa
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