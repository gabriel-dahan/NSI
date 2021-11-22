from typing import Any

def equal_lines(l: list) -> bool:
    for i in l:
        assert len(l) == len(i)
    return all(sum(l[i]) == sum(l[i + 1]) for i in range(len(l) - 1))

def calc_column(l: list, c: int) -> int:
    for i in l:
        assert len(l) == len(i)
    return sum(i[c] for i in l)

def generate_rand_list() -> None:
    from random import randint
    l = [[randint(1, 9999) for _ in range(30)] for _ in range(30)]
    print(l)
    # print(max(l))
    temp = l[0][0]
    for i in l:
        for j in i:
            if not j > temp:
                continue
            temp = j
    print(f'\nMax : {temp}')


def binary_cross() -> list:
    l = [[1] * 100 for _ in range(100)]
    for i in range(100):
        l[i][i] = 0
    for j in range(100):
        l[j][99 - j] = 0
    return l

def zeros_array(lines: int, columns: int) -> list:
    return [[0] * columns for _ in range(lines)]

def frame_on(array: list, unit: Any = 1) -> list:
    for i in range(len(array[0])):
        array[0][i] = unit
        array[-1][i] = unit
    for line in array:
        line[0] = unit
        line[-1] = unit
    return array

def diagonalize(array: list, unit: Any = 1) -> list:
    assert len(array[0]) == len(array), 'The array must be squared.'
    for i in range(len(array)):
        array[i][i] = unit
    return array

def consecutive(array: list, start: int = 1) -> list:
    for i in range(len(array)):
        pass
    return array

if __name__ == '__main__':
    r = diagonalize(zeros_array(5, 5))
    print(r)