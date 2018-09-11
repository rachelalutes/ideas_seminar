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

    def ellipse(self, xheight, yheight, direction):
        centerPoint = rs.AddPoint(self.point)
        if direction == 'right':
            centerPoint = rs.MoveObject(centerPoint, rs.VectorScale(rs.VectorCreate([1,0,0],[0,0,0]), xheight/2))
        if direction == 'left':
            centerPoint = rs.MoveObject(centerPoint, rs.VectorScale(rs.VectorCreate([-1,0,0],[0,0,0]), xheight/2))
        if direction == 'top':
            centerPoint = rs.MoveObject(centerPoint, rs.VectorScale(rs.VectorCreate([0,1,0],[0,0,0]), xheight/2))
        if direction == 'bottom':
            centerPoint = rs.MoveObject(centerPoint, rs.VectorScale(rs.VectorCreate([0,-1,0],[0,0,0]), xheight/2))
        newEllipse = rs.AddCircle(centerPoint, xheight/2)
        yScaleFactor = yheight/xheight
        rs.ScaleObject(newEllipse, self.point, [1,yScaleFactor,0])
        rs.DeleteObject(centerPoint)
        return(newEllipse)

    def rotatedEllipse(self, xheight, yheight, direction, angle):
        newEllipse = self.ellipse(xheight,yheight,direction)
        newEllipse = rs.RotateObject(newEllipse,self.point,angle)

  
bob = Turtle()
bob.forward(10)
bob.ellipse(3,2,'center')
bob.right(30)
bob.forward(5)
bob.ellipse(3,2,'right')
bob.rotatedEllipse(3,2,'right',45)