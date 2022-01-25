from matplotlib.pyplot import plot, show, legend
from timeit import default_timer

def linear_search(x, a):
    """La fonction linear_search(x,a) permet de rechercher une valeur x dans la liste a.
    Si la valeur n'est pas trouvée, la fonction renvoie -1."""
    longueur = len(a)
    index = -1
    for i in range(longueur):
        if x == a[i]:
            index = i
    return index   
    
    
def binary_search(x, a):
    """La fonction binary_search(x,a) permet de rechercher une valeur x dans la liste a triée.
C'est une recherche par dichotomie.Si la valeur n'est pas trouvée, la fonction renvoie -1."""
    longueur = len(a)
    debut = 0
    fin = longueur-1
    while debut<=fin:
        milieu=(debut+fin)//2
        if a[milieu]==x:
            return milieu
        elif a[milieu]<x:
            debut=milieu+1
        elif a[milieu]>x:
            fin=milieu-1
    return -1
    

"""
Pour mesurer le temps de calcul d'une fonction, on utilise la fonction default_timer()
qui retourne une variable de type float représente le temps à un instant t.
Avant d'exécuter la fonction, on initialise start avec le temps initial.
Lorsque la fonction a été exécutée, on initialise end avec le temps final.
end-start permet de calculer le temps d'exécution de la fonction.
Ce temps est ensuite ajouté à une liste : times_linear ou times_binary.
"""

lengths = [i for i in range(1,1001)]
def get_times(length: int, func: callable, x: int):
    l = []
    for n in length:
        a = list(range(n))
        start = default_timer()
        func(x, a)
        end = default_timer()
        l.append(end - start)
    return l

times_linear = get_times(lengths, linear_search, -1)
times_binary = get_times(lengths, binary_search, -1)

plot(lengths, times_linear, label="linear")
plot(lengths, times_binary, label="binary")
legend()
show()