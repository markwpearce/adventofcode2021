
def onlyNums(num) -> bool:
    return num.isnumeric()


def getData(filename: str, limit: int = -1) -> list[list[int]]:
    file = open(filename, "r")
    lines = file.readlines()
    output = dict()
    output = []

    if limit != -1:
        lines = lines[:limit]
    for line in lines:
        intList = list(map(int, list(filter(onlyNums, list((line))))))
        output.append(intList)

    return output


def riskLevel(height) -> int:
    return height+1


def getLowPoints(heightMap: list[list[int]]) -> list[tuple[int]]:
    lowPoints = []
    width = len(heightMap[0])
    vert = len(heightMap)
    for i, row in enumerate(heightMap):
        for j, height in enumerate(row):
            heightsAround = []
            if j > 0:
                heightsAround.append(row[j-1])
            if j < width-1:
                heightsAround.append(row[j+1])
            if i > 0:
                heightsAround.append(heightMap[i-1][j])
            if i < vert-1:
                heightsAround.append(heightMap[i+1][j])
            if height < min(heightsAround):
                lowPoints.append((i, j))
    return lowPoints


def getBasinSize(lowPoint: tuple[int], heightMap: list[list[int]]) -> int:
    width = len(heightMap[0])
    vert = len(heightMap)

    basinMap = []
    for y in range(vert):
        basinMap.append([])
        for x in range(width):
            basinMap[y].append(0)

    extendBasinMap(lowPoint, basinMap, heightMap)
    basinSize = 0
    for row in basinMap:
        basinSize += sum(row)

    return basinSize


def extendBasinMap(point: tuple[int], basinMap: list[list[int]], heightMap: list[list[int]]):
    y, x = point[0], point[1]
    width = len(heightMap[0])
    vert = len(heightMap)

    if y < 0 or x < 0 or y >= vert or x >= width or heightMap[y][x] == 9 or basinMap[y][x] == 1:
        return

    basinMap[y][x] = 1
    extendBasinMap([y-1, x], basinMap, heightMap)
    extendBasinMap([y, x-1], basinMap, heightMap)
    extendBasinMap([y+1, x], basinMap, heightMap)
    extendBasinMap([y, x+1], basinMap, heightMap)
