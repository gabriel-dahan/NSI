def max(*args) -> int:
    """ Returns the greater number in the list of arguments """
    return sorted(args)[-1]

def isleap(year: int) -> bool:
    """ Returns whether a year is leap year or not """
    return year % 4 == 0 and year % 10 != 0 or year % 400 == 0

def sum_to(n, recur: bool = False) -> int:
    """ Returns (1 + 2 + ... + n) """
    if recur:
        return 1 if n == 1 else sum_to(n - 1) + n
    return n * (n + 1) // 2