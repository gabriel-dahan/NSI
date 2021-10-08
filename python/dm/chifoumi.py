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

def partie_simple() -> Literal[0, 1, 2]:
    """ Renvoie un entier spécifiant le résultat de la partie. """
    j1 = input('Pierre, Feuille ou Ciseaux (p, f ou c) ? ')
    while j1 not in 'pfc':
        j1 = input('p, f ou c : ')
    j2 = random.choice('pfc')
    if j1 == j2:
        gagnant = 0
    elif (j1 == 'p' and j2 == 'c') \
        or (j1 == 'f' and j2 == 'p') \
        or (j1 == 'c' and j2 == 'f'):
        gagnant = 1
    else:
        gagnant = 2
    return gagnant

def pfc(m: int) -> None:
    """ Joue et affiche les résultats d'une partie de m manches. """
    assert m >= 1, 'Une partie doit compter au moins 1 manche.'
    score_j1 = 0
    score_j2 = 0
    max_score = m / 2
    i = 0
    while i < m and (score_j1 < max_score and score_j2 < max_score):
        gagnant = partie_simple()
        if gagnant == 0:
            print('Match nul.')
        elif gagnant == 1:
            print('J1 a gagné la manche.')
            score_j1 += 1
        else:
            print('J2 a gagné la manche.')
            score_j2 += 1
        print(f'\n--> Manches gagnées par J1 : {score_j1}/{max_score}')
        print(f'--> Manches gagnées par J2 : {score_j2}/{max_score}')
        i += 1
    if score_j1 > score_j2:
        print(f'\n### J1 gagne la partie avec {score_j1} points contre {score_j2} ! ###')
    elif score_j1 == score_j2:
        print(f'\n### Match nul, J1 a autant de points que J2. ###')
    else:
        print(f'\n### J2 gagne la partie avec {score_j2} points contre {score_j1} ! ###')

if __name__ == '__main__':
    pfc()