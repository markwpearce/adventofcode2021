import common as day4

file = open("day4/data.txt", "r")
data = file.readlines()

calledNums = list(map(int, data[0].split(",")))


cards = day4.getCards(data)

score = 0
winner = -1
for num in calledNums:
    for i, card in enumerate(cards):
        if card.mark(num):
            card.print()
            winner = i
            score = card.sumOfUnmarked()*num

            break

    if winner != -1:
        break

print(score)
