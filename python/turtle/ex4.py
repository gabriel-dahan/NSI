import turtle as t
from utils import reset
from math import ceil

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

def star(a: int, n: int) -> None:
    for _ in range(n):
        t.forward(a)
        t.right(2 * (360 / n))
    t.forward(a)

def star_sequence(stars: int, sides: int = 5, max_slength: int = 100, space: int = 20):
    mid_seq = stars // 2 if stars % 2 != 0 else stars / 2
    for i in range(stars, 0, -1):
        print(i, mid_seq)
        if i < mid_seq:
            print(1)
            star(max_slength - i / 10, sides)
        else:
            star(max_slength - i * 10, sides)
        t.up()
        t.forward(space)
        t.down()

if __name__ == '__main__':
    t.speed(1000)
    rays(10000, 100)
    t.mainloop()