"""Creating a turtle for rhino
Turtle class has
    attributes
        position
        direction
        line color
        turtle color
    behaviors
        left
        right
        forward
        backward
        circle
        penup
        pendown
        goto
"""
import rhinoscriptsyntax as rs

class Turtle():
    def __init__ (self,pos = [0,0,0],heading = [0,1,0]):
        self.heading = heading
        self.point = rs.AddPoint(pos)
        pointPos = rs.PointCoordinates(self.point)
        self.direction = rs.VectorCreate(heading, pointPos)
        self.lines = []
   
    def forward(self,dist):
        movement = rs.VectorScale(self.direction,dist)
        prevPos = rs.PointCoordinates(self.point)
        rs.MoveObject(self.point, movement)
        currentPos = rs.PointCoordinates(self.point)
        rs.AddLine(prevPos, currentPos)
    
    def left(self, angle):
        self.direction = rs.VectorRotate(self.direction, angle, [0,0,1])

    def right(self, angle):
        self.direction = rs.VectorRotate(self.direction, angle, [0,0,1])

    #def circle(self, radius):
        #put something here

johnny = Turtle()
print (johnny.heading)
print (johnny.point)
print (johnny.direction)

print ("-------")

mohammed = Turtle([5,5,5])
print (mohammed.heading)
print (mohammed.point)
print (mohammed.direction)

mohammed.forward(10)
mohammed.left(10)
mohammed.forward(10)



"""
forward(distance):
    pos = pos + (distance * direction) #update the position of the turtle according to the move just made.

backward(distance):
    pos = pos + (distance * -direction) 

left(angle):
    direction = direction - angle 

right(angle):
    direction = direction + angle

"""





