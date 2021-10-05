def ex1() -> None:
    """ Prints your initials """
    name, fname = input('Enter your name : '), input('Enter your family name : ')
    print(f'Initals : {name[0]}.{fname[0]}.')

def ex2(count: bool = False) -> bool:
    """ Returns wether the letter 'e' exists in a string or not """
    string = input('Entrez un texte : ')
    if count:
        return string.count('e')
    return True if 'e' in string else False

def ex3(text: str) -> str:
    """ Returns the inverted text """
    return text[::-1]

def ex4(text: str) -> bool:
    """ Returns wether the number is palyndrom or not """
    return True if text[::-1] == text else False

def ex5(base10: int) -> int:
    """ Returns the base 2 of a base 10 number """
    return int(bin(base10)[2:])

def ex6(base2: int) -> int:
    """ Returns the base 10 of a base 2 number """
    digits = str(base2)    
    final = 0
    for i, digit in enumerate(digits):
        final += int(digit) * 2 ** (len(digits) - (i + 1))
    return final

if __name__ == '__main__':
    print(ex2(count = True))