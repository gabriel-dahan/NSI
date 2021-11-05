def money_change(asked: int, paid: int, cash_register: dict) -> dict:
    """ Returns a list of the number of each type of currency the cashier must return. """
    assert paid >= asked, 'You don\'t have enough money to pay.'
    rest = paid - asked
    # total_cash = sum(_type * cash_register[_type] for _type in cash_register)
    total_cash = []
    for _type in cash_register:
        total_cash.append(_type * cash_register[_type])
    total_cash = sum(total_cash)
    assert total_cash >= rest, 'The cash register does not contain enough money to return.'
    currencies = {
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        2: 0,
        1: 0
    }
    for _type in currencies: # For each type of currency from 50$ to 1$.
        running = True
        while running and rest >= _type: # While there's enough money to return with the current currency type.
            if cash_register[_type] < 1:
                running = False
                continue
            cash_register[_type] -= 1
            currencies[_type] += 1
            rest -= _type
    return currencies

def format_change(currencies: dict) -> None:
    """ Prints the change to be returned by the cashier. """
    # change = ''.join([f"\n - {currency} x {_type}$" for _type, currency in currencies.items() if currency > 0])
    change = ''
    for _type, currency in currencies.items():
        if not currency > 0:
            continue
        change += f'\n - {currency} x {_type}$'
    print(f'Change to be returned : {change}')

def main(asked: int, paid: int, cash_register: dict, no_format: bool = False) -> None:
    """ Launches the program. """
    change = money_change(asked, paid, cash_register)
    if no_format:
        print(change)
        return
    format_change(change)

if __name__ == '__main__':
    nb_1euro = 15
    nb_2euros = 4
    nb_5euros = 4
    nb_10euros = 10
    nb_20euros = 5
    nb_50euros = 4

    main(
        asked = 12, 
        paid = 50, 
        cash_register = {
            50: nb_50euros,
            20: nb_20euros,
            10: nb_10euros,
            5: nb_5euros,
            2: nb_2euros,
            1: nb_1euro
        }
    )