from pathlib import Path
from typing import Union

from code_cesar import encrypt_ceasar, decrypt_ceasar

class Vigenere(object):

    def __init__(self, string: Union[Path, str], key: str):
        if isinstance(string, str):
            self.string = string
        elif isinstance(string, Path):
            path = string.absolute()
            with open(path) as f:
                string = f.readlines()
            self.string = ''.join(string)
        self.alph = [chr(_ord) for _ord in range(97, 123)]
        self.key = key
        while len(self.key) <= len(self.string):
            self.key += key

    def encrypt(self) -> str:
        final = ''
        i = 0
        for char in self.string:
            if char not in self.alph:
                final += char
                continue
            key_i = self.alph.index(self.key[i])
            final += encrypt_ceasar(char, key_i - 1)
            i += 1
        return final

if __name__ == '__main__':
    vig = Vigenere('un exemple de chiffrement', 'python').encrypt() # Chiffrement
    print(vig)