import random as r
from typing import List

def creer_permut():
  permut=[chr(lettre) for lettre in range(65,91)]
  r.shuffle(permut)
  return permut

def chiffrer_permut(Lp,Tc):
  return "".join([Lp[ord(lettre)-97] for lettre in Tc])

if __name__ == '__main__':
    pass