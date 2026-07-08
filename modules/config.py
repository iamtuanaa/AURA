import json

def load_config():

    with open("data/config.json", "r") as file:

        return json.load(file)