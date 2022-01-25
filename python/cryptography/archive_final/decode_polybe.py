from pathlib import Path
from typing import Union
from code_cesar import get_text_if_path

values_array = [
    'aàâbcç',
    'deéèêf',
    'ghiîjk',
    'lmnoôp',
    'qrstuù',
    'ûvwxyz'
]

def dechiffrer_polybe(string: Union[str, Path]):
    string = get_text_if_path(string)
    result = ''
    splited_str = string.split()
    for word in splited_str:
        for i, y in zip(word[0::2], word[1::2]):
            result += values_array[int(i) - 1][int(y) - 1]
        result += ' '
    return result

if __name__ == '__main__':
    c = dechiffrer_polybe(Path('./files/tcrypto2.txt'))
    print(c)