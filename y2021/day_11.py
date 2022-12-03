import itertools
import aoc
import time
import numpy as np


def day_11_part_1(data):
    o = OctGrid(data)
    o.do_steps(100)
    return o.flashes


def day_11_part_2(data):
    o = OctGrid(data)
    return o.get_sync()


class OctGrid:
    def __init__(self, data):
        self.octs = data
        self.flashers = np.ones(shape=self.octs.shape, dtype=np.int32)
        self.flashes = 0
        self.neighbours = {(i, j) for j in range(-1, 2) for i in range(-1, 2)}
        self.neighbours.remove((0, 0))

    def do_steps(self, steps):
        for _ in range(1, steps + 1):
            self.step()

    def get_sync(self):
        step = 0
        while self.octs.min() != self.octs.max():
            self.step()
            step += 1
        return step

    def step(self):
        self.octs += 1
        self.flashers = np.ones(shape=self.octs.shape, dtype=np.int32)
        to_flash = np.argwhere(self.octs > 9).tolist()
        for i, j in to_flash:
            self.flashers[i, j] = 0

        while len(to_flash) > 0:
            i, j = to_flash.pop(0)
            chain_flashers = self.do_flash(i, j)
            to_flash.extend(chain_flashers)

        self.flashes += len(np.argwhere(self.flashers == 0))
        self.octs *= self.flashers

    def do_flash(self, i, j):
        chain = []
        for m, n in self.neighbours:
            im, jn = i + m, j + n
            if 0 <= im < self.octs.shape[0] and 0 <= jn < self.octs.shape[1]:
                self.octs[im, jn] += 1
                if self.octs[im, jn] > 9 and self.flashers[im, jn] == 1:
                    self.flashers[im, jn] = 0
                    chain.append([im, jn])
        return chain


def parse_input(data):
    return np.array([[int(i) for i in line] for line in data])


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_11_data.txt")
    parsed = parse_input(data)
    # print("Part 1:", day_11_part_1(parsed))
    print("Part 2:", day_11_part_2(parsed))

    print(time.time() - t0)
