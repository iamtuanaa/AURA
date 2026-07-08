print("=" * 45)
print("🤖 Welcome to AURA")
print("=" * 45)

name = input("What is your name? ")

print()

print(f"Welcome, {name}! 🚀")

while True:

    print("\n===== MENU =====")
    print("1 - Say Hello")
    print("2 - Tell Time")
    print("3 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        print(f"Hello {name}! 👋")

    elif choice == "2":

        from datetime import datetime

        now = datetime.now()

        print(now.strftime("%H:%M:%S"))

    elif choice == "3":

        print("Goodbye!")

        break

    else:

        print("Invalid option.")