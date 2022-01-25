from code_cesar import encrypt_ceasar

alph = [chr(_ord) for _ord in range(97, 123)]
def chiffrer_vigenere(text: str, key: str):
    """ Chiffre un texte en utilisant le chiffrement de Vigenere. """
    final = ''
    while len(key) <= len(text):
        key += key
    i = 0
    for char in text:
        if char not in alph:
            final += char
            continue
        key_i = alph.index(key[i])
        final += encrypt_ceasar(char, key_i - 1)
        i += 1
    return final

if __name__ == '__main__':
    vig = chiffrer_vigenere('un exemple dechiffrement', 'python')
    print(vig)