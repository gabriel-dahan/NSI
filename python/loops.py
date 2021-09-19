from typing import List, Tuple
try:
    from .basics import isleap
except ImportError:
    from basics import isleap

def cooldown(a: int, b: int, wait_time: int = 1):
    """ Runs a cooldown from 'a' to 'b' (a > b) """
    import time
    assert a > b, '\'a\' must be greater than \'b\''
    for i in range(a, b - 1, -1):
        print(i)
        if wait_time < 1:
            continue
        time.sleep(wait_time)

def table(n: int, m: int = 10):
    """ Prints the 'n' table with 'm' multiples """
    for i in range(1, m + 1):
        print(f'{n} * {i} = {n * i}')

def tuples(a: int, b: int) -> List[Tuple[int]]:
    """ Returns from (0, 0) to (a - 1, b - 1) """
    l = []
    for x in range(0, a):
        for y in range(0, b):
            l.append((x, y))
    return l

def bank(capital: int = 10000, years: int = 5):
    """ Jean has a capital of 10000€ (by default). This capital os on a bank account with 2% annual benefit. Each year, he adds 400€ on it. 
    The function returns the capital of Jean in n-years."""
    l = []
    temp = capital
    for _ in range(1, years + 1):
        temp += temp * 0.02
        temp += 400
        l.append(temp)
    return l

def factorial(n: int):
    """ Returns the factorial of 'n' (1 * 2 * 3 * ... * n) """
    if n == 1:
        return 1
    return n * factorial(n - 1)

def year_days_nmb(year: int) -> int:
    """ Returns the amount of days in a year depending on if it's a leap year or not """
    if isleap(year):
        return 366
    return 365

def month_days_nmb(year, month):
    """ Returns the amount of days in a month of a year """
    assert 1 <= month <= 12, 'Mois non valide, (1-12)'

    if isleap(year) and month == 2:
        return 29
    if month == 2:
        return 28
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    else:
        return 30

def passed_days(date: str, separator: str = '/') -> int:
    """ Returns the number of passed days since the date's year started. """
    date = tuple(int(elem) for elem in date.split(separator))
    days = 0
    for month in range(1, date[1]):
        days += month_days_nmb(date[2], month)
    days += date[0]
    return days

def remaining_days(date: str, separator: str = '/') -> int:
    """ Returns the number of remaining days before the date's year end. """
    date = tuple(int(elem) for elem in date.split(separator))
    days = 0
    for month in range(date[1] + 1, 13):
        days += month_days_nmb(date[2], month)
    days += month_days_nmb(date[2], date[1]) - date[0]
    return days

def days_nmb(date1: str, date2: str, separator: str = '/') -> int:

    d1, d2 = tuple(int(elem) for elem in date1.split(separator)), tuple(int(elem) for elem in date2.split(separator))
    d1_month_days, d2_month_days =  month_days_nmb(d1[2], d1[1]), month_days_nmb(d2[2], d2[1])
    err = f'{date2} cannot be smaller than {date1}.'

    assert d2[2] >= d1[2], err
    if d2[2] == d1[2]:
        assert d2[1] >= d1[1], err
        if d2[1] == d1[1]:
            assert d2[0] >= d1[0], err
        days = passed_days(date2, separator) - passed_days(date1, separator)
    else:
        days = 0
        for year in range(d1[2], d2[2] + 1):
            if year == d1[2]:
                days += remaining_days(date1, separator)
                continue
            elif year == d2[2]:
                days += passed_days(date2, separator)
                continue
            days += year_days_nmb(year)
    return days

if __name__ == '__main__':
    print(days_nmb('30/07/2021', '18/09/2021'))