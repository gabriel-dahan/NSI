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
    t.pencolor('purple')
    for _ in range(iters):
        triangle_equ(length, fill = 'orange')
        space()
        square(length, fill = 'orange')
        space()

if __name__ == '__main__':
    t.mainloop()