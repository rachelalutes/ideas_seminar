fhand = open('NASA_Locations.txt')
xCoordinateList = ''
yCoordinateList = ''
for line in fhand:
    line.strip()
    pos = line.find('(')
    pos2 = line.find(',')
    pos3 = line.find(')')
    xcoord = line[pos+1:pos2]
    xcoord.strip()
    ycoord = line[pos2+2:pos3]
    ycoord.strip()
    xCoordinateList = xCoordinateList + xcoord + ','
    yCoordinateList = yCoordinateList + ycoord + ','

    
    


print(xCoordinateList)
print('\n')
print(yCoordinateList)

"""xMax = max(xCoordinateList)
xMin = min(xCoordinateList)
yMax = max(yCoordinateList)
yMin = min(yCoordinateList)"""

"""print('xMax = ',xMax,'\nxMin = ',xMin,'\nyMax = ',yMax,'\nyMin = ',yMin)

fout = open('output_NASA_locations_x', 'w')
for i in range(len(xCoordinateList)-1):
    fout.write(xCoordinateList[i])
    fout.write('\n')

fout = open('output_NASA_locations_y', 'w')
for i in range(len(yCoordinateList)-1):
    fout.write(yCoordinateList[i])
    fout.write('\n')"""

