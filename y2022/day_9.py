import aoc
import time
import numpy as np

coords = {'U': np.array((0, 1)), 'D': np.array((0, -1)), 'L': np.array((-1, 0)), 'R': np.array((1, 0))}


class Rope:
    def __init__(self, n_knots=2):
        self.head = Head()
        sections = [self.head]
        for _ in range(n_knots-1):
            sections.append(Tail(sections[-1]))
        self.tails = sections[1:]
        self.visited = set()

    def move(self, d, n):
        for n in range(n):
            self.head.move(d)
            [tail.move() for tail in self.tails]
            self.visited.add(self.tails[-1].coords)

    def do_moves(self, moves):
        for move in moves:
            self.move(*move)
        return len(self.visited)


class Head:
    def __init__(self):
        self.pos = np.array((0, 0))

    def move(self, d):
        self.pos += coords[d]


class Tail:
    def __init__(self, head):
        self.pos = np.array((0, 0))
        self.head = head

    @property
    def coords(self):
        return self.pos[0], self.pos[1]

    def move(self):
        diff = self.head.pos - self.pos
        if (abs(diff) > 1).any():
            self.pos += np.sign(diff)


def day_9_part_1(data):
    rope = Rope()
    return rope.do_moves(data)


def day_9_part_2(data):
    rope = Rope(10)
    return rope.do_moves(data)


def parse_input(data):
    out = []
    for line in data:
        l, n = line.split()
        out.append((l, int(n)))
    return out


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_9_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_9_part_1(parsed))
    print("Part 2:", day_9_part_2(parsed))

    print(time.time() - t0)
