def main():
    nb_1euro = 15
    nb_5euro = 4
    nb_10euro = 12
    nb_20euro = 5
    nb_50euro = 4
    prix = int(input("Entrez valeur à payer :" ))
    montant = int(input("Entrer l'argent que vous souhaitez donner à la caisse : "))
    if prix<=montant:
        rendu = montant - prix
        p_b = [50,20,10,5,1]
        while(rendu>0):
            print(rendu)
            while rendu>50 :
                rendu = rendu - 50
                nb_50euro -= 1
            while rendu>20 :
                rendu = rendu - 20
                nb_20euro -= 1
            while rendu>10 :
                rendu = rendu - 10
                nb_10euro -= 1
            while rendu>5 :
                rendu = rendu - 5
                nb_5euro -= 1
            while rendu>=1 :
                rendu = rendu - 1
                nb_1euro -= 1
        # p_b.append(a)
        for k in range (len(rendu)):
            print(f'La caisse vous rend {p_b[k]}')
    else:
        print("Vous n'avez pas assez d'argent")
    return rendu

print(main())