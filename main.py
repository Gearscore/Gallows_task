import random
from data import words
from terminal_ui import show_graphic

player1 = {'numErr': 0}


def random_word() -> tuple[str, str, str]:
    random_key = random.choice(list(words.keys()))
    random_value = words[random_key]
    mask_word = " ".join("_" * len(random_key))
    return random_key, random_value, mask_word


def welcome():
    print("G A M E - G A L L O W S")


if __name__ == '__main__':
    welcome()
    word, described, mask = random_word()
    print(word, described, mask)
