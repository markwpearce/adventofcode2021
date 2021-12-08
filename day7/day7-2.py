def getData(filename: str) -> list[int]:
    file = open(filename, "r")
    lines = file.readlines()
    return list(map(int, lines[0].split(',')))


positions = getData("day7/data.txt")

crabsAtPosition = [0]*(max(positions)+1)


totalDistance = crabsAtPosition.copy()

for num in positions:
    crabsAtPosition[num] += 1


def triangleNum(n: int) -> int:
    return int(n*(n+1)/2)


for d, distances in enumerate(totalDistance):
    for p, crabCount in enumerate(crabsAtPosition):
        totalDistance[d] += triangleNum(abs(d-p))*crabCount

val, idx = min((val, idx) for (idx, val) in enumerate(totalDistance))

print("Fuel: {} for position: {}".format(val, idx))
