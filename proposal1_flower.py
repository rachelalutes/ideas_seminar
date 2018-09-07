import rhinoscriptsyntax as rs

rs.DeleteObjects(rs.AllObjects('select'))#delete all existing objects

petalRadius = 10 #defines outer edge of flower
petalCount = 10
flowerCenter = (0,0,0) #define center point
petalPoints = [] #start list for point storage
petalCurveWidth = 1 #defines the amount of curve of the petal
petalCurveDistance = 1

outerCircle = rs.AddCircle(flowerCenter,petalRadius)
petalPoints = rs.DivideCurve(outerCircle,petalCount)

print(petalPoints)
for i in range(0,petalCount):
    petalCenterLine = rs.AddLine(petalPoints[i], flowerCenter) 
    petalCenterLineCenter = rs.CurveMidPoint(petalCenterLine)
    rs.AddPoint(petalCenterLineCenter)
    point = AddVector()
    #petalLinePoint = rs.AddCurve(petalPoints[i],)point on petalCenterLine, petalCurveDistance from flowerCenter
    #petalLinePoint = point petalCurveWidth away from current petalLinePoint perpendicular to petalCenterLine
    #Draw an arc between points petalPoints[i], petalLinePoint, and flowerCenter
    #Repeat for other side of petal, curving the opposite direction.
#Draw optional circle in middle for center.
