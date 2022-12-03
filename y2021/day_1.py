import aoc
import time


def day_1_part_1(data):
    return len(list(filter(lambda x: x[0] < x[1], zip(data[:-1], data[1:]))))


def day_1_part_2(data):
    n = 3
    return len(list(filter(lambda x: sum(data[x:x+n]) < sum(data[x+1:x+1+n]), range(len(data)-n))))


def parse_input(data):

    return list(int(i) for i in data)


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_1_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_1_part_1(parsed), round(time.time() - t0, 6))
    print("Part 2:", day_1_part_2(parsed), round(time.time() - t0, 6))
