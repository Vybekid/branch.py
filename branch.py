import turtle
import itertools

screen = turtle.Screen()
screen.bgcolor("#111111")
screen.title("Hypnotic Spiral")
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(2)

colors = itertools.cycle(["#FF007F", "#00FFFF", "#33CC66", "#FFD700", "#FF4500"])

for i in range(150):
    pen.pencolor(next(colors))
    pen.forward(i * 1.5)
    pen.right(145)

turtle.done()
