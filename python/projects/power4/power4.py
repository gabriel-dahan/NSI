from typing import List

Grid = List[List[int]]

def clear():
    import os
    os.system('cls') if os.name == 'nt' else os.system('clear')

def init_array() -> Grid:
    return [[0] * 6 for _ in range(7)]

def ask_player(player: int, players_repr: tuple) -> int:
    column = int(input(f"[ {players_repr[player]} ] Sur quelle colonne voulez vous placer un pion ? "))
    assert column <= 7, 'La colonne maximale est la colonne 7.' 
    return column

def update_grid(arr: Grid, player: int, players_repr: tuple) -> Grid:
    column = ask_player(player, players_repr) - 1
    running = True
    while running:
        if arr[column][0] != 0:
            print("La colonne que vous avez choisie est pleine.\nChoisissez-en une autre : ")
            column = ask_player(player, players_repr) - 1
            continue
        running = False
    for i in range(1, len(arr)):
        line = -i
        if arr[column][line] != 0:
            continue
        arr[column][line] = player
        return arr
    return arr

def format_grid(arr: Grid, players_repr: tuple) -> str:
    formated = ''
    for j in range(len(arr) - 1):
        formated += ' | '.join([players_repr[arr[i][j]] for i in range(len(arr))]) + \
            '\n--------------------------\n'
    return formated

def rowify(arr: Grid) -> Grid:
    """
        Returns a list of the rows of the power4 grid instead of its columns.
    """
    return [[arr[i][j] for i in range(len(arr))] for j in range(len(arr) - 1)]

def diagonalize(arr: Grid) -> Grid:
    """
        Returns a list of the increasing (incr) and the deceasing (decr) diagonals of the grid.
    """
    def get_decr_in(l: Grid) -> Grid:
        decr = []
        for i in range(3):
            decr.append([l[column][column + i] for column in range(6 - i)])
            decr.append([l[column + (3 - i)][column] for column in range(4 + i)])
        return decr
    decr = get_decr_in(arr)
    incr = get_decr_in(list(reversed(arr)))
    return decr + incr

    """
        Tests unitaires :
        decr1 = [arr[column][column + 2] for column in range(4)]
        decr2 = [arr[column][column + 1] for column in range(5)]
        decr3 = [arr[column][column] for column in range(6)]
        decr4 = [arr[column + 1][column] for column in range(6)]
        decr5 = [arr[column + 2][column] for column in range(5)]
        decr6 = [arr[column + 3][column] for column in range(4)]
    """

def check(arr: Grid) -> int:
    columns_check = [check_in(column) for column in arr]
    rows_check = [check_in(row) for row in rowify(arr)]
    diag_check = [check_in(diag) for diag in diagonalize(arr)]
    general_check = columns_check + rows_check + diag_check
    for winner in general_check:
        if winner == 0:
            continue
        return winner
    return 0

def check_in(l: list) -> int:
    """ 
        Checks whether a number appears 4 times in a row in a simple list. 
        Returns 0 if no one got 4 and 1 or 2 otherwise depending on the winner.
    """
    sequence = 1
    temp = 0
    for i in range(len(l)):
        temp = l[i]
        if (l[i + 1] if len(l) != i + 1 else 0) == temp:
            sequence += 1
        else:
            sequence = 1
        if sequence == 4:
            return temp
    return 0

def end_game(winner: int, players_repr: tuple):
    import sys
    print(f'La partie est finie, le joueur {players_repr[winner]} à gagné !')
    sys.exit(1)

def main(players_repr: tuple = (' ', '⬟', '⬠')):
    running = True
    i = 1
    arr = init_array()
    while running:
        player = 1 if i % 2 == 0 else 2
        winner = check(arr)
        if winner != 0:
            end_game(winner, players_repr)
        arr = update_grid(arr, player, players_repr)
        i += 1
        clear()
        print(format_grid(arr, players_repr))

try:
    main()
except KeyboardInterrupt:
    import sys
    clear()
    print('Game stopped (--> KeyboardInterrupt)')
    sys.exit(1)