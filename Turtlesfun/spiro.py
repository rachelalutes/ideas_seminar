import turtle
from math import cos,sin
from time import sleep
import random

m = turtle.Turtle()
m.speed(0)
Rlist = [240,200]
rlist = [260,260]
dlist = [34,30]
startpoint = (0,0)

for i in range(0,2):
    R = Rlist[i] #random.randint(0,300)
    r = rlist[i] #random.randint(0,300)
    d = dlist[i] #random.randint(0,300)
    angle = 0
    theta = 0.1
    steps = int(10*3.14/theta)
    color = (random.random(),random.random(),random.random())
    m.color(color)
    print('\n\n\nR = ',R, '\nr = ',r,'\nd = ',d,'\nangle = ',angle,'\ntheta = ',theta,'\nsteps = ',steps,'\ncolor = ',color)
    for t in range(0,steps):
        if t == 0 : #no line from center to start
            m.penup()
            angle += theta #+ random.random()
            x = (R-r) * cos(angle) - d * cos(((R-r)/r)*angle) #* random.random()
            y = (R-r) * sin(angle) - d * sin(((R-r)/r)*angle) #* random.random()
            m.goto(x,y)
            startpoint = (x,y)
            m.pendown()
            continue
        angle += theta #+ random.random()
        x = (R-r) * cos(angle) - d * cos(((R-r)/r)*angle) #* random.random()
        y = (R-r) * sin(angle) - d * sin(((R-r)/r)*angle) #* random.random()
        m.goto(x,y)
        if m.pos() == startpoint: 
            print('exit 1')
            continue

turtle.done()