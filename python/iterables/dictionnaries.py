import sys
import csv

def exo1():
    d = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}
    d['Jacque'] = 'Jacques'
    print(f' - Clés : {list(d.keys())}\n - Valeurs : {list(d.values())}\n - Paires K/V : {list(d.items())}')
    print(f"{d['prenom']} {d['nom']} a {d['age']} ans")

def annuaire():
    dic = {}
    running = True
    while running:
        choice = int(input(
            " [0] Exit\n [1] Write in the repository\n [2] Search in the repository\n - Your choice (int) ? "
        ))
        if choice == 0:
            running = False
            continue
        elif choice == 1:
            running_nested = True
            while running_nested:
                name = input("\n - Name : ")
                if name in ('0', '__exit__'):
                    running_nested = False
                    continue
                phone = input(" - Phone number : ")
                dic[name.lower().capitalize()] = phone
                print(dic)
            continue
        elif choice == 2:
            running_nested = True
            while running_nested:
                name = input("\n - Search a name : ").lower().capitalize()
                if name in ('0', '__exit__'):
                    running_nested = False
                    continue
                if name not in dic:
                    print(f'Name {name} not found in phone repository.')
                    continue
                print(f"{name}'s phone number : {dic[name]}")
            continue

def exo3_tp_a(word: str):
    ## TP a)
    values_scrabble = {
        10: 'kwxyz',
        8: 'jq',
        4: 'fhv',
        3: 'bcp',
        2: 'dmg'
    }
    s = 0
    for char in word:
        found = 0
        for k, v in values_scrabble.items():
            if char in v:
                found = k
        s += found or 1

    print(s)
    
## TP b)
values_scrabble = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 
    'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 10, 'l': 1, 
    'm': 2, 'n': 1, 'o': 1, 'p': 3, 'q': 8, 'r': 1, 
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 10, 'x': 10, 
    'y': 10, 'z': 10
}

def wordval(word: str):
    return sum(values_scrabble[char] for char in word)

m1, m2, m3 = 'arpentes', 'paternes', 'trepanes'

def words_value():
    v1, v2, v3 = (m1, wordval(m1)), (m2, wordval(m2)), (m3, wordval(m3))
    return v1, v2, v3

def wordval_triple(word: str):
    return sum(
        values_scrabble[char] * 3 if i == 3 else values_scrabble[char]
        for i, char in enumerate(word)
    )

def triple_on_4th():
    for word in (m1, m2, m3):
        print(wordval_triple(word))

if __name__ == '__main__':
    try:
        annuaire()
    except KeyboardInterrupt:
        sys.exit(1)