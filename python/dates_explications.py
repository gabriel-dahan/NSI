"""
Exercices 'nombre de jours entre deux dates':
    - Ecrire une fonction bissextile(a) qui renvoie un booléen indiquant si l'année a est une année bissextile.
    (Rappel : On dit qu'une année est bissextile si elle est multiple de 4 mais pas de 10 ou multiple de 400)
    - Ecrire une fonction nbjoursannee(a) qui renvoie le nombre de jours de l'année a, en utilisant la fonction bissextile.
    - Ecrire une fonction nbjoursmois(a, m) qui renvoie le nombre de jours dans le mois m de l'année a, en utilisant la fonction bissextile.
    - En utilisant les fonctions nbjoursannee et nbjoursmois, écrire une fonction nbjours(j1, m1, a1, j2, m2, a2) qui renvoie le nombre de jours compris entre deux dates données :
    la date j1/m1/a1 et la date j2/m2/a2.
"""

# Renvoie si une année est bissextile ou non
def bissextile(a):
    if a % 4 == 0 and not a % 10 == 0 or a % 400 == 0: # Si l'année est multiple de 4 ...
        return True # ... alors on renvoie True pour signifier que l'année est bissextile.
    return False # Sinon on renvoie False signifiant que l'année n'est pas bissextile

# Renvoie le nombre de jours d'une année
def nbjoursannee(a):
    if bissextile(a): # Si l'année est bissextile ...
        return 366 # ... alors son nombre de jours est égal à 366 (29 jours en février à la place de 28)
    return 365 # Sinon, l'année n'est pas bissextile et à donc 365 jours.

# Renvoie le nombre de jours d'un mois en fonction de son année
def nbjoursmois(a, m): 
    if bissextile(a) and m == 2: # Si l'année est bissextile et que le mois choisi est 2 (février) ...
        return 29 # ... alors on renvoie 29
    if m == 2: # Sinon si le mois choisi est 2 mais que l'année n'est pas bissextile ...
        return 28 # ... alors on renvoie 28 
    if m in (1, 3, 5, 7, 8, 10, 12): # Si le mois choisi est 1, 3, 5, 7, 8, 10 ou 12 ...
        return 31 # ... alors on renvoie 31 (janvier, mars, mai, ... ont 31 jours)
    else: # Sinon ...
        return 30 # ... on renvoie 30

# Renvoie le nombre de jours passés depuis le début de l'année de la date entrée jusqu'à la date
def jours_passes(j, m, a):
    jours = 0
    for mois in range(1, m): # Pour chaque mois entre 1 et m - 1 (m étant le mois entré) ...
        jours += nbjoursmois(a, mois) # ... on ajoute le nombre de jours de ce mois à la variable jours initialisée plus haut.
    jours += j # Après la boucle, on ajoute le nombre de jours de la date entrés.
    return jours # On renvoie le nombre de jours final

# Renvoie le nombre de jours restants entre la date rentrée et la fin de l'année de la date (l'inverse de la fonction au dessus)
def jours_restants(j, m, a):
    jours = 0
    for mois in range(m + 1, 13): # Pour chaque mois entre m + 1 (9 si m = 8 par exemple) et 12 (13 - 1) ...
        jours += nbjoursmois(a, mois) # ... on ajoute le nombre de jours de ce mois à la variable jours initialisée plus haut.
    jours += nbjoursmois(a, m) - j # Après la boucle, on ajoute aux jours le nombre de jours du mois de l'année entrée moins le nombre de jours entrés. 
    # Exemple : si j = 12, m = 3, a = 2021 -> nbjoursmois(2021, 3) - 12 = 31 - 12 = 19 donc jours += 19
    return jours # On renvoie le nombre de jours final

# Enfin, la fonction qui renvoie le nombre de jours entre les deux dates
def nbjours(j1, m1, a1, j2, m2, a2):
    if a1 == a2: # Si l'année de la première date est égale à l'année de la deuxième (Par exemple si les deux dates sont en 2021)
        jours = jours_passes(j2, m2, a2) - jours_passes(j1, m1, a1) # ... alors le nombre de jours entre les deux dates sera juste égal à la différence entre 
        # le nombre de jours passés dans la deuxième date par le nombre de jours passés dans la première
    else: # Sinon (si il y a une ou plusieurs années qui séparent les dates)
        jours = 0 # On initalise une variable jours à 0
        for a in range(a1, a2 + 1): # Pour chaque année entre l'année de la date 1 et l'année de la date 2 
            if a == a1: # Si l'année est égale à celle de la première date ...
                jours += jours_restants(j1, m1, a1) # ... alors on ajoute le nombre de jours restants avant la fin de l'année de cette date
                continue # ... on lance le prochain tour de boucle
            elif a == a2: # Si l'année est égale à celle de la deuxième date ...
                jours += jours_passes(j2, m2, a2) # ... alors on ajoute le nombre de jours passés depuis le débuts de l'année de cette date
                continue # ... on lance le prochain tour de boucle
            jours += nbjoursannee(a) # Si l'année n'est ni celle de la première date ni celle de la deuxième alors on ajoute le nombre de jours de cette année (365 ou 366)
    return jours # On renvoie (enfin) le nombre de jours final entre les deux dates.

print(nbjours(30, 7, 2021, 18, 8, 2021))