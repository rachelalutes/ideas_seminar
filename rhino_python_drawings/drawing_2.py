#Rachel Lutes
#08/30/2018
#ARCH 7210 Ideas Seminar
#This script draws a series of lines with circles on the ends

import rhinoscriptsyntax as rs
import random

points = []
points2 = []
numlines = 40
for i in range(0,numlines):
    a = random.random()*random.randint(1,20)
    b = random.random()*random.randint(1,20)
    c = random.random()*random.randint(1,20)
    d = random.random()*random.randint(1,20)
    e = random.random()*random.randint(1,20)
    f = random.random()*random.randint(1,20)
    rs.AddLine((a,b,c),(d,e,f))
    points.append((a,b,c))
    points2.append((d,e,f))
    rs.AddSphere((a,b,c),.1)
    rs.AddSphere((d,e,f),.2)

numpoints = len(points)
for p in range(0,numpoints):
    d = random.randint(0,numpoints)
    rs.AddLine(points[p],points2[d])