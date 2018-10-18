import rhinoscriptsyntax as rs

fhandx = open('XyelpCharlotte')
fhandy = open('YyelpCharlotte')

xCoords = []
yCoords = []
points = []

xstring = fhandx.read()
ystring = fhandy.read()

xCoords = xstring.split(',')
yCoords = ystring.split(',')

for i in range(len(xCoords)):
    xCoords[i] = float(xCoords[i])
    yCoords[i] = float(yCoords[i])
    points.append(rs.AddPoint(xCoords[i],yCoords[i],0))