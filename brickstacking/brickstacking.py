import rhinoscriptsyntax as rs

allObjs = rs.AllObjects()
rs.DeleteObjects(allObjs)

#define imputs for brick wall
height = rs.GetReal('Please enter brick height',2.25)
length = rs.GetReal('Please enter brick length',7.625)
width = rs.GetReal('Please enter brick width',3.325)
gap = rs.GetReal('Please enter desired gap between bricks',.9)
spaceBetweenBricks = length+gap
rowCount = rs.GetInteger('Please enter desired number of rows of bricks',10)
rotation = rs.GetReal('Please enter brick rotation in degrees',0)

#create the world axis as vectors
worldZAxis = rs.VectorCreate([0,0,1],[0,0,0])

#create curves to define wall and loft to get wall surface
#upperCurve = rs.AddCurve([[7,7,0],[15,-8,0],[0,-16,0]])
#lowerCurve = rs.AddCurve([[12,12,0],[1,11,0],[-3,8,0],[6,-2,0],[-7,-11,0]])
lowerCurve = rs.AddCurve(rs.GetPoints(True,True,'Please select points to create lower curve of wall'))
upperCurve = rs.AddCurve(rs.GetPoints(True,True,'Please select points to create upper curve of wall, be sure to start on the same end of the wall as the lower curve'))
upperCurve2 = rs.CopyObject(upperCurve,rs.VectorScale(worldZAxis,(height*rowCount)))
loftedSurface = rs.AddLoftSrf([lowerCurve,upperCurve2])
rs.HideObjects([loftedSurface,lowerCurve,upperCurve,upperCurve2])

#intersect planes with surface to get the profile of the wall at each row
intersected = rs.AddSrfContourCrvs(loftedSurface,([0,0,0], [0,0,(height*rowCount)]),height)
rs.HideObjects(intersected)

#make list of even and list of odd row profiles
intersectedEven = []
intersectedOdd = []
for i in range(len(intersected)):
    if i%2 == 0 :
        intersectedEven.append(intersected[i])
    else:
        intersectedOdd.append(intersected[i])

#divide each list of rows and save points and tangents
pointsEven = []
pointsOdd = []
tangentsEven = []
tangentsOdd = []
for i in range(len(intersectedEven)):
    #get points
    newPoints = (rs.DivideCurveEquidistant(intersectedEven[i],spaceBetweenBricks,False,True))
    for p in range(len(newPoints)):
        pointsEven.append(newPoints[p])
    #get tangents
    for p in range(len(pointsEven)):
        closest = rs.CurveClosestPoint(intersectedEven[i],pointsEven[p])
        tangentsEven.append(rs.CurveTangent(intersectedEven[i],closest))

for i in range(len(intersectedOdd)):
    #get points
    newPoints = (rs.DivideCurveEquidistant(intersectedOdd[i],spaceBetweenBricks/2,False,True))
    for p in range(len(newPoints)):
        if p % 2 != 0:
            pointsOdd.append(newPoints[p])
    #get tangents
    for p in range(len(pointsOdd)):
        closest = rs.CurveClosestPoint(intersectedOdd[i],pointsOdd[p])
        tangentsOdd.append(rs.CurveTangent(intersectedOdd[i],closest))

#rotate the tangent vectors around the world z axis
for i in range(len(tangentsEven)):
    tangentsEven[i] = rs.VectorRotate(tangentsEven[i], rotation, worldZAxis)
for i in range(len(tangentsOdd)):
    tangentsOdd[i] = rs.VectorRotate(tangentsOdd[i], rotation, worldZAxis)

#create a plane at each point with tangent as the normal
planesEven = []
planesOdd = []
for i in range(len(pointsEven)):
    planesEven.append(rs.PlaneFromNormal(pointsEven[i],tangentsEven[i]))
    #rs.AddPlaneSurface(rs.PlaneFromNormal(pointsEven[i],tangentsEven[i]),2,2)
for i in range(len(pointsOdd)):
    planesOdd.append(rs.PlaneFromNormal(pointsOdd[i],tangentsOdd[i]))
    #rs.AddPlaneSurface(rs.PlaneFromNormal(pointsOdd[i],tangentsOdd[i]),2,2)

#function to create a centered rectangle
def RectangleCentered(plane,height,length,width):
    x = width/2
    y = height/2
    z = length/2
    p0 = plane.PointAt(x,y,-z)
    p1 = plane.PointAt(-x,y,-z)
    p2 = plane.PointAt(-x,-y,-z)
    p3 = plane.PointAt(x,-y,-z)
    p4 = plane.PointAt(x,y,z)
    p5 = plane.PointAt(-x,y,z)
    p6 = plane.PointAt(-x,-y,z)
    p7 = plane.PointAt(x,-y,z)
    bricks.append(rs.AddBox([p0,p1,p2,p3,p4,p5,p6,p7]))

#draw a brick centered at each plane 
planes = []
for i in range(len(planesEven)):
    planes.append(planesEven[i])
for i in range(len(planesOdd)):
    planes.append(planesOdd[i])
bricks = []
for i in range(len(planes)):
    RectangleCentered(planes[i],height,length,width)
