import turtle as t
from ex1 import triangle_equ
from ex2 import square

####### EX 3 #######

def plain_figures(iters: int, length: int) -> None:
    def space():
        t.up()
        t.forward(length)
        t.down()
    t.width(3)
    t.color('purple', 'orange')
    for _ in range(iters):
        t.begin_fill()
        triangle_equ(length)
        t.end_fill()
        space()
        t.begin_fill()
        square(length)
        t.end_fill()
        space()

def rays(n: int, d: int) -> None:
    pass