from math import cos,sin
import rhinoscriptsyntax as rs

rs.DeleteObjects(rs.AllObjects('select'))#delete all existing objects

def spiro(R,r,d,angle):
    x = (R-r) * cos(angle) - d * cos(((R-r)/r)*angle) + random.randint(20,30)
    y = (R-r) * sin(angle) - d * sin(((R-r)/r)*angle) + random.randint(20,30)
    m.goto(x,y)
    #print('spiro')

"""define gears and pen sizes and locations"""
outerGearRadius = 10
innerGearRadius = 4
pointDistance = 3 #how far the pen is placed from the center of the innerGear
baseX = 0
baseY = 0
baseZ = 0
basePointOuter = (baseX,baseY,baseZ)
basePointInner = ((baseX + (outerGearRadius - innerGearRadius)),baseY,baseZ)
basePointPen = ((baseX + (outerGearRadius - innerGearRadius)+ pointDistance),baseY, baseZ)
numRotates = 100

"""Insure proportions are correct"""
if outerGearRadius <= innerGearRadius or innerGearRadius <= pointDistance:
    print ('error')
    #stop/exit program somehow

"""draw the gears and pen and create an easily movable group"""
outerGear = rs.AddCircle(basePointOuter, outerGearRadius)
innerGear = rs.AddCircle(basePointInner,innerGearRadius)
pen = rs.AddPoint(basePointPen)
moveMe = [innerGear, pen]

"""Rotate the inner gear and pen"""
"""for i in range(0,numRotates):
    rs.MoveObject(moveMe, vector?)
    rotation = rs.VectorCreate(startpoint, endpoint)"""