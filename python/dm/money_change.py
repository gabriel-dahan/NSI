def money_change(asked: int, paid: int, cash_register: dict) -> dict:
    """ Returns a dict of the change the cashier must return. """
    assert paid >= asked, 'You don\'t have enough money to pay.'
    rest = paid - asked
    # total_cash = sum(_type * cash_register[_type] for _type in cash_register)
    total_cash = []
    for _type in cash_register:
        total_cash.append(_type * cash_register[_type])
    total_cash = sum(total_cash)
    assert total_cash >= rest, 'The cash register does not contain enough money to return.'
    change = {
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        2: 0,
        1: 0
    }
    for _type in change: # For each type of change from 50€ to 1€.
        # While the cash register contains enough money and the rest of the money to be returned is greater than the type of change to be returned.
        while cash_register[_type] >= 1 and rest >= _type:
            cash_register[_type] -= 1
            change[_type] += 1
            rest -= _type
    return change

def format_change(currencies: dict) -> None:
    """ Prints the change to be returned by the cashier. """
    # change = ''.join([f"\n - {currency} x {_type}$" for _type, currency in currencies.items() if currency > 0])
    formated_change = ''
    for _type, change in currencies.items():
        if not change > 0:
            continue
        formated_change += f'\n - {change} x {_type}$'
    print(f'Change to be returned : {formated_change}')

def main(cash_register: dict, no_format: bool = False) -> None:
    """ Launches the program. """
    requested = int(input("How much money is requested by the cashier ? "))
    paid = int(input("How much money did you pay ? "))
    print()
    change = money_change(requested, paid, cash_register)
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
        {
            50: nb_50euros,
            20: nb_20euros,
            10: nb_10euros,
            5: nb_5euros,
            2: nb_20euros,
            1: nb_1euro
        }
    )