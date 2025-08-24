import turtle 
import itertools 

screen = turtle.Screen()
screen.bgcolor("#1FFA07")
screen.title("Hypnotic Star")
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(4)

colors = itertools.cycle(["black", "yellow", "red", "light blue", "purple"])

for i in range(150): 
    pen.pencolor(next(colors))
    pen.forward(i * 2.6)
    pen.right(145)

turtle.done()


