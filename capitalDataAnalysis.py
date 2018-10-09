fhand = open('capitals.rtf')
xCoordinateList = ''
yCoordinateList = ''
for line in fhand:
    line.strip()
    pos = line.find('latitude')
    pos2 = line.find(',',pos)
    pos3 = line.find('longitude')
    pos4 = line.find(',',pos3)
    xcoord = line[pos+10:pos2]
    ycoord = line[pos3+11:pos4]
    xCoordinateList = xCoordinateList + xcoord + ','
    yCoordinateList = yCoordinateList + ycoord + ','

'''print(xCoordinateList)
print('\n')
print(yCoordinateList)'''

fout = open('Xcapitals', 'w')
fout.write(xCoordinateList)
fouty = open('Ycapitals', 'w')
fouty.write(yCoordinateList)