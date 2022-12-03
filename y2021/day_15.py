import math

import aoc
import time
from heapq import *
import numpy as np


def day_15_part_1(data):
    t = Traverser(data)
    return t.traverse()


class Traverser:
    nn = {(0, 1), (0, -1), (1, 0), (-1, 0)}

    def __init__(self, data):
        self.data = data
        self.ulx, self.uly = len(self.data[0]), len(self.data)
        self.queue = []
        self.nodes = {}

    def traverse(self):
        node = Node(0, 0, (0, 0), (0, 0))
        self.nodes[node.coords] = node
        its = 0
        while node.coords != (self.ulx - 1, self.uly - 1):
            self.push_valid_nn(node)
            node = heappop(self.queue)
            node.visited += 1
            its += 1
        return its, node.total, len(list(filter(lambda n: n.visited > 0, self.nodes.values()))), len(self.nodes.values())

    def push_valid_nn(self, parnode):
        nns = list(filter(lambda c: 0 <= c[0] < self.ulx and 0 <= c[1] < self.uly, ([parnode.coords[0]+di, parnode.coords[1]+dj] for di, dj in self.nn)))
        for ni, nj in nns:
            new_total = self.data[ni][nj] + parnode.total
            score = ((self.ulx - ni) + (self.uly - nj)) + new_total
            newnode = Node(score, new_total, (ni, nj), parnode.coords)
            if newnode.coords in self.nodes.keys() and newnode.score >= self.nodes[newnode.coords].score:
                continue
            self.nodes[newnode.coords] = newnode
            heappush(self.queue, newnode)


class Node:
    def __init__(self, score, total, coords, parent):
        self.score = score
        self.total = total
        self.coords = coords
        self.parent = parent
        self.visited = 0

    def __lt__(self, other):
        return self.score < other.score

    def __le__(self, other):
        return self.score <= other.score


def day_15_part_2(data):
    new_data = expand_the_cave(data)
    t = Traverser(new_data)
    return t.traverse()


def expand_the_cave(data):
    olddata = np.array(data)
    newdata = np.zeros(shape=(olddata.shape[0]*5, olddata.shape[1]*5))
    x, y = olddata.shape
    for i in range(5):
        for j in range(5):
            newdata[x*i:x*(i+1), y*j:y*(j+1)] += olddata + i + j
            newdata[newdata >= 10] -= 9

    return newdata.tolist()


def parse_input(data):
    return [[int(i) for i in line] for line in data]


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_15_data.txt")
    parsed = parse_input(data)
    # print("Part 1:", day_15_part_1(parsed))
    print("Part 2:", day_15_part_2(parsed))

    print(time.time() - t0)
