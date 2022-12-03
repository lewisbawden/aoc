import aoc
import time


def day_12_part_1(caves):
    c = CavePaths(caves, 1)
    c.get_paths(caves.get('start'), 'start')
    return len(c.paths)


def day_12_part_2(caves):
    c = CavePaths(caves, 2)
    c.get_paths(caves.get('start'), 'start')
    return len(c.paths)


class Cave:
    def __init__(self, i):
        self.name = i
        self.connections = list()
        self.paths = list()


class CavePaths:
    def __init__(self, caves, part):
        self.caves = caves
        self.paths = set()
        self.part = part

    def get_paths(self, cave: Cave, *args):
        inpath = list(args)
        if inpath[-1] == 'end':
            return self.paths.add(tuple(inpath))

        for conn in cave.connections:
            if not self.is_valid_connection(conn, inpath):
                continue
            self.get_paths(self.caves.get(conn), *inpath, conn)

    def is_valid_connection(self, conn, path):
        if conn == 'start':
            return False
        if conn.isupper():
            return True
        if self.part == 1 and conn in path:
            return False

        num = 0
        path_chars = {}
        for k in filter(lambda c: c.islower() and c != 'start', path):
            if k in path_chars.keys():
                path_chars[k] += 1
            else:
                path_chars[k] = 1
            if path_chars[k] >= 2:
                num += 1
            if num >= 2:
                return False
        return True


def parse_input(data):
    caves = {}
    for line in data:
        i, o = line.split('-')
        icave = caves.get(i, Cave(i))
        icave.connections.append(o)
        ocave = caves.get(o, Cave(o))
        ocave.connections.append(i)
        caves[i] = icave
        caves[o] = ocave
    return caves


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_12_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_12_part_1(parsed))
    print("Part 2:", day_12_part_2(parsed))

    print(time.time() - t0)
