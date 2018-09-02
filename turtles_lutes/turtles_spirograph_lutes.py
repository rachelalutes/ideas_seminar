import turtle
from math import cos,sin
from time import sleep
import random

m = turtle.Turtle()
m.speed(0)
R = 30
r = 97
d = 80
angle = 0
theta = 0.1
steps = int(100*3.14/theta)

for t in range(0,steps):
    m.color((random.random(),random.random(),random.random()))
    angle += theta + random.random()
    x = (R-r) * cos(angle) - d * cos(((R-r)/r)*angle) #* random.random()
    y = (R-r) * sin(angle) - d * sin(((R-r)/r)*angle) #* random.random()
    m.goto(x,y)

turtle.done()