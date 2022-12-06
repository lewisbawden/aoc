import aoc
import time


def day_6_part_1(data):
    n = 4
    for i in range(n, len(data)):
        if len(set(data[i - n:i])) == n:
            return i


def day_6_part_2(data):
    n = 14
    for i in range(n, len(data)):
        if len(set(data[i - n:i])) == n:
            return i


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_6_data.txt")
    print("Part 1:", day_6_part_1(data[0]))
    print("Part 2:", day_6_part_2(data[0]))

    print(time.time() - t0)
