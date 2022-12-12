import aoc
import time
from heapq import *
from string import ascii_lowercase


def day_12_part_1(data):
    t = Traverser(*data)
    return t.traverse()


class Traverser:
    # Possible nearest neighbours
    nn = {(0, 1), (0, -1), (1, 0), (-1, 0)}

    def __init__(self, data, start, goal):
        self.data = data
        self.startx, self.starty = start
        self.extentx, self.extenty = len(data), len(data[0])
        self.goalx, self.goaly = goal
        self.queue = []
        self.nodes = {}

    def traverse(self):
        node = Node(0, 0, (self.startx, self.starty), None)
        self.nodes[node.coords] = node
        its = 0
        # Try the next possible direction - keep going until we reach the goal
        while node.coords != (self.goalx, self.goaly):
            self.push_valid_nn(node)
            node = heappop(self.queue)
            node.visited += 1
            its += 1
        return node.total

    def push_valid_nn(self, parnode):
        # Check all four neighbouring coordinates (if they do not overrun the grid)
        nns = list(filter(lambda c: 0 <= c[0] < self.extentx and 0 <= c[1] < self.extenty, ([parnode.coords[0]+di, parnode.coords[1]+dj] for di, dj in self.nn)))
        for ni, nj in nns:
            # Cannot go more than 1 height uphill
            if self.data[ni][nj] - parnode.score > 1:
                continue
            # Increment total by 1
            newnode = Node(self.data[ni][nj], parnode.total + 1, (ni, nj), parnode.coords)
            # If we have reached this node before (in keys), and we got there by a shorter route
            #   -> then no need to add it to the list of possible directions to try
            if newnode.coords in self.nodes.keys() and newnode.total >= self.nodes[newnode.coords].total:
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


def day_12_part_2(data):

    return None


def parse_input(data):
    heights = {s: i for i, s in enumerate(ascii_lowercase)}
    heights['E'] = 26
    heights['S'] = 0
    out = []
    for i, line in enumerate(data):
        row = []
        for j, c in enumerate(line):
            if c == 'S':
                start = (i, j)
            elif c == 'E':
                goal = (i, j)
            row.append(heights[c])
        out.append(row)
    return out, start, goal


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_12_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_12_part_1(parsed))
    print("Part 2:", day_12_part_2(parsed))

    print(time.time() - t0)
