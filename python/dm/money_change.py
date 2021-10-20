def money_change(asked: int, paid: int) -> list:
    assert paid >= asked, 'You don\'t have enough money to pay.'
    rest = paid - asked
    currency = [
        [50, 0],
        [20, 0],
        [10, 0],
        [5, 0],
        [2, 0],
        [1, 0]
    ]
    for ctype in currency:
        while rest >= ctype[0]:
            ctype[1] += 1
            rest -= ctype[0]
    return currency

def format_change(currency: list) -> None:
    """ Prints the change to be returned by the cashier. """
    # change = '\n - ' + '\n - '.join([f"{elem[0]}$ --> {elem[1]}" for elem in currency if elem[1] > 0])
    change = ''
    for elem in currency:
        if not elem[1] > 0:
            continue
        change += f'\n - {elem[0]}$ --> {elem[1]}'
    print(f'Change to be returned : {change}')

if __name__ == '__main__':
    format_change(money_change(12, 50))