import aoc
import time
import string

test = r"""
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".split()


def day_3_part_1(data):
    priority = {l: i + 1 for i, l in enumerate(string.ascii_letters)}
    score = 0
    for bag in data:
        comp1, comp2 = set(bag[:int(len(bag)/2)]), set(bag[int(len(bag)/2):])
        common = comp1.intersection(comp2)
        score += priority[list(common)[0]]
    return score


def day_3_part_2(data):
    priority = {l: i + 1 for i, l in enumerate(string.ascii_letters)}
    score = 0
    group = 0
    while group < len(data):
        bag1, bag2, bag3 = set(data[group]), set(data[group+1]), set(data[group+2])
        common = bag1.intersection(bag2).intersection(bag3)
        score += priority[list(common)[0]]
        group += 3
    return score


def parse_input(data):

    return data


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_3_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_3_part_1(parsed))
    print("Part 2:", day_3_part_2(parsed))

    print(time.time() - t0)
