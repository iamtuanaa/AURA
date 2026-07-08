import json


def get_answer(question):

    with open("data/brain.json", "r") as file:

        brain = json.load(file)

    return brain.get(question.lower())


def save_answer(question, answer):

    with open("data/brain.json", "r") as file:

        brain = json.load(file)

    brain[question.lower()] = answer

    with open("data/brain.json", "w") as file:

        json.dump(brain, file, indent=4)