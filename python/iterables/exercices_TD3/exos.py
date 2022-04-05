import csv
from re import T
from typing import Dict, List, Tuple

### EXERCICE 4 ###

def check_common_key(key: str, dicts: List[Dict]) -> bool:
    return all(key in _dict for _dict in dicts)

def join_lists(obj: Tuple[list]) -> List:
    final = []
    for _list in obj:
        final += _list
    return final

def join(table1: List[Dict], table2: List[Dict], key: str) -> List[Dict]:
    from copy import deepcopy
    final = []
    for line1 in table1:
        for line2 in table2:
            if line1[key] == line2[key]:
                new_line = deepcopy(line1)
                for k in line2:
                    if k != key:
                        new_line[k] = line2[k]
                final.append(new_line)
    return final

def columns_union(*tables: List[Dict], key: str = None) -> List[Dict]:
    assert all(len(table) == len(tables[0]) for table in tables)
    if not key:
        common_descriptors = [[elem for elem in table[0].keys() if check_common_key(elem, join_lists(tables))] for table in tables]
        key = common_descriptors[0][0] if len(common_descriptors[0]) > 0 else None
        assert key, 'No common descriptors found.'
    common_columns = [[line[key] for line in table] for table in tables]
    assert all(common_columns[0] == column for column in common_columns), 'The common colums must be equal to each other.'
    jtable = [{} for _ in tables[0]]
    for i in range(len(tables)):
        for lcount, line in enumerate(tables[i]):
            for k, v in line.items():
                jtable[lcount][k] = v
    return jtable

def lines_union(*tables: List[Dict]) -> List[Dict]:
    assert all(table[0].keys() == tables[0][0].keys() for table in tables), 'Descriptors of each table must be the same.'
    final = []
    for table in tables:
        for line in table:
            final += [line]
    return final

def get_csv_tables(*tables: List[str]) -> List[List[Dict]]:
    final_tabs = []
    for table in tables:
        with open(table) as fp:
            final_tabs.append(list(csv.DictReader(fp)))
    return final_tabs

if __name__ == '__main__':
    ### EX 4 : ###
    oiseaux1, oiseaux2, couleur2 = get_csv_tables(
        './ex4/Oiseaux1.csv',
        './ex4/Oiseaux2.csv',
        './ex4/couleur2.csv'
    )
    oiseaux3 = lines_union(oiseaux1, oiseaux2)
    bilan_oiseaux = join(oiseaux3, couleur2, 'nom')
    print(f'{"-" * 20}\nbilan_oiseaux.csv : {bilan_oiseaux}\n{"-" * 20}\n')
    ##############

    ### EX 5 : ###
    membre, pret, livre = get_csv_tables(
        './ex5/membre.csv',
        './ex5/pret.csv',
        './ex5/livre.csv'
    )
    jointure1 = join(membre, pret, 'idm')
    jointure_finale = join(jointure1, livre, 'idl')
    print(f'{"-" * 20}\njointure_finale.csv : {jointure_finale}\n{"-" * 20}\n')
    ##############

