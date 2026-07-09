import json
import os

BRAIN_FILE = "data/brain.json"


def load_brain():

    if not os.path.exists(BRAIN_FILE):

        with open(BRAIN_FILE, "w") as file:
            json.dump({}, file)

    with open(BRAIN_FILE, "r") as file:
        return json.load(file)


def save_brain(brain):

    with open(BRAIN_FILE, "w") as file:
        json.dump(brain, file, indent=4)


def get_answer(question):

    brain = load_brain()

    return brain.get(question.lower())


def save_answer(question, answer):

    brain = load_brain()

    brain[question.lower()] = answer

    save_brain(brain)


def get_memory():

    return load_brain()