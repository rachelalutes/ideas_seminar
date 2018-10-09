limitToResultsContaining = 'NC'

import rhinoscriptsyntax as rs
fhand = open('brickstacking/data analysis/yelp_academic_dataset_business.json')
xCoords = []
yCoords = []
points = []

for line in fhand:
    if limitToResultsContaining in line:
        line.strip()
        pos = line.find('latitude')
        pos2 = line.find(',',pos)
        pos3 = line.find('longitude')
        pos4 = line.find(',',pos3)
        xCoords.append(float(line[pos+10:pos2]))
        yCoords.append(float(line[pos3+11:pos4]))

for i in range(len(xCoords)):
    points.append(rs.AddPoint(xCoords[i],yCoords[i],0))

for i in range(len(points)):
	closest = rs.PointArrayClosestPoint(points,points[i])
	distance = rs.VectorLength(rs.VectorCreate(closest,points[i]))
	'''if distance > 1 :
		points.pop(i)'''