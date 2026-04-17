import turtle
screen = turtle.Screen().bgcolor("skyblue")
pen = turtle.Turtle()
#semicircle
def semicircle(radius):
    for i in range(180):
        pen.forward(1)
        pen.left(1)
semicircle(100)
turtle.done()
