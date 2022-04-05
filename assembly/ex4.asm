LDR R0,a
LDR R1,b
LDR R2,c
MOV R3,#0
CMP R0,R1
BGT fun1
MOV R3,R1
CMP R2,R3
BGT fun2
HALT
fun1:
    MOV R3,R0
    HALT
fun2:
    MOV R3,R2
    HALT
    
a:1
b:2
c:3