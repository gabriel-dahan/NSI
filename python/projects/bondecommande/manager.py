import csv
from typing import Dict, List

def lecture_bon(file: str = './commands.csv') -> List[Dict]:
    with open(file) as fp:
        f = csv.DictReader(fp)
        l = []
        for object_ in f:
            for k, v in object_.items():
                if k in ('prix', 'qté'):
                    object_[k] = float(v) if k == 'prix' else int(v)
            l.append(object_)
        return l

def verifie_quantites(b: List[Dict]) -> bool:
    return all(object_['qté'] >= 0 for object_ in b)

def facture(b: List[Dict]) -> float:
    assert verifie_quantites(b), 'Les objets commandés doivent être présents en quantités positives.'
    return sum(object_['prix'] for object_ in b)

def poids_commande(b: List[Dict], poids: Dict) -> float:
    return sum(poids.values())

def articles_lourds(b: List[Dict], poids: Dict) -> List[Dict]:
    return [object_ for object_ in b if poids[object_['Réf.']] > 200]

def exporter_nouveau_bon(b: List[Dict], file_name: str):
    with open('commands.csv') as fp:
        descriptors = csv.DictReader(fp).fieldnames
    with open(file_name, 'w') as fp:
        writer = csv.DictWriter(fp, descriptors)
        writer.writeheader()
        writer.writerows(b)

def main():
    poids_produits = {
        '45672': 250.5,
        '16722': 70,
        '97612': 15,
        '62120': 400.25,
        '56721': 150,
        '12949': 100
    }
    lecture = lecture_bon()
    alourds = articles_lourds(lecture, poids_produits)
    exporter_nouveau_bon(alourds, 'commands_new.csv')

if __name__ == '__main__':
    main()