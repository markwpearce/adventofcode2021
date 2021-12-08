def getData(filename: str):
    file = open(filename, "r")
    lines = file.readlines()
    return lines


class Point:
    def __init__(self, coordsStr: str):
        parts = coordsStr.split(',')
        self.x = int(parts[0])
        self.y = int(parts[1])


class VentLine:
    def __init__(self, coordsStr: str):
        parts = coordsStr.split(' -> ')
        self.p1 = Point(parts[0])
        self.p2 = Point(parts[1])
        self.minX = min(self.p1.x, self.p2.x)
        self.maxX = max(self.p1.x, self.p2.x)
        self.minY = min(self.p1.y, self.p2.y)
        self.maxY = max(self.p1.y, self.p2.y)


class SeaFloor:
    def __init__(self, w: int, h: int):
        self.floor = []

        for y in range(h):
            row = []
            for x in range(w):
                row.append(0)
            self.floor.append(row)

    def addVentLine(self, ventLine: VentLine, allow45Diagonal: bool):
        ortho = False
        diag = False
        if (ventLine.p1.x != ventLine.p2.x) and (ventLine.p1.y != ventLine.p2.y):
            if not allow45Diagonal:
                return
            elif (ventLine.maxX - ventLine.minX) == (ventLine.maxY - ventLine.minY):
                diag = True
            else:
                return
        else:
            ortho = True

        if ortho:
            for x in range(ventLine.minX, ventLine.maxX+1):
                for y in range(ventLine.minY, ventLine.maxY+1):
                    self.floor[y][x] = self.floor[y][x]+1
        elif diag:
            xDelta = 1 if ventLine.p2.x > ventLine.p1.x else -1
            yDelta = 1 if ventLine.p2.y > ventLine.p1.y else -1
            for i in range(ventLine.maxX-ventLine.minX+1):
                x = ventLine.p1.x+i*xDelta
                y = ventLine.p1.y+i*yDelta
                self.floor[y][x] = self.floor[y][x]+1

    def countOverThreshold(self, threshold: int):
        count = 0
        for row in self.floor:
            for num in row:
                if num > threshold:
                    count += 1
        return count

    def toString(self):
        output = ""
        for row in self.floor:
            for num in row:
                output += "." if num == 0 else str(num)
            output += "\n"
        return output
