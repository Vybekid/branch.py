from turtle import *
import colorsys as cs

tracer(2)
bgcolor('black')
pensize(2)
h = 0.3

for i in range(500):
    c = cs.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.005
    rt(14)
    for j in range(5):
        fd(200)
        rt(144)