import rhinoscriptsyntax as rs
import random
"""
a = rs.AddPoint([0,0,0])
b = rs.AddPoint([25,5,30])
c = rs.AddLine(a,b)
print(a)#prints out unique id for this item.
print(b)
print(c) """

points = []
for i in range(20):
    x = random.random() * 10
    y = random.random() * 10
    z = random.random() * 10
    p = rs.AddPoint(x,y,z)
    points.append(p)

rs.AddCurve(points)  

"""Keep drawing with rhino. Use new types of geometry.
We will use rhino to create our own turtle in rhino"""