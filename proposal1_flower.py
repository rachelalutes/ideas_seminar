petalRadius = 10 #defines outer edge of flower
petalCount = 10
flowerCenter = (0,0,0) #define center point
petalPoints = [ ] #start list for point storage
petalCurveWidth = defines the amount of curve of the petal
petalCurveDistance

#Create petalCount points equidistant around circle defined by petalRadius and flowerCenter and add to points list.
For i in range(0,petalCount-1):
    petalCenterLine = line from petalPoints[i] to flowerCenter. 
    petalLinePoint = point on petalCenterLine, petalCurveDistance from flowerCenter
    petalLinePoint = point petalCurveWidth away from current petalLinePoint perpendicular to petalCenterLine
    Draw an arc between points petalPoints[i], petalLinePoint, and flowerCenter
    Repeat for other side of petal, curving the opposite direction.
    Draw optional circle in middle for center.
