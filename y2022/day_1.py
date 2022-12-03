import aoc
import time


def day_1_part_1(data):
    return max(sum(elf) for elf in data)


def day_1_part_2(data):
    return sum(sorted(sum(elf) for elf in data)[-3:])


def parse_input(data):
    elves = []
    foods = []
    for food in data:
        if food == '':
            elves.append(foods)
            foods = []
        else:
            foods.append(int(food))
    return elves


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_1_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_1_part_1(parsed))
    print("Part 2:", day_1_part_2(parsed))

    print(time.time() - t0)
