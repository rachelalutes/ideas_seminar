#Rachel Lutes
#08/30/2018
#ARCH 7210 Ideas Seminar
#This script draws

import rhinoscriptsyntax as rs
import random
import math

a = rs.AddCircle((0,0,0),15)

b = rs.CurvePoints(a)
#c = rs.AddPoint(b[random.randint(0,len(b)-1)],b[random.randint(0,len(b)-1)],0)
#d = rs.AddPoint(b[random.randint(0,len(b)-1)],b[random.randint(0,len(b)-1)],0)
for i in range(len(b)):
    rs.AddLine(b[i],(0,0,0))

rs.ObjectColor(object, (r,g,b))