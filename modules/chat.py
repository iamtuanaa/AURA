from modules.brain import get_answer, save_answer


def chat():

    print("\n🤖 Chat Mode")
    print("Type 'exit' to return to menu.\n")

    while True:

        message = input("You: ")

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

            print(f"🤖 AURA: {answer}")