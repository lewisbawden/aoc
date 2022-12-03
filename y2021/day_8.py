import aoc
import time


def day_8_part_1(data):
    return sum(d.count_usegs_in_output for d in data)


def day_8_part_2(data):
    for i, d in enumerate(data):
        d.solve()
    return sum(d.output() for d in data)


class Display:
    letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    numbers = [set('abcefg'), set('cf'), set('acdeg'), set('acdfg'), set('bcdf'), set('abdfg'), set('abdefg'), set('acf'), set('abcdefg'), set('abcdfg')]
    segs = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    usegs = [1, 4, 7, 8]

    def __init__(self, tens, fours):
        self.tens = tens
        self.fours = fours
        self.count_usegs_in_output = len(list(filter(lambda n: any(len(n) == self.segs[u] for u in self.usegs), self.fours)))

        self.segconv = {l: self.letters for l in sorted(self.letters)}

    def solve(self):
        tens = sorted(self.tens, key=lambda n: len(n))

        # '1' only contains two segments - could both be c or f
        self.segconv['c'] = set(list(filter(lambda n: len(n) == 2, tens))[0])
        self.segconv['f'] = set(list(filter(lambda n: len(n) == 2, tens))[0])

        # '7' contains '1' and one more segment - a is the remainder
        self.segconv['a'] = set(list(filter(lambda n: len(n) == 3, tens))[0]) - self.segconv['c']

        # '4' contains '1' and two more segments - these are b and d
        self.segconv['b'] = set(list(filter(lambda n: len(n) == 4, tens))[0]) - self.segconv['c']
        self.segconv['d'] = set(list(filter(lambda n: len(n) == 4, tens))[0]) - self.segconv['c']

        # '9' contains '7' and '4' and one more segment g
        gsegs = self.joinconv(['a', 'b', 'c'])
        glist = list(filter(lambda n: len(set(n) - gsegs) == 1 and len(n) == 6, tens))
        self.segconv['g'] = set(glist[0]) - gsegs

        # '8' contains '9' and one more segment e
        esegs = self.joinconv(['a', 'b', 'c', 'g'])
        elist = list(filter(lambda n: len(set(n) - esegs) == 1 and len(n) == 7, tens))
        self.segconv['e'] = set(elist[0]) - esegs

        # '0' contains b but not d
        dlist = list(filter(lambda n: len(n) == 6 and len(set(n) - self.segconv['d']) == 5, tens))
        self.segconv['b'] = set(dlist[0]) - self.joinconv(['a', 'c', 'e', 'g'])
        self.segconv['d'] -= self.segconv['b']

        # '6' contains c but not f
        clist = list(filter(lambda n: len(n) == 6 and len(set(n) - self.segconv['c']) == 5, tens))
        self.segconv['f'] = set(clist[0]) - self.joinconv(['a', 'b', 'd', 'e', 'g'])
        self.segconv['c'] -= self.segconv['f']

        # invert the lookup for converting numbers later
        self.decoder = {list(v)[0]: k for k, v in self.segconv.items()}

    def joinconv(self, ls):
        s = set()
        for l in ls:
            s = s.union(self.segconv[l])
        return s

    def decode(self, ls):
        s = set()
        for l in ls:
            s = s.union(self.decoder[l])
        return s

    def output(self):
        out = ''
        for f in self.fours:
            out += self.convert_to_digit(f)
        return int(out)

    def convert_to_digit(self, inp):
        s = self.decode(inp)
        for i, n in enumerate(self.numbers):
            if s == n:
                return f'{i}'


def parse_input(data):
    displays = []
    for line in data:
        s = line.split(' | ')
        displays.append(Display(s[0].split(), s[1].split()))
    return displays


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_8_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_8_part_1(parsed))
    print("Part 2:", day_8_part_2(parsed))

    print(time.time() - t0)
