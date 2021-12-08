import common as day5


lines = day5.getData("day5/data.txt")

ventLines = []
width = 0
height = 0
for line in lines:
    vl = day5.VentLine(line)
    width = max(width, vl.maxX)
    height = max(height, vl.maxY)
    ventLines.append(vl)

floor = day5.SeaFloor(width+1, height+1)

for vl in ventLines:
    floor.addVentLine(vl, False)


print(floor.toString())
print(floor.countOverThreshold(1))
