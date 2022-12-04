import aoc
import time


def day_4_part_1(data):
    count = 0
    for p in data:
        p00, p01, p10, p11 = p[0][0], p[0][1], p[1][0], p[1][1]
        c1 = p10 <= p00 <= p11
        c2 = p10 <= p01 <= p11
        c3 = p00 <= p10 <= p01
        c4 = p00 <= p11 <= p01
        if (c1 and c2) or (c3 and c4):
            count += 1
    return count


def day_4_part_2(data):
    count = 0
    for p in data:
        p00, p01, p10, p11 = p[0][0], p[0][1], p[1][0], p[1][1]
        c1 = p10 <= p00 <= p11
        c2 = p10 <= p01 <= p11
        c3 = p00 <= p10 <= p01
        c4 = p00 <= p11 <= p01
        if (c1 or c2) or (c3 or c4):
            count += 1
    return count


def parse_input(data):
    return [[[int(p) for p in pair.split('-')] for pair in line.split(',')] for line in data]


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_4_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_4_part_1(parsed))
    print("Part 2:", day_4_part_2(parsed))

    print(time.time() - t0)
