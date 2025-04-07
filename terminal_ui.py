import os
import platform


def cleaningScreen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def show_gallows(frameNum: int):
    print('  И Г Р А - "В И С Е Л И Ц А"')
    print("*" * 31, end="")
    match frameNum:
        case 0:
            print(r"""
  [Живой]   +---+ 
                |  
                |  
                |  
                |  
                |  
        =========""")
        case 1:
            print(r"""
  [Живой]   +---+ 
            |   |  верёвка
                |  
                |  
                |  
                |  
        =========""")
        case 2:
            print(r"""
  [Живой]   +---+ 
            |   |  верёвка
            O   |  голова
                |  
                |  
                |  
        =========""")
        case 3:
            print(r"""
  [Живой]   +---+  
            |   |  верёвка
            O   |  голова
           /    |  рука
                |  
                |  
        =========""")
        case 4:
            print(r"""
  [Живой]   +---+  
            |   |  верёвка
            O   |  голова
           / \  |  руки
                |  
                |  
        =========""")
        case 5:
            print(r"""
  [Живой]   +---+
            |   |  верёвка
            O   |  голова
           /|\  |  руки, тело
                |  
                |  
        =========""")
        case 6:
            print(r"""
  [Живой]   +---+  
            |   |  верёвка
            O   |  голова
           /|\  |  руки, тело
           /    |  нога
                |  
        =========""")
        case 7:
            print(r"""
  [Повешен] +---+  
            |   |  верёвка
            O   |  голова
           /|\  |  руки, тело
           / \  |  ноги
                |  
        =========""")
    print("*" * 31)


def infoStatusGame(p: dict):
    cleaningScreen()
    show_gallows(len(p["errLetters"]))
    print(f"Загаданное слово {' '.join(i[1] for i in p['secretWords']).upper()}\nПодсказка ({p['descriptionWords']})")
    if p['errLetters']:
        print(f"Ошибочные буквы: {' '.join(p['errLetters'])}")


def inputPlayer(p: dict) -> str:
    while True:
        s = input("Введите букву: ").lower()
        if len(s) == 1 and s.isalpha() and not s in p["errLetters"]:
            if [s, s] in p["secretWords"]:
                print("Эта буква уже угадана :)")
                continue
            break
        else:
            print("Некорректный ввод ;(")
    return s
