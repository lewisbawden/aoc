import aoc
import time


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = {}
        self.files = {}
        self.size = 0


class Browser:
    def __init__(self, limit):
        self.current = Dir('/', None)
        self.limit = limit
        self.above_limit = []
        self.avail = 0
        self.need = 0
        self.unused = 0
        self.min_req_size = 0

    def readall(self, lines):
        for line in lines:
            self.read(line)

    def cd_root(self):
        while self.current.parent is not None:
            self.current = self.current.parent

    def getsizes(self):
        self.cd_root()
        self.getsize(self.current)
        return sum(d.size for d in self.above_limit)

    def getsize(self, d):
        d.size = sum(d.files.values())
        for child in d.dirs.values():
            self.getsize(child)
            d.size += child.size
        if d.size < self.limit:
            self.above_limit.append(d)

    def read(self, line):
        if line == '$ cd ..':
            self.current = self.current.parent
        elif line == '$ cd /':
            self.cd_root()
        elif line.startswith('$ cd'):
            dirname = line.split()[-1]
            if dirname not in self.current.dirs.keys():
                self.current.dirs[dirname] = Dir(dirname, self.current)
            self.current = self.current.dirs[dirname]
        elif line.startswith('dir'):
            dirname = line.split()[-1]
            if dirname not in self.current.dirs.keys():
                self.current.dirs[dirname] = Dir(dirname, self.current)
        elif line != '$ ls':  # file
            size, name = line.split()
            self.current.files[name] = float(size)

    def find_space(self, d):
        for child in d.dirs.values():
            self.find_space(child)
        newsize = self.unused + d.size
        if newsize > self.need and d.size < self.min_req_size:
            self.min_req_size = d.size


def day_7_part_2(b):
    b.avail = 70000000
    b.need = 30000000
    b.min_req_size = 70000000
    b.cd_root()
    b.unused = b.avail - b.current.size
    b.find_space(b.current)
    return b.min_req_size


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_7_data.txt")
    b = Browser(100000)
    b.readall(data)
    size = b.getsizes()
    print("Part 1:", size)
    print("Part 2:", day_7_part_2(b))
    print(time.time() - t0)
