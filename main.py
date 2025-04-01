import random
from data import words


player1 = {'numErr': 0}


def random_word() -> tuple[str, str, str]:
    random_key = random.choice(list(words.keys()))
    random_value = words[random_key]
    mask_word = " ".join("_" * len(random_key))
    return random_key, random_value, mask_word



def welcome():
    print("G A L L O W S")


def show_graphic(n: int):
    match n:
        case 1:
            print(r"""
    +---+  
        |  
        |  
        |  
        |  
        |  
=========""")
        case 2:
            print(r"""
    +---+  
    |   |  
        |  
        |  
        |  
        |  
=========""")
        case 3:
            print(r"""
    +---+  
    |   |  
    O   |  
        |  
        |  
        |  
=========""")
        case 4:
            print(r"""
    +---+  
    |   |  
    O   |  
   /    |  
        |  
        |  
=========""")
        case 5:
            print(r"""
    +---+  
    |   |  
    O   |  
   / \  |  
        |  
        |  
=========""")
        case 6:
            print(r"""
    +---+  
    |   |  
    O   |  
   /|\  |  
        |  
        |  
=========""")
        case 7:
            print(r"""
    +---+  
    |   |  
    O   |  
   /|\  |  
   /    |  
        |  
=========""")
        case 8:
            print(r"""
    +---+  
    |   |  
    O   |  
   /|\  |  
   / \  |  
        |  
=========""")


if __name__ == '__main__':
    welcome()
    word, described, mask = random_word()
    print(word, described, mask)
