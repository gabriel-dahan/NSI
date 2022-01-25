from pathlib import Path
from typing import Union

def get_text_if_path(text: Union[str, Path]) -> str:
    """ Renvoie le texte présent dans un fichier si le texte donné est un lien vers ce fichier. """
    if isinstance(text, str):
        return text
    elif isinstance(text, Path):
        path = text.absolute()
        with open(path) as f:
            text = f.readlines()
        return ''.join(text)

def encrypt_ceasar(text: Union[str, Path], depth: int = 3) -> str:
    """ Chiffre un texte en utilisant le chiffrement de César. """
    text = get_text_if_path(text)
    result = ''
    for i in range(len(text)):  
        char = text[i]
        if ord(char) not in {*range(65, 91), *range(97, 123)}:
            result += char
            continue
        if char.isupper():  
            result += chr((ord(char) + depth - 64) % 26 + 65)
        else:  
            result += chr((ord(char) + depth - 96) % 26 + 97)
    return result

def decrypt_ceasar(text: Union[str, Path], depth: int = 3) -> str:
    """ Déchiffre un texte en utilisant le chiffrement de César. """
    depth = 24 - depth
    return encrypt_ceasar(text, depth)

if __name__ == '__main__':
    text = "IVEUVQ MFLJ TV JFZI RL TRWV UV CR XRIV CV JZXEV UV IVTFEERZJJRETV JVIR LE GRIRGCLZV SCVL"
    for key in range(2, 27):
        uncrypted = decrypt_ceasar(text, key)
        print(key, uncrypted)