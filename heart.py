import turtle
draw = turtle.Turtle()
win = draw.screen
win.bgcolor('black')
def curve():
    draw.pen(pencolor="white", pensize=3, speed=5)
    for i in range(200):
        draw.rt(1)
        draw.fd(1)

def heart():
    draw.pen(pencolor="white",fillcolor="red", pensize=3, speed=5)
    draw.shape('turtle')
    draw.shapesize(1,1,1)
    draw.begin_fill()
    draw.lt(140)
    draw.fd(113)
    curve()
    draw.lt(120)
    curve()
    draw.fd(112)
    draw.end_fill()

    draw.hideturtle()

heart()
turtle.done()
