import turtle as t
from utils import reset
from math import ceil, sqrt
from ex1 import triangle_equ
from ex2 import square

####### EX 4 #######

def rays(n: int, d: int) -> None:
    for _ in range(n):
        t.forward(d)
        reset(reset_heading = False)
        t.right(360 / n) # 360 / n --> nmb of degrees necessary between each ray

def polygon(a: int, n: int) -> None:
    for _ in range(n):
        t.forward(a)
        t.right(360 / n)

def star(a: int, n: int, invert: bool = False) -> None:
    for _ in range(n):
        t.forward(a)
        if invert:
            t.left(2 * (360 / n))
            continue
        t.right(2 * (360 / n))
    t.forward(a)

def star_sequence(stars: int, sides: int = 5, ratio: float = 0.20, min_l: int = 25, space: int = 20) -> None:
    mid_seq = ceil(stars / 2) if stars % 2 != 0 else stars / 2
    for i in range(stars):
        if i < mid_seq:
            star(min_l + min_l * (i * ratio), sides)
        elif i == mid_seq and mid_seq == stars / 2:
            star(min_l + min_l * ((i - 1) * ratio), sides)
        else:
            i -= mid_seq + 2 if mid_seq == stars / 2 else mid_seq + 1
            star(min_l - min_l * (i * ratio), sides)
        t.up()
        t.forward(space)
        t.down()

def david_star(a: int, no_triangle: bool = False) -> None:
    rel = (a / 4) / (sqrt(3) / 2)
    if no_triangle:
        t.right(60)
        for i in range(6):
            t.right(60)
            t.forward(rel)
            t.left(60)
            t.forward(rel)
            t.right(60)
        return
    triangle_equ(a)
    t.up()
    t.forward(a / 2)
    t.left(90)
    t.forward(a / 4)
    t.right(90)
    t.down()
    triangle_equ(a, up_vertex = True)
    t.up()
    t.right(30)
    t.forward(a / 4)
    t.left(90)
    t.forward(a / 2)
    t.down()

def geometric_spiral(iters: int, length: int = 50, space: int = 20):
    l = length
    s = space
    for _ in range(iters):
        david_star(l)
        t.up()
        t.forward(s + l / 2)
        t.left(90)
        t.forward(l * (sqrt(3) / 2))
        t.right(90)
        t.down()
        triangle_equ(l, up_vertex = True)
        t.up()
        t.forward(l)
        t.left(60)
        t.forward(s)
        t.down()
        star(l, 5, invert = True)
        t.up()
        t.forward(s)
        t.left(90)
        t.forward(l)
        t.right(90)
        t.down()
        square(l)
        t.up()
        t.forward(l + 2 * s)
        t.down()
        t.right(45)
        l *= 0.80
        s *= 0.80 

if __name__ == '__main__':
    t.speed(20)
    geometric_spiral(15)
    t.mainloop()