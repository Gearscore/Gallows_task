def welcome():
    print('И Г Р А - "В И С Е Л И Ц А"')


def show_drawing(frameNum: int):
    match frameNum:
        case 0:
            print(r"""
    +---+  
        |  
        |  
        |  
        |  
        |  
=========""")
        case 1:
            print(r"""
    +---+  
    |   |  
        |  
        |  
        |  
        |  
=========""")
        case 2:
            print(r"""
    +---+  
    |   |  
    O   |  
        |  
        |  
        |  
=========""")
        case 3:
            print(r"""
    +---+  
    |   |  
    O   |  
   /    |  
        |  
        |  
=========""")
        case 4:
            print(r"""
    +---+  
    |   |  
    O   |  
   / \  |  
        |  
        |  
=========""")
        case 5:
            print(r"""
    +---+  
    |   |  
    O   |  
   /|\  |  
        |  
        |  
=========""")
        case 6:
            print(r"""
    +---+  
    |   |  
    O   |  
   /|\  |  
   /    |  
        |  
=========""")
        case 7:
            print(r"""
    +---+  
    |   |  
    O   |  
   /|\  |  
   / \  |  
        |  
=========""")


def nextGameStep(p: dict):
    show_drawing(len(p["errLetters"]))
    print(f"Загаданное слово - {' '.join(i[1] for i in p['secretWords'])}\nПодсказка ({p['descriptionWords']})")
    if p['errLetters']:
        print(f"Ошибочные буквы: {' '.join(p['errLetters'])}")


def inputPlayer(p: dict) -> str:
    while True:
        s = input("Введите букву: ").lower()
        if len(s) == 1 and s.isalpha() and not s in p["errLetters"]:
            break
        else:
            print("Некорректный ввод ;(")
    return s
