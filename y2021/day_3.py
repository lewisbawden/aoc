import aoc
import time
import numpy as np
from operator import ge, gt, eq, ne


def day_3_part_1(data):
    gamma_b = data.sum(axis=0) // (data.shape[0] / 2)
    beta_b = 0 ** gamma_b
    gamma = bin_conv(gamma_b)
    beta = bin_conv(beta_b)
    return gamma * beta


def bin_conv(b):
    bin_array = np.array([2 ** i for i in range(b.size - 1, -1, -1)])
    return (b * bin_array).sum()


def day_3_part_2(data):
    O2 = find_rating(data, 'O2')
    CO2 = find_rating(data, 'CO2')
    return O2 * CO2


def find_rating(data, mode):
    op = {'O2': eq, 'CO2': ne}.get(mode)
    col = 0
    while True:
        coldata = data[:, col]
        mc = int(ge(coldata.sum(), coldata.size / 2))
        keep = op(coldata, mc)
        data = data[keep, :]
        if data.shape[0] == 1:
            return bin_conv(data[0, :])
        col += 1


def parse_input(data):
    return np.array([[int(i) for i in line] for line in data])


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_3_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_3_part_1(parsed))
    print("Part 2:", day_3_part_2(parsed))

    print(time.time() - t0)
