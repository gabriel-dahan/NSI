"""
Fonction recherche_max(tab)
    max <-- tab[0]
    i <-- 0
    Tant que taille(tab)-i > 0
        Si tab[i] > max
            max <-- tab[i]
        Fin Si
        i <-- i + 1
    Fin Tant que
    retourner max
"""

def recherche_max(tab):
    _max = tab[0]
    i = 0
    while len(tab) - i > 0:
        if tab[i] > _max:
            _max = tab[i]
        i += 1
    return _max

print(recherche_max([7, 1, 2, 6, 3, 4, 5]))