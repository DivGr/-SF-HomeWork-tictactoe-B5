from colorama import *

init(autoreset=True)

from emoji import emojize

table = [[emojize(':smiling_face_with_sunglasses:')] * 3 for _ in range(3)]

name1 = input(Fore.GREEN + 'Введите имя игрока №1 (игра за крестики):')
name2 = input(Fore.GREEN + 'Введите имя игрока №2 (игра за нолики):')


def field(t):
    coord = '   0  1  2'
    coord_2 = 'a b c'
    print(coord)
    # zip
    for row, column in zip(t, coord_2.split()):
        print(f"{column} {' '.join(row)}")


def input_player(t):
    while True:
        in_coord = input(Fore.GREEN + 'Введите координаты в формате: буква (a, b, c) и число (0, 1, 2):').split()
        if len(in_coord) != 2:
            print(Fore.RED + 'Введите две координаты', emojize(":angry_face:"))
            continue
        if not (in_coord[0].isalpha() and in_coord[1].isdigit()):
            print(Fore.RED + 'Ну не правильно! Поменяйте координаты местами!', emojize(":angry_face:"))
            continue
        if not (in_coord[0].isalpha()):
            print(Fore.RED + 'Первая координата - это буква (a, b, c), а вы ввели цифру!', emojize(":angry_face:"),
                  'введите букву!')
            continue
        if not (in_coord[1].isdigit()):
            print(Fore.RED + 'Вторая координата - это число (0, 1, 2), а вы ввели букву!', emojize(":angry_face:"),
                  'введите число!')
            continue
        x = in_coord[0]
        y = int(in_coord[1])
        if not ((x == 'a' or x == 'b' or x == 'c') and y >= 0 and y < 3):
            print(Fore.RED + 'Не верное значение координат!', emojize(":angry_face:"),
                  Fore.RED + 'Введите координаты в формате: буква (a, b, c) и число (0, 1, 2)')
            continue
        if x == 'a':
            x = 0
        elif x == 'b':
            x = 1
        elif x == 'c':
            x = 2

        if t[x][y] != emojize(":smiling_face_with_sunglasses:"):
            print(Fore.RED + 'Ячейка занята!!!!!!')
            continue
        break
    return x, y


def win_player(t, player):
    t_list = []
    for l in t:
        t_list += l
    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    signs = set([i for i, n in enumerate(t_list) if n == player])
    for p in positions:
        if len(signs.intersection(set(p))) == 3:
            return True
    return False


def start_game(table):
    count = 0
    while True:
        field(table)
        if count % 2 == 0:
            player = ' x'
            print(Fore.MAGENTA + f'Ходит {name1}')
        else:
            player = ' 0'
            print(Fore.CYAN + f'Ходит {name2}')
        if count < 9:
            x, y = input_player(table)
            table[x][y] = player
        elif count == 9:
            print(Fore.YELLOW + Style.BRIGHT + 'Ничья!!!')
            break
        if win_player(table, player):
            field(table)
            if table[x][y] == ' x':
                print(Fore.BLUE + Style.BRIGHT + f'Поздравляю! Выиграл {name1}', emojize(":star-struck:"))
            else:
                print(Fore.BLUE + Style.BRIGHT + f'Поздравляю! Выиграл {name2}', emojize(":star-struck:"))
            break
        count += 1


start_game(table)
