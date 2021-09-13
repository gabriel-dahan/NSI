def max(*args) -> int:
    """ Returns the greater number in the list of arguments """
    return sorted(args)[:-1]

def isleap(year: int) -> bool:
    """ Returns whether a year is leap year or not """
    return True if year % 4 == 0 else False

def sum_to(n, recur: bool = False) -> int:
    """ Returns (1 + 2 + ... + n) """
    if recur:
        if n == 1:
            return 1
        return sum_to(n - 1) + n
    return n * (n + 1) // 2