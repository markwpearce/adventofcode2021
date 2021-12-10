import common as day9


heightMap = day9.getData("day9/data.txt")


for row in heightMap:
    print(row)

lowPoints = day9.getLowPoints(heightMap)

totalRisk = 0

for lowPoint in lowPoints:
    height = heightMap[lowPoint[0]][lowPoint[1]]
    print(height)
    totalRisk += day9.riskLevel(height)

print(totalRisk)
