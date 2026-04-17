import turtle
screen = turtle.Screen().bgcolor("purple")
pen = turtle.Turtle()
#polygon
def polygon(sides, length):
    angle = 360 / sides
    for i in range(sides):
        pen.forward(length)
        pen.left(angle)
polygon(5, 100)
turtle.done()