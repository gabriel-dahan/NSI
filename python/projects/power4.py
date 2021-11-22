def init_array() -> list:
    return [[0] * 6 for _ in range(7)]

def change(coords: tuple, player: int) -> None:
    pass

def clear():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def ask_player(player: int) -> int:
    column = int(input(f"[P{player}] Sur quelle colonne voulez vous placer un pion ? "))
    assert column <= 7, 'La colonne maximale est la colonne 7.' 
    return column

def update_grid(arr: list, player: int):
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

def format_grid(arr: list) -> str:
    formated = ''
    for j in range(len(arr) - 1):
        formated += ' | '.join([str(arr[i][j]) for i in range(len(arr))]) + '\n--------------------------\n'
    return formated

def end_game():
    pass

def check(arr: list):
    score = {
        1: 0,
        2: 0
    }
    for column in arr:
        for i in range(column):
            if column[i] == 1:
                check(score, 1, 2)
            elif column[i] == 2:
                check(score, 2, 1)
            else:
                score[1], score[2] = 0, 0
        
        for j in range(len(arr) - 1):
            if column[j] == 1:
                check(score, 1, 2)
            elif column[j] == 2:
                check(score, 2, 1)
            else:
                score[1], score[2] = 0, 0
    return (True | False, 1 | 2)

    
def check_line(score, player, enemy):
    score[player] += 1
    score[enemy] = 0
    if score[player] == 4:
        end_game()

def get_winner() -> int:
    pass

def main():
    running = True
    i = 1
    arr = init_array()
    while running:
        player = 1 if i % 2 == 0 else 2
        arr = update_grid(arr, player)
        i += 1
        clear()
        print(format_grid(arr))

main()