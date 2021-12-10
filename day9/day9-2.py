
# importing functools for reduce()
import functools

# importing operator for operator functions
import operator

import common as day9


heightMap = day9.getData("day9/data.txt")


lowPoints = day9.getLowPoints(heightMap)

basinSizes = []

for lowPoint in lowPoints:
    basinSizes.append(day9.getBasinSize(lowPoint, heightMap))

basinSizes.sort(reverse=True)

topthree = basinSizes[:3]

print(topthree)
print(functools.reduce(operator.mul, topthree))
