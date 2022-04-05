from pathlib import Path
from typing import Any, Dict, List, Union

class csv(object):

    def __init__(self, file: Union[str, Path]):
        self.file = file.absolute() if isinstance(file, Path) else file
        self.descriptors = self.read()[0]

    def _represents_int(self, nb: Any):
        try:
            int(nb)
            return True
        except ValueError:
            return False

    def read(self, delimiter: str = ',') -> List[str]:
        with open(self.file) as fp:
            lines = fp.readlines()
        list_lines = [line.split(delimiter) for line in lines]
        for line in list_lines:
            line[-1] = line[-1].replace('\n', '')
        return list_lines

    def dict_read(self, delimiter: str = ',') -> Dict[str, List[Any]]:
        assert self.descriptors, 'The csv file must contain descriptors to convert to dict.'
        lines = self.read(delimiter)
        return {
            lines[0][i]: [line[i] for line in lines[1:]]
            for i in range(len(self.descriptors))
        }

    def writelines(self, lines: List[str], delimiter: str = ',', column: int = -1, unique: bool = False):
        with open(self.file, 'a+') as fp:
            if column == -1:
                old = self.read()
                for line in lines:
                    if unique and line in old:
                        continue
                    for i in range(len(line)):
                        line[i] = str(line[i]) if self._represents_int(line[i]) else line[i]
                    fp.write(delimiter.join(line) + '\n')
                return
        

# La fonction DictReader() du module csv renvoie un objet itérable.
# Chaque élément de cet objet est une liste de tuples.

if __name__ == '__main__':
    csvf = csv('./testing_files/notes_eleves.csv')
    print(csvf.dict_read())