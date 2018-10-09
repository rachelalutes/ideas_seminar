import rhinoscriptsyntax as rs

#delete all existing objects
rs.DeleteObjects(rs.AllObjects('select'))

#basic setup of variables
petalRadius = 10 #defines outer edge of flower
petalCount = 10 #number of petals
flowerCenter = (0,0,0) #define center point
petalPoints = [] #start list for point storage
petalCurveWidth = 1 #defines the amount of curve of the petal
petalCurveDistance = 1

outerCircle = rs.AddCircle(flowerCenter,petalRadius)
petalPoints = rs.DivideCurve(outerCircle,petalCount)
rs.AddPoints(petalPoints)

for i in range(0,petalCount):
    #create petal center line
    petalCenterLine = rs.AddLine(petalPoints[i], flowerCenter)
    rs.HideObject(petalCenterLine)
    #find midPoint of petal center line
    petalCenterLineMidPoint = rs.CurveMidPoint(petalCenterLine)
    rs.AddPoint(petalCenterLineMidPoint)
    #draw vector 
    newVector = rs.RotateObject(rs.VectorScale(rs.VectorUnitize(rs.VectorCreate(petalPoints[i],petalCenterLineMidPoint)),petalCurveWidth),petalCenterLineMidPoint,90)
    newPoint = rs.CopyObject(petalCenterLineMidPoint