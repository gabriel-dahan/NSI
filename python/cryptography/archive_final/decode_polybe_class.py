from pathlib import Path
from typing import Any, List, Tuple, Union

class Polybe(object):

    def __init__(self, string: Union[Path, str]):
        if isinstance(string, str):
            self.string = string
        elif isinstance(string, Path):
            path = string.absolute()
            with open(path) as f:
                string = f.readlines()
            self.string = ''.join(string)
        self.values_array = [
            'aàâbcç',
            'deéèêf',
            'ghiîjk',
            'lmnoôp',
            'qrstuù',
            'ûvwxyz'
        ]
        self.values_ords = {*range(97, 123), 224, 226, 232, 233, 234, 238, 244, 249, 251}

    def _indexes_in_array(self, array: List[list], elem: Any) -> Tuple[int]:
        for i, line in enumerate(array):
            try:
                print(line, elem)
                y = line.index(elem)
                return (i, y)
            except ValueError:
                continue

    def encrypt(self) -> str:
        result = ''
        for char in self.string:
            if ord(char.lower()) not in self.values_ords:
                result += char
                continue
            i = self._indexes_in_array(self.values_array, char.lower())
            result += f'{i[0] + 1}{i[1] + 1}'
        return result

    def decrypt(self) -> str:
        result = ''
        splited_str = self.string.split()
        for word in splited_str:
            for i, y in zip(word[0::2], word[1::2]):
                result += self.values_array[int(i) - 1][int(y) - 1]
            result += ' '
        return result

if __name__ == '__main__':
    c = Polybe(Path('./files/tcrypto2.txt')).decrypt()
    print(c)