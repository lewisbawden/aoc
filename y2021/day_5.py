import aoc
import time
import numpy as np
import re


def day_5_part_1(data):
    grid = fill_horizontal_vertical_vents(data)
    return count_twos(grid)


def fill_horizontal_vertical_vents(data):
    grid = np.zeros(shape=(data.max() + 1, data.max() + 1))
    for r in range(data.shape[0]):
        idxs = [[], []]
        for c in range(data.shape[1]):
            if data[r, 0, c] == data[r, 1, c]:
                idxs[c] = data[r, 0, c]
                idxs[0 ** c] = get_seq(*data[r, :, 0 ** c])
                grid[idxs] += 1
    return grid


def count_twos(grid):
    apply_count_twos = np.vectorize(lambda x: 1 if x >= 2 else 0)
    twos = apply_count_twos(grid)
    return twos.sum()


def day_5_part_2(data):
    grid = fill_horizontal_vertical_vents(data)
    grid += fill_diagonal_vents(data)
    return count_twos(grid)


def fill_diagonal_vents(data):
    grid = np.zeros(shape=(data.max() + 1, data.max() + 1))
    for r in range(data.shape[0]):
        idxs = [[], []]
        if data[r, 0, 0] != data[r, 1, 0] and data[r, 0, 1] != data[r, 1, 1]:
            idxs[0] = get_seq(*data[r, :, 0])
            idxs[1] = get_seq(*data[r, :, 1])
            grid[idxs] += 1
    return grid


def get_seq(c1, c2):
    sign = (-1) ** int(c1 > c2)
    return list(range(c1, c2 + sign, sign))


def parse_input(data):
    coords = list(map(parse_line, data))
    return np.array(coords)


p = re.compile('^(\d+),(\d+) -> (\d+),(\d+)$')
def parse_line(line):
    m = p.match(line)
    return [[int(m.group(1)), int(m.group(2))], [int(m.group(3)), int(m.group(4))]]


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_5_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_5_part_1(parsed))
    print("Part 2:", day_5_part_2(parsed))

    print(time.time() - t0)
