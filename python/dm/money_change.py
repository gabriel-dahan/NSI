def money_change(asked: int, paid: int, cash_register: list) -> list:
    """ Returns a list of the number of each type of currency the cashier must return. """
    assert paid >= asked, 'You don\'t have enough money to pay.'
    rest = paid - asked
    currencies = [
        [50, 0],
        [20, 0],
        [10, 0],
        [5, 0],
        [2, 0],
        [1, 0]
    ]
    for i, ctype in enumerate(currencies):
        running = True
        while running and rest >= ctype[0]:
            if cash_register[i] - 1 < 0:
                running = False
                continue
            cash_register[i] -= 1
            ctype[1] += 1
            rest -= ctype[0]
    return currencies

def format_change(currencies: list) -> None:
    """ Prints the change to be returned by the cashier. """
    # change = '\n - ' + '\n - '.join([f"{currency[1]} x {currency[0]}$" for currency in currencies if currency[1] > 0])
    change = ''
    for currency in currencies:
        if not currency[1] > 0:
            continue
        change += f'\n - {currency[1]} x {currency[0]}$'
    print(f'Change to be returned : {change}')

def main(asked: int, paid: int):
    format_change(money_change(asked, paid))

if __name__ == '__main__':
    nb_1euro = 15
    nb_2euros = 4
    nb_5euros = 4
    nb_10euros = 10
    nb_20euros = 5
    nb_50euros = 4
    cash_register = [
        nb_50euros,
        nb_20euros,
        nb_10euros,
        nb_5euros,
        nb_2euros,
        nb_1euro
    ]
    format_change(money_change(12, 455, cash_register))