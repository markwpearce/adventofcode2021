
digitLookUp = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
}
knownDigitBySignalSize = [-1, -1, 1, 7, 4, -1, -1, 8]


class Readout:
    def __init__(self, input: str):
        self.parts = input.split("|")
        self.signals = self.parts[0].split()
        self.digits = self.parts[1].split()
        self.digitSize = list(map(len, self.digits))
        self.signalMap = [""]*10
        self.segmentMap = {"a": "", "b": "", "c": "",
                           "d": "", "e": "", "f": "", "g": ""}
        self.initMaps()
        self.number = self.getNum()

    def __repr__(self) -> str:
        return " ".join(self.signals) + " | "+" ".join(self.digits) + " ("+str(self.digitSize)+")"

    def getCountOfDigitSize(self, targetSizes: list[int]) -> int:
        count = 0
        for digitSize in self.digitSize:
            if digitSize in targetSizes:
                count += 1
        return count

    def initMaps(self):
        global knownDigitBySignalSize
        for signal in self.signals:
            knownDigit = knownDigitBySignalSize[len(signal)]
            if knownDigit != -1:
                self.signalMap[knownDigit] = signal

        found = []
        # diff between 7 & 1 gives "a"
        aMap = set(self.signalMap[7]).difference(set(self.signalMap[1]))
        self.segmentMap["a"] = list(aMap)[0]
        found.append(self.segmentMap["a"])

        # diff between 4 & 7 gives "b" and "d" in unknown order
        bAndDList = list(set(self.signalMap[4]).difference(
            set(self.signalMap[7])))

        assert len(bAndDList) == 2, "Cant find b & d possibilities " + \
            str(len(bAndDList))

        # D appears more than B
        firstCount = self.parts[0].count(bAndDList[0])
        secondCount = self.parts[0].count(bAndDList[1])
        if firstCount > secondCount:
            self.segmentMap["b"] = bAndDList[1]
            self.segmentMap["d"] = bAndDList[0]
        else:
            self.segmentMap["b"] = bAndDList[0]
            self.segmentMap["d"] = bAndDList[1]
        found += bAndDList

        # f appears more than c - can get this from 1
        firstCount = self.parts[0].count(self.signalMap[1][0])
        secondCount = self.parts[0].count(self.signalMap[1][1])
        if firstCount > secondCount:
            self.segmentMap["c"] = self.signalMap[1][1]
            self.segmentMap["f"] = self.signalMap[1][0]
        else:
            self.segmentMap["c"] = self.signalMap[1][0]
            self.segmentMap["f"] = self.signalMap[1][1]
        found += self.signalMap[1]

        notFoundYet = list(set("abcdefg")-set(found))
        assert len(notFoundYet) == 2, "Cant find e & g possibilities " + \
            str(len(notFoundYet))

        # g appears more than e - should only be 2 digits unaccounted for
        firstCount = self.parts[0].count(notFoundYet[0])
        secondCount = self.parts[0].count(notFoundYet[1])
        if firstCount > secondCount:
            self.segmentMap["e"] = notFoundYet[1]
            self.segmentMap["g"] = notFoundYet[0]
        else:
            self.segmentMap["e"] = notFoundYet[0]
            self.segmentMap["g"] = notFoundYet[1]
        found += notFoundYet
        self.segmentMap = {v: k for k, v in self.segmentMap.items()}

        print(self.segmentMap)

    def getNum(self) -> int:
        global knownDigitBySignalSize
        global digitLookUp
        number = 0
        for i, digit in enumerate(self.digits):
            digitSize = self.digitSize[i]
            digitVal = knownDigitBySignalSize[digitSize]
            if digitVal == -1:
                mappedDigit = []
                for letter in list(digit):
                    mappedDigit.append(self.segmentMap[letter])
                print(digit)
                print("".join(mappedDigit))
                mappedDigit.sort()
                print("sorted" + str(mappedDigit))
                digitVal = digitLookUp["".join(mappedDigit)]

            number += digitVal*pow(10, len(self.digits)-1-i)
        return number


def getData(filename: str, limit: int = -1) -> list[Readout]:
    file = open(filename, "r")
    lines = file.readlines()
    if limit != -1:
        lines = lines[:limit]
    return list(map(Readout, lines))
