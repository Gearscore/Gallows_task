import random
from data import words
import terminal_ui
from sys import exit as sys_exit



def createPlayer() -> dict:
    word = random.choice(list(words.keys())).lower()
    description = words[word]
    return {
        "secretWords": tuple([i, "_"] for i in word),
        "descriptionWords": description,
        "errLetters": [],
    }


def searchLetter(p: dict, l: str):
    flag = False
    for value in p["secretWords"]:
        if value[0] == l:
            value[1] = l
            flag = True
    if not flag:
        p["errLetters"] += [l]


def checkVictoryOrLoss(p: dict) -> bool:
    if len(p["errLetters"]) == 7:
        terminal_ui.infoStatusGame(p)
        print("Вы проиграли Вас повесили!!!")
        return True
    if tuple(i[0] for i in p['secretWords']) == tuple(i[1] for i in p['secretWords']):
        terminal_ui.infoStatusGame(p)
        print(f"ДА! Секретное слово - {''.join(i[1] for i in p['secretWords']).upper()}! Вы угадали!")
        return True
    return False


def restart_game():
    while True:
        s = input("Хотите сыграть еще? (да или нет): ").lower()
        if s in ("да", "нет"):
            if s == "да":
                main_func()
            sys_exit(0)


def main_func():
    PLAYER_1 = createPlayer()
    # print(' '.join(i[0] for i in PLAYER_1['secretWords']))
    while True:
        terminal_ui.infoStatusGame(PLAYER_1)
        letter = terminal_ui.inputPlayer(PLAYER_1)
        searchLetter(PLAYER_1, letter)
        if checkVictoryOrLoss(PLAYER_1):
            restart_game()


if __name__ == '__main__':
    main_func()
