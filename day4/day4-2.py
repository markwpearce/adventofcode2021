import common as day4

file = open("day4/data.txt", "r")
data = file.readlines()

calledNums = list(map(int, data[0].split(",")))


cards = day4.getCards(data)


def removeCompleteCards(card):
    return not card.complete


score = 0
for num in calledNums:
    if(len(cards) > 0):
        print(len(cards))
        for card in cards:
            if card.mark(num):
                print(num)
                card.print()
                score = card.sumOfUnmarked()*num
        cards = list(filter(removeCompleteCards, cards))

print(score)
