def get_answer(question):

    dosya = open("data/brain.txt", "r")

    for satir in dosya:

        satir = satir.strip()

        if "=" in satir:

            soru, cevap = satir.split("=", 1)

            if soru.lower() == question.lower():
                dosya.close()
                return cevap

    dosya.close()
    return None


def save_answer(question, answer):

    dosya = open("data/brain.txt", "a")

    dosya.write(f"\n{question.lower()}={answer}")

    dosya.close()