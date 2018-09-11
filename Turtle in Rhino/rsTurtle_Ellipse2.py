import rhinoscriptsyntax as rs

allObjs = rs.AllObjects()
rs.DeleteObjects(allObjs)



class Turtle:
    def __init__(self, pos = [0,0,0], heading = [1,0,0]):
        self.heading = heading
        self.point = rs.AddPoint(pos)
        pointPos = rs.PointCoordinates(self.point)
        self.direction = rs.VectorCreate(heading,pointPos)
        self.lines = []
    
    def forward(self,magnitude):
        print (self.direction)
        movement = rs.VectorScale(self.direction,magnitude)
        prevPos = rs.PointCoordinates(self.point)
        rs.MoveObject(self.point,movement)
        currentPos = rs.PointCoordinates(self.point)
        rs.AddLine(prevPos,currentPos)
        
    def left(self,angle):
        self.direction = rs.VectorRotate(self.direction, angle, [0,0,1])
        print(self.direction)
        
    def right(self,angle):
        self.direction = rs.VectorRotate(self.direction, -angle, [0,0,1])
        print(self.direction)
    
    def goto(self, x, y):
        prevPos = rs.PointCoordinates(self.point)
        movement = rs.VectorCreate([x,y,0],prevPos)
        rs.MoveObject(self.point,movement)
        currentPos = rs.PointCoordinates(self.point)
        rs.AddLine(prevPos,currentPos)

#ellipse guide
#   xheight and yheight are the dimensions of the ellipse when created with angle 0
#   placement is where the turtle is on the ellipse. enter 'center' or 'edge'
#   angle is the angle of rotation from original ellipse placement. 
#       when placement is center
#           90 and 270 have the same effect as swaping xheight and yheight
#           0 and 180 do nothing
#       when placement is edge
#           0 will place ellipse to right of turtle
#           90 will place ellipse above turtle with xheight and yheight appearing flipped
#           180 will place ellips to left of turtle
#           270 will place ellipse below turtle with xheight and yheight appearing flipped
#   xheight and yheight are required
#   placement and angle are optional and will default to center and 0 respectivly

    def ellipse(self, xheight, yheight, placement = 'center', angle = 0):
        centerPoint = rs.AddPoint(self.point)
        if placement == 'edge':
            centerPoint = rs.MoveObject(centerPoint, rs.VectorScale(rs.VectorCreate([1,0,0],[0,0,0]), xheight/2))
        newEllipse = rs.AddCircle(centerPoint, xheight/2)
        ScaleFactor = yheight/xheight
        rs.ScaleObject(newEllipse, self.point, [1,ScaleFactor,0])
        newEllipse = rs.RotateObject(newEllipse,self.point,angle)
        rs.DeleteObject(centerPoint)
