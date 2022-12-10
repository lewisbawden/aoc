import aoc
import time


class Dir:
    def __init__(self, name, parent):
        self.name = name  # string with the name of this Directory object
        self.parent = parent  # Dir referring to the parent, for going up a level
        self.dirs = {}  # dictionary with keys: values s.t. {'dirname': reference to another Dir object, ...}
        self.files = {}  # dictionary s.t. {'filename': size as a float, ...}
        self.size = 0  # size is the full directory size including all contents in children Dir objects


class Browser:
    def __init__(self, limit):
        # Initialise parameters, and initialise a root directory which has no parent
        # self.current refers to the node currently being visited (the current working directory)
        self.current = Dir('/', None)
        self.limit = limit
        self.above_limit = []
        self.avail = 0
        self.need = 0
        self.unused = 0
        self.min_req_size = 0

    def readall(self, lines):
        # Parse the lines one by one performing a relevant command
        for line in lines:
            self.read(line)

    def cd_root(self):
        # The root directory is the only one with no parent - so keep going up until the current node has no parent
        while self.current.parent is not None:
            self.current = self.current.parent

    def getsizes(self):
        # starting from the root node, get the size of each directory
        # Getting a directories size requires knowing the size of any directories inside - so do this recursively
        self.cd_root()
        self.getsize(self.current)
        return sum(d.size for d in self.above_limit)

    def getsize(self, d):
        # directory size is the sum of all files, and the sum of all contents in all child folders
        d.size = sum(d.files.values())
        for child in d.dirs.values():
            # use the .getsize function to get the size of each child folder
            self.getsize(child)
            # add the size of the child to the directory being evaluated
            d.size += child.size
        if d.size < self.limit:
            self.above_limit.append(d)

    def read(self, line):
        if line == '$ cd ..':
            # set the current directory to its parent (go up one level)
            self.current = self.current.parent
        elif line == '$ cd /':
            # go up a level until root is reached
            self.cd_root()
        elif line.startswith('$ cd'):
            # change to a directory with this name
            dirname = line.split()[-1]
            # add it as a new directory with self.current as the parent if it doesn't exist
            if dirname not in self.current.dirs.keys():
                self.current.dirs[dirname] = Dir(dirname, self.current)
            # change to it by setting the current directory to the Dir object with that name
            self.current = self.current.dirs[dirname]
        elif line.startswith('dir'):
            # add the directory to the list of directories if it doesn't exist yet
            dirname = line.split()[-1]
            if dirname not in self.current.dirs.keys():
                self.current.dirs[dirname] = Dir(dirname, self.current)
        elif line != '$ ls':
            # save file to the dictionary of files
            size, name = line.split()
            self.current.files[name] = float(size)

    def find_space(self, d):
        # Check the space gained from deleting this - need to know the space gained from each child
        for child in d.dirs.values():
            # check the space gained from each child using .find_space recursively
            self.find_space(child)
        # check if the space gained is enough
        newsize = self.unused + d.size
        if newsize > self.need and d.size < self.min_req_size:
            # if its enough, and its smaller than the current minimum, update the best answer so far
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
