file = open("day2/data.txt", "r")
data = file.readlines()


class Instruction:
    def __init__(self, line: str):
        parts = line.split()
        self.direction = parts[0]
        self.amount = int(parts[1])


def makeInstruction(line: str):
    return Instruction(line)


instructions = map(makeInstruction, data)

horizontal = 0
depth = 0
aim = 0


for instruction in instructions:
    if instruction.direction == "forward":
        horizontal += instruction.amount
        depth += aim*instruction.amount
    elif instruction.direction == "up":
        # depth -= instruction.amount
        aim -= instruction.amount
    elif instruction.direction == "down":
        # depth += instruction.amount
        aim += instruction.amount


print("Horizontal {} * depth {} = {}".format(horizontal, depth, horizontal*depth))
