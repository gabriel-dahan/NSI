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

def partie_simple():
    j1 = input('Pierre, Feuille ou Ciseaux (p, f ou c) ? ')
    while not j1 or j1 not in 'pfc':
        j1 = input('p, f ou c : ')
    j2 = random.choice('pfc')
    if j1 == j2:
        winner = 0
    elif (j1 == 'p' and j2 == 'c') \
        or (j1 == 'f' and j2 == 'p') \
        or (j1 == 'c' and j2 == 'f'):
        winner = 1
    else:
        winner = 2
    return winner

if __name__ == '__main__':
    score_j1 = 0
    score_j2 = 0
    for _ in range(10):
        if score_j1 == 5 or score_j2 == 5:
            break
        winner = partie_simple()
        if winner == 0:
            print(f'Match nul.')
        elif winner == 1:
            print(f'Vous avez gagné !')
            score_j1 += 1
        else:
            print(f'L\'ordinateur à gagné.')
            score_j2 += 1
        print(f'\n--> Manches gagnées par J1 : {score_j1}/10')
        print(f'--> Manches gagnées par J2 : {score_j2}/10')
    if score_j1 > score_j2:
        print(f'\n### J1 gagne la partie avec {score_j1} points contre {score_j2} ! ###')
    elif score_j1 == score_j2:
        print(f'\n### Match nul, J1 a autant de points que J2. ###')
    else:
        print(f'\n### J2 gagne la partie avec {score_j2} points contre {score_j1} ! ###')