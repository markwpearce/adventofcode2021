def getData(filename: str) -> list[int]:
    file = open(filename, "r")
    lines = file.readlines()
    return list(map(int, lines[0].split(',')))


class LanternFish:
    def __init__(self, timer: int = 9):
        self.timer = timer

    def tick(self) -> bool:
        if self.timer == 0:
            self.timer = 6
            return False
        else:
            self.timer -= 1
            if self.timer == 0:
                return True
            return False

    def __repr__(self):
        return str(self.timer)


def makeFish(nums: list[int]) -> list[LanternFish]:
    fish = []
    for num in nums:
        fish.append(LanternFish(num))
    return fish
