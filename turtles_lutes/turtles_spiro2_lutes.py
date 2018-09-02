import turtle
from math import cos,sin
from time import sleep
import random

def spiro(R,r,d,angle):
    x = (R-r) * cos(angle) - d * cos(((R-r)/r)*angle) + random.randint(20,30)
    y = (R-r) * sin(angle) - d * sin(((R-r)/r)*angle) + random.randint(20,30)
    m.goto(x,y)
    #print('spiro')

m = turtle.Turtle()
m.speed(0)
Rlist = [400,480]
rlist = [520,520]
dlist = [60,68]
slist = [825, 825] #int(50*3.14/theta)
startpoint = m.pos()
#x = 0
#y = 0

for i in range(0,2):
    #define variables for each new pattern
    R = random.randint(0,300) #Rlist[i]
    r = random.randint(0,300) #rlist[i]
    d = random.randint(0,300) #dlist[i]
    angle = 0
    theta = 0.1
    steps = slist[i]
    color = (random.random(),random.random(),random.random())
    m.color(color)
    print('\n\n\nR = ',R, '\nr = ',r,'\nd = ',d,'\nangle = ',angle,'\ntheta = ',theta,'\nsteps = ',steps,'\ncolor = ',color)

    #move to starting location without drawing
    for t in range(0,steps):
        if t == 0 : #no line from center to start
            m.penup()
            angle += theta
            spiro(R,r,d,angle)
            m.pendown()
            startpoint = m.pos()
            continue
        
        angle += theta
        spiro(R,r,d,angle)
        if m.pos()==startpoint: 
            print('exit')
            break

turtle.done()