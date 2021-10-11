from typing import Tuple

### QUESTION 1 ###

def temps_secondes(time: Tuple[int]) -> int:
    """ Returns how many seconds are in (hh, mm, ss). """
    assert time[0] < 24 and time[1] < 60 and time[2] < 60, 'Format must be (hh, mm, ss) with hh < 24, mm < 60, ss < 60.'
    return time[0] * 3600 + time[1] * 60 + time[2]

### QUESTION 2 ###

def temps_h_mn_s(seconds: int) -> Tuple[int]:
    """ Returns how many hours, minutes, seconds are in x seconds. """
    minsec = divmod(seconds, 60)
    hoursmin = (0, 0)
    if minsec[0] > 59:
        hoursmin = divmod(minsec[0], 60)
    return (hoursmin[0], hoursmin[1] if minsec[0] > 59 else minsec[0], minsec[1])

donnees = (
    ('Paul', (2, 3, 45)), 
    ('Sandrine', (1, 10, 5)), 
    ('Jacques', (2, 0, 15)),
    ('Marylline', (7, 10, 56)),
    ('Sacha', (0, 3, 2))
)

### QUESTION 3 ###

def temps_en_s(data: Tuple[Tuple[str, int]]) -> Tuple[Tuple[str, int]]:
    new_data = []
    for elem in data:
        new_data.append((elem[0], temps_secondes(elem[1])))
    return tuple(new_data)

### QUESTION 4 ###

# 1)
def liste_temps(data: Tuple[Tuple[str, int]]) -> Tuple[Tuple[str, int]]:
    return tuple(temps_secondes(elem[1]) for elem in data)

# 2)
def val_min(_tuple: Tuple[int]) -> Tuple[int]:
    temp = (0, _tuple[0])
    for i, val in enumerate(_tuple):
        if not val < temp[1]:
            continue
        temp = (val, i)
    return temp

### QUESTION 5 ###

def gagnant(data: Tuple[Tuple[str, int]]) -> str:
    data = temps_en_s(data)
    temp = data[0]
    for elem in data:
        if not elem[1] < temp[1]:
            continue
        temp = elem
    return temp

if __name__ == '__main__':
    print(gagnant(donnees))