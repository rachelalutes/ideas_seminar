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
        if direction == center:
            centerPoint = self.point
        else if direction == right:
            centerPoint = rs.CopyObject(self.point, rs.VectorScale(rs.VectorCreate([1,0,0],[0,0,0]), xheight/2))
        else if direction == left:
            centerPoint = rs.CopyObject(self.point, rs.VectorScale(rs.VectorCreate([-1,0,0],[0,0,0]), xheight/2))
        else if direction == top:
            centerPoint = rs.CopyObject(self.point, rs.VectorScale(rs.VectorCreate([0,1,0],[0,0,0]), yheight/2))
        else if direction == bottom:
            centerPoint = rs.CopyObject(self.point, rs.VectorScale(rs.VectorCreate([0,-1,0],[0,0,0]), yheight/2))
        else:
            print('invalid direction')
            continue
        newEllipse = rs.AddCircle(centerPoint, xheight/2)
        yScaleFactor = yheight/xheight
        rs.ScaleObject(newEllipse, self.point, [1,yScaleFactor,0])

    '''def ellipseRight(self, xheight, yheight):
        newVector = rs.VectorCreate([1,0,0],[0,0,0])
        centerPoint = rs.CopyObject(self.point, rs.VectorScale(newVector, xheight/2))
        newEllipse = newEllipse = rs.AddCircle(centerPoint, xheight/2)
        yScaleFactor = yheight/xheight
        rs.ScaleObject(newEllipse, centerPoint, [1,yScaleFactor,0])

    def ellipseLeft(self, xheight, yheight):
        newVector = rs.VectorCreate([-1,0,0],[0,0,0])
        centerPoint = rs.CopyObject(self.point, rs.VectorScale(newVector, xheight/2))
        newEllipse = newEllipse = rs.AddCircle(centerPoint, xheight/2)
        yScaleFactor = yheight/xheight
        rs.ScaleObject(newEllipse, centerPoint, [1,yScaleFactor,0])
    
    def ellipseTop(self, xheight, yheight):
        newVector = rs.VectorCreate([0,1,0],[0,0,0])
        centerPoint = rs.CopyObject(self.point, rs.VectorScale(newVector, yheight/2))
        newEllipse = newEllipse = rs.AddCircle(centerPoint, xheight/2)
        yScaleFactor = yheight/xheight
        rs.ScaleObject(newEllipse, centerPoint, [1,yScaleFactor,0])

    def ellipseBottom(self, xheight, yheight):
        newVector = rs.VectorCreate([0,-1,0],[0,0,0])
        centerPoint = rs.CopyObject(self.point, rs.VectorScale(newVector, yheight/2))
        newEllipse = newEllipse = rs.AddCircle(centerPoint, xheight/2)
        yScaleFactor = yheight/xheight
        rs.ScaleObject(newEllipse, centerPoint, [1,yScaleFactor,0])'''

    


bob = Turtle()
bob.forward(10)
#bob.ellipse(3,2)
bob.right(30)
bob.forward(5)
bob.ellipseLeft(5,3)