from typing import List

### EX 1 ###
""" Cet algorithme assigne aux 6 premières valeurs d'une liste les carrés de 0 à 5. """

### EX 2 ###
""" Cet algorithme, en partant de 1, génère la suite des 7 premiers entiers impairs par recursion. """

### EX 3 ###
def ask_grades(n: int) -> list:
    """ Ask the user to enter a list of x grades. """
    grades, coeff = [], []
    for i in range(1, n + 1):
        grade = input(f'Entrez la note {i} et son coefficient (séparés par un \':\') : ').split(':')
        grades.append(float(grade[0]))
        coeff.append(float(grade[1]))
    return grades, coeff

def mean_of(n: int) -> float:
    """ Returns the mean of the values from a list of x ints. """
    grades, coeff = ask_grades(n)
    s = sum(grades[i] * coeff[i] for i in range(len(grades)))
    return s / sum(coeff)

### EX 4 ###
def ask_ints():
    """ Prints the amout of positive and negative numbers in a list of x values. """
    iters = int(input('Entrez le nombre d\'entiers que vous comptez saisir : '))
    assert iters > 0, 'Iterations number must be positive.'
    l = [int(input(f'#{i} : ')) for i in range(1, iters + 1)]
    positive = sum(val >= 0 for val in l)
    print(f'Positive : {positive}\nNegative : {len(l) - positive}')

### EX 5 ###
def sum_of(l1: list, l2: list) -> list:
    """ Returns a sum of the index of length-equal lists. """
    assert len(l1) == len(l2), 'l1 length must be equal to l2 length'
    return [l1[i] + l2[i] for i in range(len(l1))]

### EX 6 ###
def schtroumpf(l1: list, l2: list) -> list:
    """ Returns the 'schtroumpf' of 2 lists. """
    s = 0
    for i in l1:
        for y in l2:
            s += i * y
    return s

if __name__ == '__main__':
    print(mean_of(10))