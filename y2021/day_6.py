import aoc
import time
from copy import deepcopy


def day_6_part_1(data, days):
    return do_days(data, days)


def do_days(data, days):
    for i in range(days):
        tmp = data[0]
        data[0] = data[1]
        data[1] = data[2]
        data[2] = data[3]
        data[3] = data[4]
        data[4] = data[5]
        data[5] = data[6]
        data[6] = data[7] + tmp
        data[7] = data[8]
        data[8] = tmp
    return sum(data)


def day_6_part_2(data, days):
    return do_days(data, days)


def parse_input(data):
    fish = list(map(lambda f: int(f), data[0].split(',')))
    fish_nums = []
    for i in range(9):
        count = len(list(filter(lambda f: f == i, fish)))
        fish_nums.append(count)
    return fish_nums


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_6_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_6_part_1(deepcopy(parsed), 80))
    print("Part 2:", day_6_part_2(deepcopy(parsed), 256))

    print(time.time() - t0)
