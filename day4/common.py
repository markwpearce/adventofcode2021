

class BingoCard:
    def __init__(self, lines: list[str]):
        self.numbers = []
        self.complete = False
        for line in lines:
            self.numbers.append(list(map(int, line.split())))
        self.marked = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    def print(self):
        for i, line in enumerate(self.numbers):
            printLine = []
            for j, num in enumerate(line):
                if self.marked[i][j] == 1:
                    printLine.append("X")
                else:
                    printLine.append(num)
            print(*printLine, sep="  ")

    def mark(self, num: int):
        for i, line in enumerate(self.numbers):
            for j, cardNum in enumerate(line):
                if cardNum == num:
                    self.marked[i][j] = 1
        return self.test()

    def test(self):
        for line in self.marked:
            if line.count(1) == len(line):
                self.complete = True
                return True
        for i in range(0, len(self.marked)):
            count = 0
            for j in range(0, len(self.marked)):
                count += self.marked[j][i]
            if count == len(self.marked):
                self.complete = True
                return True
        return False

    def sumOfUnmarked(self):
        sum = 0
        for i in range(0, len(self.marked)):
            for j in range(0, len(self.marked)):
                if self.marked[i][j] == 0:
                    sum += self.numbers[i][j]
        return sum


def getCards(data: list[str]):
    cards = []
    cardData = []
    for i in range(1, len(data)):
        if data[i] == "\n" and len(cardData) > 0:
            cards.append(BingoCard(cardData))
            cardData = []
        elif data[i] != "\n":
            cardData.append(data[i])

    if len(cardData) > 0:
        cards.append(BingoCard(cardData))
        cardData = []
    return cards
