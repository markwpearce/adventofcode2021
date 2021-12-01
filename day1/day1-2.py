file = open("day1/data.txt", "r")
data = file.readlines()
increases = -1
lastDepth = 0
for i, line in enumerate(data):
    if i < len(data)-2:
        currentDepth = int(data[i]) + int(data[i+1])+int(data[i+2])
    else:
        break

    print("{0} vs {1}".format(currentDepth, lastDepth))
    if currentDepth > lastDepth:
        increases += 1
    lastDepth = currentDepth

print(increases)
