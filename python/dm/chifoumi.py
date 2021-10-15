# REPO FILE : https://github.com/gabriel-dahan/NSI/blob/main/python/dm/chifoumi.py
"""
    Pierre-Feuille-Ciseau (ou Chifoumi) est un jeu où 2 joueurs s'affrontent en choisissant chacun Pierre, Feuille ou Ciseaux.
    La Pierre écrase les Ciseaux, la Feuille enveloppe la Pierre, les Ciseaux découpent la Feuille.
    La gagnant de la manche remporte la un point.

    Représenter tous les cas possibles pour un duel en indiquant à chaque fois s'il y a un match nul ou un gagnant :
    - Si deux joueurs choisissent la même chose, il y a match nul.
    - Si un joueur choisi Pierre et l'autre Ciseaux, celui ayant pris Pierre gagne.
    - Si un joueur choisi Feuille et l'autre Pierre, celui ayant pris Feuille gagne.
    - Si un joueur choisi Ciseaux et l'autre Feuille, celui ayant pris Ciseaux gagne.
"""

import random
from typing import Literal

def simple_round() -> Literal[0, 1, 2]:
    """ Returns an integer specifying the result of a round of chifoumi. """
    p1 = input('Rock, Paper or Scissors (r, p or s) ? ')
    while p1 not in 'rps':
        p1 = input('r, p or s : ')
    p2 = random.choice('rps')
    if p1 == p2:
        winner = 0
    elif (p1 == 'r' and p2 == 's') \
        or (p1 == 'p' and p2 == 'r') \
        or (p1 == 's' and p2 == 'p'):
        winner = 1
    else:
        winner = 2
    return winner

def play_chifoumi(r: int = 10) -> None:
    """ Play and display the results of a game of r rounds. """
    assert r >= 1, 'A game must last at least 1 round.'
    p1_score = 0
    p2_score = 0
    max_score = r // 2 if r % 2 == 0 else (r // 2) + 1
    i = 0
    while i < r and (p1_score < max_score and p2_score < max_score):
        winner = simple_round()
        if winner == 0:
            print('Draw...')
        elif winner == 1:
            print('P1 won the round.')
            p1_score += 1
        else:
            print('P2 won the round.')
            p2_score += 1
        print(f'\n--> Rounds won by P1 : {p1_score}/{max_score}')
        print(f'--> Rounds won by P2 : {p2_score}/{max_score}')
        i += 1
    if p1_score > p2_score:
        print(f'\n### P1 wins the game with {p1_score} points against {p2_score} ! ###')
    elif p1_score == p2_score:
        print(f'\n### Draw, P1 has the same score as P2. ###')
    else:
        print(f'\n### P2 wins the game with {p2_score} points against {p1_score} ! ###')

if __name__ == '__main__':
    play_chifoumi()