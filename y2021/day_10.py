import aoc
import time
from numpy import median


def day_10_part_1(data):
    c = Checker(data)
    return c.get_corrupt_score()


def day_10_part_2(data):
    c = Checker(data)
    return c.get_incomplete_score()


class Checker:
    corrupt_scoremap = {')': 3, ']': 57, '}': 1197, '>': 25137}
    incomplete_scoremap = {')': 1, ']': 2, '}': 3, '>': 4}
    charmap = {'(': ')', '[': ']', '{': '}', '<': '>'}

    def __init__(self, lines):
        self.lines = lines
        self.corrupt_scores = [0] * len(self.lines)
        self.incomplete_scores = []
        for lidx in range(len(self.lines)):
            self.check_line(lidx)

    def check_line(self, lidx):
        closes = [None]
        for c in self.lines[lidx]:
            if c in self.charmap.keys():
                closes.append(self.charmap[c])
            else:
                if c != closes.pop():
                    self.corrupt_scores[lidx] = self.corrupt_scoremap[c]
                    return

        if self.corrupt_scores[lidx] == 0:
            score = 0
            for i in range(1, len(closes)):
                score = (score * 5) + (self.incomplete_scoremap[closes[-i]])
            self.incomplete_scores.append(score)

    def get_corrupt_score(self):
        return sum(self.corrupt_scores)

    def get_incomplete_score(self):
        return median(self.incomplete_scores)


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_10_data.txt")
    print("Part 1:", day_10_part_1(data))
    print("Part 2:", day_10_part_2(data))

    print(time.time() - t0)
