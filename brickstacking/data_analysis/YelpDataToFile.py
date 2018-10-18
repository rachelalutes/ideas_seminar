fhand = open('yelp_academic_dataset_business.json')
xCoordinateList = ''
yCoordinateList = ''

for line in fhand:
    if 'Charlotte' in line:
        line.strip()
        pos = line.find('latitude')
        pos2 = line.find(',',pos)
        pos3 = line.find('longitude')
        pos4 = line.find(',',pos3)
        xcoord = line[pos+10:pos2]
        ycoord = line[pos3+11:pos4]
        xCoordinateList = xCoordinateList + xcoord + ','
        yCoordinateList = yCoordinateList + ycoord + ','

#strip final comma from file
xCoordinateList = xCoordinateList[:-1]
yCoordinateList = yCoordinateList[:-1]

#write lists to file as a comma seperated string
fout = open('XyelpCharlotte', 'w')
fout.write(xCoordinateList)
fouty = open('YyelpCharlotte', 'w')
fouty.write(yCoordinateList)