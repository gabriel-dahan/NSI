from typing import List

Grid = List[List[int]]

def clear():
    import os
    os.system('cls') if os.name == 'nt' else os.system('clear')

def init_array() -> Grid:
    return [[0] * 6 for _ in range(7)]

def ask_player(player: int) -> int:
    column = int(input(f"[P{player}] Sur quelle colonne voulez vous placer un pion ? "))
    assert column <= 7, 'La colonne maximale est la colonne 7.' 
    return column

def update_grid(arr: Grid, player: int) -> Grid:
    column = ask_player(player) - 1
    running = True
    while running:
        if arr[column][0] != 0:
            print("La colonne que vous avez choisie est pleine.\nChoisissez-en une autre : ")
            column = ask_player(player) - 1
            continue
        running = False
    for i in range(1, len(arr)):
        line = -i
        if arr[column][line] != 0:
            continue
        arr[column][line] = player
        break
    return arr

def format_grid(arr: Grid) -> str:
    formated = ''
    for j in range(len(arr) - 1):
        formated += ' | '.join([str(arr[i][j]) for i in range(len(arr))]) + '\n--------------------------\n'
    return formated

def rowify(arr: Grid) -> Grid:
    return [[arr[i][j] for i in range(len(arr))] for j in range(len(arr) - 1)]

def diagonalize(arr: Grid) -> Grid:
    ltr1 = [arr[column][column + 2] for column in range(len(arr) - 3)]
    ltr2 = [arr[column][column + 1] for column in range(len(arr) - 2)]
    ltr3 = [arr[column][column] for column in range(len(arr) - 1)]
    ltr4 = [arr[column + 1][column] for column in range(len(arr) - 1)]
    ltr5 = [arr[column + 2][column] for column in range(len(arr) - 2)]
    ltr6 = [arr[column + 3][column] for column in range(len(arr) - 3)]
    print(f'{ltr1}\n{ltr2}\n{ltr3}\n{ltr4}\n{ltr5}\n{ltr6}')

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
    # l1 : [0, 0, 0, 2, 2, 2]
    # l2 : [0, 2, 2, 2, 2, 1]

def end_game(winner: int):
    import sys
    print(f'La partie est finie, le joueur {winner} à gagné !')
    sys.exit(1)

def main():
    running = True
    i = 1
    arr = init_array()
    while running:
        player = 1 if i % 2 == 0 else 2
        # check(arr)
        diagonalize(arr)
        arr = update_grid(arr, player)
        i += 1
        clear()
        print(format_grid(arr))

try:
    main()
except KeyboardInterrupt:
    import sys
    clear()
    print('Game stopped (--> KeyboardInterrupt)')
    sys.exit(1)