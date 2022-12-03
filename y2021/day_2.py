import aoc
import time
import re

inp_re = re.compile('^(\w+) (\d+)$')


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, v):
        if isinstance(v, (int, float)):
            return Coord(self.x*v, self.y*v)

    def __add__(self, v):
        if isinstance(v, Coord):
            x = self.x + v.x
            y = self.y + v.y
        elif isinstance(v, (int, float)):
            x = self.x + v
            y = self.y + v
        return Coord(x, y)


class Submarine:
    dmap = {'forward': Coord(1, 0), 'down': Coord(0, 1), 'up': Coord(0, -1)}

    def __init__(self, x=0, y=0):
        self.pos = Coord(x, y)
        self.z = 0

    def parse(self, inp):
        m = inp_re.match(inp)
        direction, distance = m.group(1), int(m.group(2))
        return self.dmap[direction], distance

    def move(self, inp):
        coord, dist = self.parse(inp)
        self.pos += (coord * dist)
        self.z += (self.pos.y * dist) * coord.x


def day_2_part_1(data):
    sub = Submarine()
    [sub.move(inp) for inp in data]
    return sub.pos.x * sub.pos.y


def day_2_part_2(data):
    sub = Submarine()
    [sub.move(inp) for inp in data]
    return sub.pos.x * sub.z


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_2_data.txt")
    # print("Part 1:", day_2_part_1(data))
    print("Part 2:", day_2_part_2(data))

    print(time.time() - t0)
