from modules.brain import get_answer, save_answer

PINK = "\033[95m"
RESET = "\033[0m"
CYAN = "\033[96m"

def chat():

    print(PINK)
    print("══════════════════════════════")
    print("🤖      AURA CHAT MODE")
    print("══════════════════════════════")
    print(RESET)

    print("Type 'exit' to return.\n")
    print("Type 'exit' to return to menu.\n")

    while True:

        message = input(CYAN + "👤 You: " + RESET)

        if message.lower() == "exit":
            print("Leaving chat...\n")
            break

        answer = get_answer(message)

        if answer is None:

            print("🤖 I don't know the answer.")

            teach = input("Teach me? (yes/no): ")

            if teach.lower() == "yes":

                new_answer = input("What should I answer? ")

                save_answer(message, new_answer)

                print("✅ Thanks! I learned something new!")

            else:

                print("😊 Maybe next time!")

        else:

            print(PINK + f"🤖 AURA: {answer}" + RESET)