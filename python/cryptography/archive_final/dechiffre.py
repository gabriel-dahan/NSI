
def dechiffrer_monoalph(permut):
    texte=input("Entrer le texte chiffré : ").lower()
    dechif="".join([chr(permut.index(lettre)+97) for lettre in texte])
    return dechif.replace(chr(permut.index(' ')+97),' ')

if __name__ == '__main__':
    dechif = dechiffrer_monoalph(['m','z','x','t','g','o','j','q','y','n','w','d','p','r','h','s','u','v','b','a','c','k','f','e','l','i',' '])
    print(dechif)