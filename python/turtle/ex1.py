import turtle as t
from utils import reset

####### EX 1 #######

def triangle_equ(length: int, up_vertex: bool = False, fill: str = None) -> None:
    if fill: 
        t.fillcolor(fill)
        t.begin_fill()
    if up_vertex:
        t.right(60)
    for _ in range(3):
        t.forward(length)
        t.right(120)
    if fill: t.end_fill()

def triangle_angle(length: int, angle: int) -> None:
    angle += 60
    t.right(angle)
    for _ in range(3):
        t.forward(length)
        t.right(120)

if __name__ == '__main__':
    length = 100
    triangle_equ(length)
    reset()
    triangle_equ(length, up_vertex = True)
    reset()
    triangle_angle(length, 120)
    t.mainloop()