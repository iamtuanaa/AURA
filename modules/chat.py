from modules.brain import get_answer, save_answer

# AURA'nın öğrenmeye çalıştığı soru
learning_question = None


def process_message(message):
    global learning_question

    message = message.strip()

    if message == "":
        return "Please type a message."

    # Eğer AURA öğrenme modundaysa
    if learning_question is not None:

        save_answer(learning_question, message)

        learning_question = None

        return "💖 Thank you! I'll remember that."

    # Bilinen cevap var mı?
    answer = get_answer(message)

    if answer is None:

        learning_question = message

        return (
            "🤔 I don't know the answer yet.\n"
            "What should I answer next time?"
        )

    return answer