#Rachel Lutes
#08/30/2018
#ARCH 7210 Ideas Seminar
#This script draws a series of spirals with some randomness.

import rhinoscriptsyntax as rs
import random

for r in range(1,100): 
    r1 = r*random.random() #randomize the end radius
    t = random.random() #randomize number of turns
    a = rs.AddSpiral((0,0,0),(0,0,1),0,t,0,r1)
    #(start point, direction, flat or some depth, turns, how close to center to start, how close to center to finish.
