import turtle as t
from utils import start_before

####### EX 2 #######

def square(length: int, fill: str = None) -> None:
    if fill: 
        t.fillcolor(fill)
        t.begin_fill()
    for _ in range(4):
        t.forward(length)
        t.right(90)
    if fill: t.end_fill()

def square_sequence(a: int, n: int) -> None:
    start_before()
    for _ in range(n):
        square(a)
        t.up()
        t.forward(a + a / 4)
        t.down()

def growing_squares(a: int, n: int) -> None:
    coeff = 1.25
    start_before()
    square(a)
    space = a / 4
    t.up()
    t.forward(a + space)
    t.down()
    length = a * coeff
    for _ in range(n):
        square(length)
        space *= coeff
        t.up()
        t.forward(length + space)
        t.down()
        length *= coeff
        print(space, length)

if __name__ == '__main__':
    t.mainloop()