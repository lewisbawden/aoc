import aoc
import time


class Order(Exception):
    def __init__(self, *args):
        self.msg = args[0]
        self.value = args[1]


def day_13_part_1(data):
    total = 0
    pair_n = 0
    for i in range(0, len(data), 2):
        pair_n += 1
        p1 = data[i]
        p2 = data[i+1]
        try:
            result = compare(p1, p2)
        except Order as ex:
            result = ex.value
        print(result, pair_n)
        if result:
            total += pair_n
    return total


class Packet:
    def __init__(self, line):
        self.line = line

    def __lt__(self, other):
        try:
            result = compare(self.line, other.line)
        except Order as ex:
            result = ex.value
        return result


def compare(p1, p2):
    if isinstance(p1, list) and isinstance(p2, list):
        for p1i, p2i in zip(p1, p2):
            compare(p1i, p2i)
        if len(p1) < len(p2):
            raise Order('Right Order', True)
        elif len(p1) > len(p2):
            raise Order('Wrong Order', False)
    elif isinstance(p1, int) and isinstance(p2, int):
        if p1 < p2:
            raise Order('Right Order', True)
        elif p1 > p2:
            raise Order('Wrong Order', False)
    elif isinstance(p1, list) and isinstance(p2, int):
        return compare(p1, [p2])
    elif isinstance(p1, int) and isinstance(p2, list):
        return compare([p1], p2)


def day_13_part_2(data):
    data.append([[2]])
    data.append([[6]])
    out = [Packet(line) for line in data]
    out = [p.line for p in sorted(out)]
    i, j = 0, 0
    for idx, line in enumerate(out):
        if line == [[2]]:
            i = idx + 1
        elif line == [[6]]:
            j = idx + 1
            break
    return i * j


def parse_input(data):
    out = []
    for line in data:
        if line != '' and line != '\n':
            out.append(eval(line))
    return out


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_13_data.txt")
    parsed = parse_input(data)

    print("Part 1:", day_13_part_1(parsed))
    print("Part 2:", day_13_part_2(parsed))

    print(time.time() - t0)
