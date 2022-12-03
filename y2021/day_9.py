import aoc
import time
import numpy as np
import itertools
from copy import deepcopy


def day_9_part_1(data):
    s = Sinks(data)
    s.get_sinks()
    return s.get_risk()


class Sinks:
    hor_ver = {(0, 1), (0, -1), (1, 0), (-1, 0)}

    def __init__(self, data):
        self.data = deepcopy(data)
        self.pad = np.zeros(shape=[d + 2 for d in self.data.shape])
        self.basin_sizes = deepcopy(self.pad[1:-1, 1:-1])
        self.basin_size_list = []
        self.pad += 10
        self.pad[1:-1, 1:-1] = deepcopy(self.data)

    def get_sinks(self):
        for i, j in itertools.product(*[range(d) for d in self.data.shape]):
            self.data[i, j] = self.is_sink(i + 1, j + 1)

    def is_sink(self, i, j):
        return int(all(self.pad[i, j] < self.pad[i + di, j + dj] for di, dj in self.hor_ver))

    def get_risk(self):
        self.risk = (self.data * self.pad[1:-1, 1:-1]) + self.data
        return self.risk.sum(axis=0).sum()

    def get_basin_sizes(self):
        for i, j in itertools.product(*[range(d) for d in self.data.shape]):
            if self.data[i, j] == 0:
                self.basin_sizes[i, j] = 0
                continue

            self.basin_sizes[i, j] = self.get_basin_size(i + 1, j + 1)
            self.basin_size_list.append(self.basin_sizes[i, j])
        return sorted(self.basin_size_list, reverse=True)

    def get_basin_size(self, i, j):
        if self.pad[i, j] >= 9:
            return 0

        count = 1
        self.pad[i, j] = 9
        for di, dj in self.hor_ver:
            count += self.get_basin_size(i + di, j + dj)
        return count


def day_9_part_2(data):
    s = Sinks(data)
    s.get_sinks()
    b = s.get_basin_sizes()
    return b[0] * b[1] * b[2]


def parse_input(data):
    return np.array([[int(i) for i in line] for line in data])


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_9_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_9_part_1(parsed))
    print("Part 2:", day_9_part_2(parsed))

    print(time.time() - t0)
