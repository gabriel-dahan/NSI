from typing import List

def get_index_of_max(l: List[list]):
    temp = 0
    for i in range(len(l) - 1):
        if l[i][0] < l[i + 1][0]:
            temp = i + 1
    return temp

def change_order_of(l: List[list]):
    for elem in l:
        elem[1] = not elem[1]
    return list(reversed(l))

def change_order_to(index: int, _list: List[list]):
    for i in range(index + 1):
        _list[i][1] = not _list[i][1]
    reversed_to_index = list(reversed([_list[i] for i in range(index)]))
    for i in range(index, len(_list) - 1):
        reversed_to_index.append(_list[i])
    return reversed_to_index

if __name__ == '__main__':
    crepes = [
        [5, True],
        [8, True],
        [1, False]
    ]
    crepes = change_order_to(get_index_of_max(crepes), crepes)
    print(crepes)



i = crepes.index(max(crepes))
temp = crepes[-1]
crepes[-1] = crepes[i]
crepes[i] = temp