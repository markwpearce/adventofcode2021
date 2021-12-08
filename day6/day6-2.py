import common as day6

initialData = day6.getData("day6/data.txt")


fishesAtStage = [0] * 9

for num in initialData:
    fishesAtStage[num] += 1

days = 256


print("Initial State: {} ".format(fishesAtStage))
for day in range(days):
    zeroFishes = fishesAtStage[0]
    for i, stage in enumerate(fishesAtStage):
        if i > 0:
            fishesAtStage[i-1] = fishesAtStage[i]
    fishesAtStage[6] += zeroFishes
    fishesAtStage[8] = zeroFishes

    print("After {} days: {} ({})".format(
        day+1, (fishesAtStage), sum(fishesAtStage)))
