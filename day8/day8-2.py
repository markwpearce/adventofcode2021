import common as day8


readouts = day8.getData("day8/data.txt")

count = 0
for ro in readouts:
    print(ro)
    count += ro.number

print(count)
