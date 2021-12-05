## Explication des fonctions
### Clear (`None`)
 - _Cette fonction permet le nettoyage de la console à chaque affichage de la grille de jeu :_

Importation du module `os`, permettant dans ce cas d'executer la commande 'clear' ou 'cls' en fonction du système d'exploitation de la machine sur laquelle le code est executé ('cls' si windows sinon 'clear').
### Init Array (`list`)
 - _Cette fonction crée la grille du jeu et la renvoie :_ 

 Tableau de 6 x 7 élements (Liste à 2 dimensions avec 7 lignes de 6 élements).
### Ask Player (`int`)
 - _Cette fonction demande à un des deux joueurs sur quelle colonne il veut placer son pion :_

Vérifie que la colonne demandée est bien inférieure ou égale à 7 (il y a 7 colonnes dans un puissance 4).
Renvoie le numéro de la colonne demandée.

__Remarque__ : `players_repr` est un tuple de 3 strings servant à l'affichage des différents symboles dans la grille du jeu (les caractères utilisés pour une case vide, pour une case occupée par le joueur 1 ou 2). Dans le `input()`, cette variable est utilisée pour afficher le symbole du joueur qui doit jouer en fonction du numéro de ce joueur. Par exemple, si c'est au joueur 2 de placer un pion, `players_repr[2]` sera exécuté.
### Update Grid (`list`)
 - _Cette fonction modifie la grille du jeu en ajoutant un nouveau pion placé par un des deux joueurs puis la renvoie :_

Appel de la fonction `ask_player` renvoyant le numéro de la colonne demandée par le joueur, numéro auquel on soustrait 1 (car l'élement n° i d'une liste se trouve toujours à l'index i-1).
Puis on rentre dans une boucle demandant au joueur de rentrer une colonnne tant que celle qu'il a choisi n'est pas libre.
On rentre ensuite dans une nouvelle boucle qui itère (=va) cette fois de `i=1` à `i=6` (`i=7-1`) et qui a chaque nombre i prend son contraire (-i), permettant de commencer par la fin de la colonne pour monter jusqu'au début et ainsi pouvoir vérifier au fur et à mesure si les cases sont occupées. Avec cette méthode, on voit facilement quelle case n'est pas occupée et par conséquent la plus basse pouvant accueillir un nouveau joueur.
### Format Grid (`str`)
 - _Cette fonction formate la grille du jeu sous forme de string pour être affichée dans le shell (la console) :_

Création du empty string (de la chaîne de caractères vide) `formated` qui va contenir la grille formatée.
Ensuite, on entre dans une boucle qui, pour chaque valeur de i entre 0 à 5 (pour chaque ligne), va ajouter à la variable `formated` un string contenant la concaténation du `join()` de chaque élement (= Case vide, J1 ou J2) de la ligne i de la grille et d'une ligne de séparation.

__Remarque__ : `join` est une méthode s'applicant sur un string (une chaîne de caractères) et prenant en paramètre une liste. Elle permet la concaténation de tous les termes de cette liste avec comme élément de séparation le string sur lequel la méthode à été utilisée.
Exemple : 
```py
'-'.join(['A', 'B', 'C', 'D', 'E'])
# --> "A-B-C-D-E"
```
### Check In/Check (`int`)
 - _La fonction `check_in()` va vérifier, dans une liste simple, si il y a une suite de 4 élements successifs, et retournera l'élement qui est présent 4 fois de suite (0, 1, ou 2). Si aucun élement n'est présent 4 fois de suite, 0 sera alors retourné._
 - _La fonction `check()`, à l'aide de la fonction `check_in()`, va vérifier pour chaque colonne, chaque ligne et chaque diagonale de la grille si une suite de 4 '1' ou de 4 '2' est présente, puis retournera le gagnant (1 ou 2) ou 0 si il n'y a pas de gagnant._
### End Game (`None`)
 - _Cette fonction permet d'afficher un message en précisant le joueur ayant gagné la partie._
### Main (`None`)
 - _Cette fonction gère le fonctionnement général du programme, elle contient la boucle du jeu et appelle les fonctions principales._

Compteur `i` initialité à 0, création de la grille de jeu (`arr`). Lancement de la boucle de jeu qui à chaque tour de boucle va incrémenter `i` puis assigner 1 ou 2 à la variable `player` en fonction de la parité de `i`.
Varible `winner` à laquelle on assigne à chaque tour de boucle la valeur du potentiel gagnant (0, 1 ou 2). Si le gagnant est différent de 0, c'est qu'il y a un gagnant et donc que la partie est finie, sinon si la grille est remplie mais qu'il n'y a pas de gagnant, alors la partie se finit avec une égalité.
Si il n'y a aucun gagnant et que la grille n'est pas pleine, alors on met à jour la grille avec la fonction `update_grid` (qui va demander au joueur de placer un pion sur une colonne etc...), puis on `clear` le shell et on affiche la grille mise à jour.