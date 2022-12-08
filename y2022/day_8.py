import aoc
import time
import numpy as np


def day_8_part_1(data):
    rows = data.shape[0]
    cols = data.shape[1]
    count = 0

    def is_visible(a: np.array):
        return (a < 0).all()

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            left = data[i, 0:j] - data[i, j]
            right = data[i, j+1:cols] - data[i, j]
            up = data[0:i, j] - data[i, j]
            down = data[i+1:rows, j] - data[i, j]
            visible = any(is_visible(d) for d in [left, right, up, down])
            count += int(visible)

    edge_trees = 2*rows + 2*cols - 4

    return count + edge_trees


def day_8_part_2(data):
    rows = data.shape[0]
    cols = data.shape[1]

    def view_distance(a: np.array, height: int):
        count = 0
        for tree in a:
            count += 1
            if tree >= height:
                break
        return count

    scores = np.ones(shape=data.shape)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            left = data[i, 0:j]
            right = data[i, j + 1:cols]
            up = data[0:i, j]
            down = data[i + 1:rows, j]
            for a in [reversed(left), right, reversed(up), down]:
                scores[i, j] *= view_distance(a, data[i, j])
    argmax = np.argmax(scores)
    score = scores.ravel()[argmax]
    return score


def parse_input(data):
    trees = np.array([[int(i) for i in line] for line in data])
    return trees


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_8_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_8_part_1(parsed))
    print("Part 2:", day_8_part_2(parsed))

    print(time.time() - t0)
