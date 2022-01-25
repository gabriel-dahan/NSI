import matplotlib.pyplot as plt

def frequence(texte):
    """ Renvoie la fréquence des 26 lettres de l'alphabet dans un texte. """
    texte=texte.upper()
    liste=[[chr(text),0] for text in range (65,91)]
    for i in range(26):
        liste[i][1]=round(texte.count(liste[i][0])/len(texte.replace(' ', '').replace("'", ''))*100,3)
    return liste

def afficher_plot():
    file=open("./files/tcrypto3.txt","r")
    texte=file.read()

    lettre=list(range(26))
    lcrypte=[x+0.3 for x in lettre]
    alpha="abcdefghijklmnopqrstuvwxyz"
    F=[8.15,0.97,3.15,3.73,17.39,1.12,0.97,0.85,7.31,0.45,0.02,5.69,2.87,7.12,5.28,2.80,1.21,6.64,8.14,7.22,6.38,1.64,0.03,0.41,0.28,0.15]
    liste=frequence(texte)
    freq=[liste[i][1] for i in range(len(liste))]
    plt.xticks(lettre, list(alpha))
    plt.bar(lettre,F,color="red")
    plt.bar(lcrypte,freq,color="green")
    plt.grid(True)
    plt.show

if __name__ == '__main__':
    afficher_plot()