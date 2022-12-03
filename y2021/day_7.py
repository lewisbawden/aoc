import aoc
import time
import numpy as np


def day_7_part_1(data):
    diffs = get_differences(data)
    return get_best_position(diffs)


def get_differences(data):
    max_crab = max(data)
    min_crab = min(data)
    arr = np.array([data for _ in range(min_crab, max_crab + 1)])
    arr_rep = np.array([[i for _ in range(len(data))] for i in range(min_crab, max_crab + 1)])
    return abs(arr_rep - arr)


def get_best_position(diffs):
    diffs_sum = diffs.sum(axis=1)
    m = np.argmin(diffs_sum)
    return m, diffs_sum[m]


def day_7_part_2(data):
    diffs = get_differences(data)
    convert_to_actual_crab_fuel = np.vectorize(lambda n: n * (n + 1) / 2)
    actual_crab_fuel = convert_to_actual_crab_fuel(diffs)
    return get_best_position(actual_crab_fuel)


def parse_input(data):
    return list(map(lambda f: int(f), data[0].split(',')))


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_7_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_7_part_1(parsed))
    print("Part 2:", day_7_part_2(parsed))

    print(time.time() - t0)
