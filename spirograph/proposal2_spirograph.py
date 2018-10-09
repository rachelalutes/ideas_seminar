from math import cos,sin
import rhinoscriptsyntax as rs

rs.DeleteObjects(rs.AllObjects('select'))#delete all existing objects

def spiro(R,r,d,angle):
    x = (R-r) * cos(angle) - d * cos(((R-r)/r)*angle) + random.randint(20,30)
    y = (R-r) * sin(angle) - d * sin(((R-r)/r)*angle) + random.randint(20,30)
    m.goto(x,y)
    #print('spiro')

outerGearRadius = 10
innerGearRadius = 5
basePoint = (0,0,0)
basePoint2 = ((basePoint + (outerGearRadius - innerGearRadius)),0,0)
print (basePoint)
print (basePoint2)
pointDistance = 2 #how far the pen is placed from the edge of the innerGear
outerGear = rs.AddCircle(basePoint, outerGearRadius)
innerGear = rs.AddCircle(basePoint+((outerGearRadius-innerGearRadius),0,0),innerGearRadius)