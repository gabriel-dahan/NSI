import numpy as np


def fib(n: int) -> int:
    un = 0
    un1 = 1
    a = 0
    for _ in range(n - 1):
        print(a)
        a = un + un1
        un, un1 = un1, a
    return a

"""

ASSEMBLY - FIBONACCI :

      MOV R0,#0
      MOV R1,#1
      LDR R3,n
      SUB R3,R3,#1
      MOV R4,#0
while:
      CMP R4,R3
      BGT end
      ADD R4,R4,#1
      ADD R2,R0,R1
      MOV R0,R1
      MOV R1,R2
      B while
end:
      STR R2,150
      HALT
n:9

"""

def factorial(a):
      elems = np.array(list(range(1, a + 1)))
      return np.prod(elems)

print(factorial(10))