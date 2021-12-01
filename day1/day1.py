file = open("day1/data.txt", "r")
data = file.readlines()
increases = -1
lastDepth = 0
for line in data:
    currentDepth = int(line)
    print("{0} vs {1}".format(currentDepth, lastDepth))
    if currentDepth > lastDepth:
        increases += 1
    lastDepth = currentDepth

print(increases)
