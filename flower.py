import rhinoscriptsyntax as rs 

#delete all existing objects
rs.DeleteObjects(rs.AllObjects('select'))

#variables
flowerRadius = 10
centerRadius = 2
petalCount = 15
flowerCenter = (0,0,0)
petalWidth = 4
petalCurves = []

outerCircle = rs.AddCircle(flowerCenter,flowerRadius)
points = rs.AddPoints(rs.DivideCurve(outerCircle,petalCount))
rs.HideObjects(points)

for i in range(len(points)):
    centerLine = rs.AddLine(points[i],flowerCenter)
    rs.HideObject(centerLine)
    petalMidpoint = rs.AddPoint(rs.CurveMidPoint(centerLine))
    rs.HideObjects(petalMidpoint)
    vector = rs.VectorCreate(points[i],petalMidpoint)
    vector = rs.VectorUnitize(vector)
    vector = rs.VectorScale(vector,(petalWidth/2))
    vector = rs.VectorRotate(vector,90,[0,0,1])
    petalEdgePoint = rs.CopyObject(petalMidpoint)
    petalEdgePoint = rs.MoveObject(petalEdgePoint,vector)
    curve = rs.AddArc3Pt(flowerCenter,points[i],petalEdgePoint)
    vector2 = rs.VectorRotate(vector,180,[0,0,1])
    petalEdgePoint2 = rs.CopyObject(petalMidpoint)
    petalEdgePoint2 = rs.MoveObject(petalEdgePoint2,vector2)
    curve2 = rs.AddArc3Pt(flowerCenter,points[i],petalEdgePoint2)
    petalCurves.append(rs.JoinCurves([curve,curve2]))

rs.AddPlanarSrf(petalCurves)

rs.MoveObject(rs.AddPlanarSrf(rs.AddCircle(flowerCenter,centerRadius)),[0,0,.1])

rs.HideObjects(rs.ObjectsByType(4,True))