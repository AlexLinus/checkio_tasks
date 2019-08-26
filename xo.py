from typing import List

def checkio(game_result):
    kletki = set()
    for item in game_result:
        print(item)
        kletki.add((item[0], item[1], item[2]))
    kletki = list(kletki)
    if kletki[0][0] == 'X' and kletki[0][1] == 'X' and kletki[0][2]  == 'X' or kletki[0][0] == 'X' and kletki[1][0] == 'X' and kletki[2][0] == 'X' or kletki[1][0] == 'X' and kletki[1][1] == 'X' and kletki[1][2] == 'X' or kletki[2][0] == 'X' and kletki[2][1] == 'X' and kletki[2][2] == 'X' or kletki[0][1] == 'X' and kletki[1][1] == 'X' and kletki[2][1] == 'X' or kletki[0][2] == 'X' and kletki[1][2] == 'X' and kletki[2][2] == 'X':
        return "X"
    elif kletki[0][0] == 'X' and kletki[1][1] == 'X' and kletki[2][2] == 'X' or kletki[2][0] == 'X' and kletki[1][1] == 'X' and kletki[0][2] == 'X':
        return "X"
    elif kletki[0][0] == 'O' and kletki[0][1] == 'O' and kletki[0][2]  == 'O' or kletki[0][0] == 'O' and kletki[1][0] == 'O' and kletki[2][0] == 'O' or kletki[1][0] == 'O' and kletki[1][1] == 'O' and kletki[1][2] == 'O' or kletki[2][0] == 'O' and kletki[2][1] == 'O' and kletki[2][2] == 'O' or kletki[0][1] == 'O' and kletki[1][1] == 'O' and kletki[2][1] == 'O' or kletki[0][2] == 'O' and kletki[1][2] == 'O' and kletki[2][2] == 'O':
        return "O"
    elif kletki[0][0] == 'O' and kletki[1][1] == 'O' and kletki[2][2] == 'O' or kletki[2][0] == 'O' and kletki[1][1] == 'O' and kletki[0][2] == 'O':
        return "O"
    else:
        return "D"

#if __name__ == '__main__':
#    print("Example:")
#    print(checkio(["X.O",
#                   "XX.",
#                   "XOO"]))
#
#    #These "asserts" using only for self-checking and not necessary for auto-testing
#    assert checkio([
#        "X.O",
#       "XX.",
#        "XOO"]) == "X", "Xs wins"
#    assert checkio([
#        "OO.",
#        "XOX",
#        "XOX"]) == "O", "Os wins"
#    assert checkio([
#        "OOX",
#        "XXO",
#        "OXX"]) == "D", "Draw"
print(checkio(["O.X", "XX.", "XOO"]))