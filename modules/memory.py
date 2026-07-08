def load_user():
    dosya = open("memory/user.txt", "r")
    name = dosya.read().strip()
    dosya.close()

    return name


def save_user(name):
    dosya = open("memory/user.txt", "w")
    dosya.write(name)
    dosya.close()