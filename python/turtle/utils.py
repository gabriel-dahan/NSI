import turtle as t

def reset(reset_heading: bool = True):
    t.up()
    t.goto(0, 0)
    if reset_heading:
        t.setheading(0)
    t.down()

def start_before():
    t.up()
    t.goto(-100, 0)
    t.down()