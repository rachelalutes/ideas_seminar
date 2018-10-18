import rhinoscriptsyntax as rs
import math
import Rhino
from Rhino.Geometry import *

points = []
epoints = []
spoints = []
split = []
csplit = []
hcurve = []
dom = []
cir = []
cplane = []


YAxis = rs.WorldXYPlane()
vector = (0,0,1)
point = rs.AddPoint(5,1,-10)
r = 1

#create the points for the first hyperbolic curve
for d in rs.frange(-2,4, 0.1):
    x = d 
    z =  -(math.cosh(x))
    y = 1 
    pt = (x,y,z)
    rs.AddPoint(x,y,z)
    points.append(pt)

#create the circles and planes from them
for c in range (0,7):
    X = 5
    Y = 1
    Z = -23 + c ** 2 / 2
    point = (X,Y,Z)
    r = r + 0.3
    circle = rs.AddCircle(point, r)
    cir.append(circle)
    domain = rs.CurveDomain(circle)
    dom.append(domain)
    plane = rs.AddPlanarSrf(circle)
    cplane.append(plane)



#rotate the first curve and intersect the curves with circles
for i in range(1,30):
 curve = rs.AddCurve(points)
 rcurve = rs.RotateObject(curve, point, i * 10 , vector, copy=True)
 hcurve.append(rcurve)
#intersection
 for h in xrange(0,7):
        cur,intpoint = rs.CurveBrepIntersect(rcurve, cplane[h])
        split.append(intpoint[0])
#make a domain for each trim and trim the curves
 domain = rs.CurveDomain(rcurve)
 domain[1] /= i * 0.08
 domain[0] /= i * 2
 tcurve = rs.TrimCurve(rcurve, domain )
 epoint = rs.CurveEndPoint(tcurve)
 spoint = rs.CurveStartPoint(tcurve)
 epoints.append(epoint)
 spoints.append(spoint)

ecurve = rs.AddCurve(epoints)
scurve = rs.AddCurve(spoints)
