import turtle as t
from utils import reset

####### EX 4 #######

def rays(n: int, d: int) -> None:
    for _ in range(n):
        t.forward(d)
        reset(reset_heading = False)
        t.right(360 / n) # 360 / n --> nmb of degrees necessary between each ray

if __name__ == '__main__':
    t.speed(20)
    rays(18, 60)
    t.mainloop()