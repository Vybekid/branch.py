import turtle
import itertools

screen = turtle.Screen()
screen.bgcolor("#111111")
screen.title("Hypnotic Spiral")
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(2)

colors = itertools.cycle(["#FF00FF", "#00FFFF", "#FFFF00", "#FF4500", "#32CD32"])

for i in range(250):
    pen.pencolor(next(colors))
    pen.circle(i, 80)
    pen.right(10)
    
turtle.done()
