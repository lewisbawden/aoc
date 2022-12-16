import aoc
import time
import numpy as np
test = r"""
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
""".split('\n')


def day_15_part_1(data):
    s, b = data
    d = (abs(s - b)).sum(axis=1)

    row = 10
    # row = 2000000
    not_allowed = set()
    for i in range(s.shape[0]):
        maxd = d[i] - abs(row - s[i, 1])
        if maxd < 0:
            continue
        start, end = s[i, 0] - maxd, s[i, 0] + maxd
        not_allowed.add(int(start))
        [not_allowed.add(j) for j in range(start, end)]
    return len(not_allowed)


def day_15_part_2(data):
    s, b = data
    d = (abs(s - b)).sum(axis=1)

    ulim = 4000000
    for i in range(s.shape[0]):
        print(i)
        for j in range(0, d[i] + 1):
            c1=(s[i, 0] - d[i] - 1 + j, s[i, 1] + j)
            c2=(s[i, 0] - d[i] - 1 + j, s[i, 1] - j)
            c3=(s[i, 0] + d[i] + 1 - j, s[i, 1] + j)
            c4=(s[i, 0] + d[i] + 1 - j, s[i, 1] - j)
            c = {c1, c2, c3, c4}
            for ci in c:
                valid = True
                if not ((0 <= ci[0] <= ulim) and (0 <= ci[1] <= ulim)):
                    continue
                for bi in range(s.shape[0]):
                    if bi == i:
                        continue
                    if abs(s[bi, 0] - ci[0]) + abs(s[bi, 1] - ci[1]) <= d[bi]:
                        valid = False
                        break
                if valid:
                    return ci[0] * 4000000 + ci[1]


def parse_input(data):
    replace = {'Sensor at x=': '', ': closest beacon is at x=': ',', ' y=': '', '\n': ''}
    bx, by, sx, sy = [], [], [], []
    for line in filter(lambda l: l != '', data):
        for k, v in replace.items():
            line = line.replace(k, v)
        vals = line.split(',')
        sx.append(int(vals[0]))
        sy.append(int(vals[1]))
        bx.append(int(vals[2]))
        by.append(int(vals[3]))
    s = np.array([[i, j] for i, j in zip(sx, sy)])
    b = np.array([[i, j] for i, j in zip(bx, by)])
    return s, b


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_15_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_15_part_1(parsed))
    print("Part 2:", day_15_part_2(parsed))

    print(time.time() - t0)
