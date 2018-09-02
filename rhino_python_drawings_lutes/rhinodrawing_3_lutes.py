#Rachel Lutes
#08/30/2018
#ARCH 7210 Ideas Seminar
#This script draws spirals and changes their color.

import rhinoscriptsyntax as rs
import random
spirals = []
for r in range(1,100): 
    r1 = r*random.random() #randomize the end radius
    t = random.random() #randomize number of turns
    a = rs.AddSpiral((0,0,0),(0,0,1),0,t,0,r1)
    b = rs.planar(a,(0,0,0))
    spirals.append(b)
    rs.ObjectColor(b,(128,g,b))
    #c = rs.AddHatch(b)
    #spirals.append(c)
