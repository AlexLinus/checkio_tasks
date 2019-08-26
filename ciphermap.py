#https://py.checkio.org/ru/mission/cipher-map2/
def recall_password(grille, pw):
    solution = []
    print('Оригинальный grille')
    print(grille)

    #перебираем от 1 до 4, _ (underscore) показывает, что данную переменная дальше нигде не исользуется. Это то же самое что и i, или x.
    print(list(zip(grille, pw)))
    for _ in range(4):
        for rows in zip(grille, pw):
            print(rows)
            for g, p in zip(*rows):
                if g == 'X':
                    solution.append(p)
        grille = list(zip(*grille[::-1]))
        print('Сейчас будет Grille')
        print(grille)
        print('Конец grille')
        print('Сейчас будет solution')
        print(solution)
    return ''.join(solution)
#a = [1, 3, 8, 7]
#a[::-1]
#[7, 8, 3, 1]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforg iddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'