file = open("day3/data.txt", "r")
data = file.readlines()

maxBinaryLength = 0


def readBinary(input: str):
    global maxBinaryLength
    if len(input) > maxBinaryLength:
        maxBinaryLength = len(input)
    return int(input, 2)


binaryNums = list(map(readBinary, data))

onesCount = [0] * (maxBinaryLength-1)
for num in binaryNums:
    for i in range(0, maxBinaryLength, 1):
        if num & pow(2, i):
            onesCount[i] += 1

print(onesCount)

epsilon = 0
gamma = 0

threshold = len(binaryNums)/2

for i, count in enumerate(onesCount):
    if count > threshold:
        epsilon += pow(2, i)
    else:
        epsilon += pow(2, i)

print("epsilon {} * gamma {} = {}".format(epsilon, gamma, epsilon*gamma))
