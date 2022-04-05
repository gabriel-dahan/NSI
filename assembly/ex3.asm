MOV R0,#0
MOV R1,#0
LDR R2,n
CMP R2,R0
BGT while
HALT
while:
  ADD R1,R1,#1
  ADD R0,R0,R1
  CMP R2,R1
  BGT while
  STR R0,100
  STR R1,101
  HALT
n:10

----- OU ALORS (correction de la prof) -----

INP R0,2
MOV R1,#1
MOV R2,R1
while:
    CMP R1,R0
    BEQ end
    ADD R1,R1,#1
    ADD R2,R1,R2
    B while
end:
    OUT R2,4
    HALT