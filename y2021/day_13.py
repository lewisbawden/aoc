import numpy as np

import aoc
import time


def day_13_part_1(data):
    folds, arr = data
    arr = fold(arr, *(folds[0]))
    return (0 ** (0 ** arr)).sum(axis=1).sum()


def day_13_part_2(data):
    folds, arr = data
    for f in folds:
        arr = fold(arr, *f)
    show(arr)


def show(arr):
    a = 0 ** arr
    a = np.array2string(a.T)
    print(a.replace('\n', '').replace(']', '\n').replace('0.', '#').replace('1.', '.'))


def fold(arr, axis, point):
    if axis == 0:
        for i in range(point):
            arr[i, :] += arr[-i-1, :]
        arr = arr[:point, :]
    elif axis == 1:
        for i in range(point):
            arr[:, i] += arr[:, -i-1]
        arr = arr[:, :point]
    return arr


def parse_input(data):
    dots = []
    for idx, line in enumerate(data):
        if ',' in line:
            dots.append([int(i) for i in line.split(',')])
        else:
            break
    folds = []
    for line in data[idx+1:]:
        f, i = line.split('=')
        folds.append([int('y' in f), int(i)])

    xmax = max(dots, key=lambda c: c[0])[0]
    ymax = max(dots, key=lambda c: c[1])[1]

    arr = np.zeros(shape=(xmax + 1, ymax + 1))
    for m, n in dots:
        arr[m][n] = 1

    return folds, arr


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_13_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_13_part_1(parsed))
    print("Part 2:", day_13_part_2(parsed))

    print(time.time() - t0)
