def chat():

    message = input("\nYou: ").lower()

    if "hello" in message or "hi" in message:
        print("🤖 AURA: Hello Tuana! Nice to see you.")

    elif "how are you" in message:
        print("🤖 AURA: I'm feeling great! Thanks for asking. 💙")

    elif "your name" in message:
        print("🤖 AURA: My name is AURA.")

    elif "who made you" in message:
        print("🤖 AURA: I was created by Tuana Bilgin. 🚀")

    elif "python" in message:
        print("🤖 AURA: Python is my favorite language!")

    else:
        print("🤖 AURA: I don't know how to answer that yet.")