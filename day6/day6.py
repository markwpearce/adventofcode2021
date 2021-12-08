import common as day6


fishes = day6.makeFish(day6.getData("day6/data.txt"))

days = 256
fishToAdd = 0
print("Initial State: {} ".format(fishes))
for day in range(days):
    if fishToAdd > 0:
        for _ in range(0, fishToAdd):
            fishes.append(day6.LanternFish())
    fishToAdd = 0
    for fish in fishes:
        if fish.tick():
            fishToAdd += 1

    print("After {} days: {} ".format(day+1, len(fishes)))
