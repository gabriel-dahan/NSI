import csv
from typing import Any, List

def _read_csv(file: str):
    with open(file, 'r') as fp:
        reader = csv.DictReader(fp, delimiter = ',')
        return [dict(line) for line in reader]

def get_all(descriptors: List[str], table: str) -> List[Any]:
    return [[obj[descriptor] for obj in _read_csv(table)] for descriptor in descriptors]

def get_all_gardians(table: str = 'files/BaseGardiens.csv'):
    return get_all(['NomAgent'], table)[0]
    # SELECTion des enregistrements en effectuant une projection.

def get_all_cities(table: str = 'files/BaseAgents.csv'):
    l = []
    for city in get_all(['VilleAgent'], table)[0]:
        if city not in l:
            l.append(city)
    return l
    # SELECTion des enregistrements en effectuant une projection.

def get_triplets():
    nocabine, nomalien = get_all(['NoCabine', 'NomAlien'], 'files/BaseAliens.csv')
    gardians = get_all_gardians()
    return [(i + 1, nomalien[i], gardians[i]) for i in range(len(nocabine))]

def get_aliens_from_allee(allee: int):
    allees = get_all(['NoAllee'], 'files/BaseCabines.csv')[0]
    aliens = get_all(['NomAlien'], 'files/BaseAliens.csv')[0]
    return [aliens[i] for i in range(1, len(aliens)) if int(allees[i]) == allee]

def get_aliens_from_city(city: str):
    gardians, cities = get_all(['NomAgent', 'VilleAgent'], 'files/BaseAgents.csv')
    triplets = get_triplets()
    gardians_from_city = [gardians[i] for i in range(len(gardians)) if cities[i] == city]
    return [elem[1] for elem in triplets if elem[2] in gardians_from_city]

def get_gardians_with(alien_masculin: bool = False, alien_eats: str = 'Bortsch'):
    genre = 'F' if not alien_masculin else 'M'
    aliens, genres = get_all(['NomAlien', 'Sexe'], 'files/BaseAliens.csv')
    aliens_with_genre = [aliens[i] for i in range(len(aliens)) if genres[i] == genre]
    aliments = get_all(['Aliment'], 'files/BaseMiams.csv')[0]
    aliens_who_eat = [aliens[i] for i in range(len(aliens)) if aliments[i] == alien_eats]
    triplets = get_triplets()
    return [elem[2] for elem in triplets \
        if elem[1] in aliens_with_genre and elem[1] in aliens_who_eat]

if __name__ == '__main__':
    print(get_gardians_with())