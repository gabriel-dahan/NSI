# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 17:57:41 2022

@author: Sylvaine
"""

import csv
from copy import deepcopy
def lecture(fichier):
    objet = csv.DictReader(open(fichier+".csv"))
    return [dict(ligne) for ligne in objet]  

def jointure(table1,table2,cle):
    tablej = []
    for ligneA in table1:
        for ligneB in table2:
            if ligneA[cle]==ligneB[cle]:
                new_line = deepcopy(ligneA)
                for k in ligneB:
                    if k != cle:
                        new_line[k]= ligneB[k]
                tablej.append(new_line)
    
    return tablej