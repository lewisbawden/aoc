import aoc
import time
import numpy as np

test = r"""
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
""".split('\n')


class Block:
    start = -1
    empty = 0
    sand = 1
    rock = 2


def day_14_part_1(data):
    i = 0
    try:
        while True:
            data = drop_sand(data)
            # printcave(data[0])
            i += 1
    except IndexError:
        printcave(data[0])
    return i


class SAANDERROR(Exception):
    """SAAAND"""


def drop_sand(data):
    cave, x1, x2, y1, y2 = data
    i, j = (500, 0)
    while True:
        # printcave(cave)
        if cave[i - x1, j - y1 + 1] == Block.empty:
            j += 1
        elif cave[i - x1 - 1, j - y1 + 1] == Block.empty:
            if i - x1 - 1 < 0:
                raise IndexError('Python can handle -1 in an array urgh')
            i -= 1
        elif cave[i - x1 + 1, j - y1 + 1] == Block.empty:
            i += 1
        elif cave[i - x1, j - y1] == Block.empty:
            cave[i - x1, j - y1] = Block.sand
            break
        elif cave[i - x1 + 1, j - y1 + 1] == cave[i - x1 - 1, j - y1 + 1] == Block.sand:
            raise SAANDERROR("(Sand: toomuch")
    return cave, x1, x2, y1, y2


def expand_cave(data):
    cave = data[0]
    newcave = np.zeros(shape=(cave.shape[0] + 2, cave.shape[1]))
    newcave[1:-1, :] = data[0]
    seg = newcave[:, -1]
    newcave[:, -1] = np.ones(shape=seg.shape) * Block.rock
    return newcave, data[1] - 1, data[2] + 1, data[3], data[4]


def day_14_part_2(data):
    newcave = np.zeros(shape=(data[0].shape[0], data[0].shape[1] + 2))
    seg = newcave[:, -1]
    newcave[:, -1] = np.ones(shape=seg.shape) * Block.rock
    newcave[:, :-2] = data[0]
    data = (newcave, data[1], data[2], data[3], data[4] + 2)
    try:
        while True:
            try:
                # printcave(data[0])
                data = drop_sand(data)
            except IndexError:
                data = expand_cave(data)
    except SAANDERROR:
        sands = 0 ** abs(data[0] - Block.sand)
        totalsand = sands.sum()
    printcave(data[0])
    return totalsand + 1


def printcave(cave):
    convert = {Block.rock: '#', Block.start: '+', Block.empty: '.', Block.sand: 'o'}
    for i in range(cave.shape[1]):
        for j in range(cave.shape[0]):
            print(convert[cave[j, i]], end='')
        print()


def parse_input(data):
    rocks = []
    x1, x2, y1, y2 = 9999999, -1, 0, -1
    for line in data:
        line = line.rstrip('\n')
        if line == '':
            continue
        rock = []
        coords = line.split(' -> ')
        for coord in coords:
            i = int(coord.split(',')[0])
            j = int(coord.split(',')[1])
            x1 = min(x1, i)
            x2 = max(x2, i)
            y1 = min(y1, j)
            y2 = max(y2, j)
            rock.append((i, j))
        rocks.append(rock)

    cave = np.zeros(shape=((x2-x1 + 1), (y2-y1 + 1)))
    cave[500-x1, 0-y1] = Block.start
    for rock in rocks:
        ip, jp = None, None
        for i, j in rock:
            cave[i-x1, j-y1] = Block.rock
            if ip is not None:
                if ip == i:
                    l, u = (j - y1, jp - y1) if j < jp else (jp - y1, j - y1)
                    seg = cave[i - x1, l: u]
                    cave[i - x1, l: u] = np.ones(shape=seg.shape) * Block.rock
                else:
                    l, u = (i - x1, ip - x1) if i < ip else (ip - x1, i - x1)
                    seg = cave[l: u, j - y1]
                    cave[l: u, j - y1] = np.ones(shape=seg.shape) * Block.rock
            ip, jp = i, j
    printcave(cave)
    return cave, x1, x2, y1, y2


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_14_data.txt")
    parsed = parse_input(data)
    # print("Part 1:", day_14_part_1(parsed))
    print("Part 2:", day_14_part_2(parsed))

    print(time.time() - t0)
