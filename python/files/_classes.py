import json
from typing import List, Union


class TXTFile(object):

    def __init__(self, path: str):
        self.path = path

    def read(self, string: bool = False):
        with open(self.path) as f:
            r = f.readlines()
            if string: r = '\n'.join(r)
        return r

    def write(self, new: Union[List[str], str], add: bool = True, new_line: bool = True):
        is_list = isinstance(new, list)
        if new_line:
            new = ['\n' + line for line in new] if is_list else '\n' + new
        f = open(self.path, 'a') if add else open(self.path, 'w')
        f.writelines(new) if is_list else f.write(new)
        f.close()

class JSONFile(object):

    def __init__(self, path: str):
        self.path = path

    def read(self):
        data = []
        with open(self.path, 'r') as f:
            data = [json.loads(l.replace('}]}"},', '}]}"}')) for l in f.readlines()]
        return data

    def write(self):
        pass

class XMLFile(object):

    def __init__(self, path: str):
        self.path = path

    def read(self):
        pass

    def write(self):
        pass

if __name__ == '__main__':
    """f = TXTFile('./testing_files/file.txt')
    for _ in range(100):
        import random as r
        f.write(f'{r.randint(1, 100)}')"""
    f = JSONFile('./testing_files/file.json')
    print(f.read())