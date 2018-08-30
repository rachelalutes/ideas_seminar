#Rachel Lutes
#08/30/2018
#ARCH 7210 Ideas Seminar
#This script creates a surface from a grid of random points

import rhinoscriptsyntax as rs
import random
points = []
u = 10
v = 10

for i in range(0,u):
    for j in range(0,v):
        points.append(rs.AddPoint((i+random.random()),(j+random.random()),random.random()))

rs.AddSrfPtGrid((u,v),points)