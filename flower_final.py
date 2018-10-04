import rhinoscriptsyntax as rs 

#delete all existing objects
rs.ShowObjects(rs.HiddenObjects())
rs.DeleteObjects(rs.AllObjects('select'))

#variables
flowerRadius = 10 #radius of the flower
centerRadius = 2 #radius of the center of the flower
petalCount = 15
flowerCenter = (0,0,0) 
petalWidth = 6 #width of the petals
petals = [] #store petal curves here

#print out the variables
textToPrint = 'flowerRadius = %d\ncenterRadius = %d\npetalCount = %d\npetalWidth = %d' %(flowerRadius,centerRadius,petalCount,petalWidth)
rs.AddText(textToPrint, ((flowerRadius+1),2,0), height=1.0)

#draw outer circle
outerCircle = rs.AddCircle(flowerCenter,flowerRadius) 

#divide to get the point of each petal
points = rs.AddPoints(rs.DivideCurve(outerCircle,petalCount)) 

#draw each petal
for i in range(len(points)):
    #draw line from center to point of the petal
    centerLine = rs.AddLine(points[i],flowerCenter)

    #find the midpoint
    petalMidpoint = rs.AddPoint(rs.CurveMidPoint(centerLine))

    #draw a vector perpendicular to the centerLine, with a length of half the petal width
    vector = rs.VectorCreate(points[i],petalMidpoint) #create vector along the centerline
    vector = rs.VectorUnitize(vector) #unitize the vector to make the length 1
    vector = rs.VectorScale(vector,(petalWidth/2)) #scale vector to make length = half petal width
    vector = rs.VectorRotate(vector,90,[0,0,1]) #rotate vector 90 degrees to centerline
    vector2 = rs.VectorRotate(vector,180,[0,0,1]) #draw the opposite vector for the other side of the petal

    #add a points on the edge of each petal
    petalEdgePoint = rs.CopyObject(petalMidpoint)
    petalEdgePoint = rs.MoveObject(petalEdgePoint,vector)
    petalEdgePoint2 = rs.CopyObject(petalMidpoint)
    petalEdgePoint2 = rs.MoveObject(petalEdgePoint2,vector2)

    #draw edges of the petals
    curve = rs.AddArc3Pt(flowerCenter,points[i],petalEdgePoint)
    curve2 = rs.AddArc3Pt(flowerCenter,points[i],petalEdgePoint2)
    
    #add petal outline to list of petals
    petals.append(rs.JoinCurves([curve,curve2]))

#draw the flower center and raise it slightly
flowerCenterLine = rs.AddCircle(flowerCenter,centerRadius)
flowerCenterSrf = rs.MoveObject(rs.AddPlanarSrf(flowerCenterLine),[0,0,.1])

#draw a surface for each petal
petalSrfs = rs.AddPlanarSrf(petals)

#hide the curves and points
rs.HideObjects(rs.ObjectsByType(4|1,True))