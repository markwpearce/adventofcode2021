file = open("day3/data.txt", "r")
data = file.readlines()

maxBinaryLength = 0


curIndex = 0
lookAtOpposite = False


def readBinary(input: str):
    global maxBinaryLength
    if len(input) > maxBinaryLength:
        maxBinaryLength = len(input)
    return int(input, 2)


def checkBinaryDigit(num):
    global curIndex
    global lookAtOpposite
    global onesCount
    global arrayInQuestion
    threshold = (len(arrayInQuestion)/2)
    print(curIndex)
    reverseFilter = lookAtOpposite
    if onesCount[curIndex] < threshold:
        reverseFilter = not reverseFilter
    print("onesCount[i]: {}, i: {} threshold: {} filterCheck {}".format(
        onesCount[curIndex], curIndex, threshold, reverseFilter))
    isMatch = bool((num & pow(2, curIndex)) > 0)
    if reverseFilter:
        isMatch = not isMatch
    print("num {} (2^i = {}) result:{}  isMatch? {}".format(
        num, pow(2, curIndex), (num & pow(2, curIndex)), isMatch))
    return isMatch


binaryNums = list(map(readBinary, data))

oxygen = binaryNums.copy()
print(oxygen)
print(maxBinaryLength)
onesCount = [0] * (maxBinaryLength-1)
print(onesCount)
arrayInQuestion = oxygen

for i in range(maxBinaryLength-2, -1, -1):
    print(oxygen)
    if len(oxygen) > 1:
        for num in oxygen:
            if num & pow(2, i):
                onesCount[i] += 1
        curIndex = i
        arrayInQuestion = oxygen
        oxygen = list(filter(checkBinaryDigit, oxygen))
    else:
        break


print(oxygen)
o2Gen = oxygen[0]


co2 = binaryNums.copy()
onesCount = [0] * (maxBinaryLength-1)


for i in range(maxBinaryLength-2, -1, -1):
    print(co2)
    if len(co2) > 1:
        for num in co2:
            if num & pow(2, i):
                onesCount[i] += 1
        curIndex = i
        lookAtOpposite = True
        arrayInQuestion = co2
        co2 = list(filter(checkBinaryDigit, co2))
    else:
        break

print(co2)
co2Scrub = co2[0]

print("o2 {} * co2 {} = {}".format(o2Gen, co2Scrub, o2Gen*co2Scrub))
