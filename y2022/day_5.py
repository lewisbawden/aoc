import aoc
import time


def day_5_part_1(data):
    stacks, instructions = data
    for (num, fr, to) in instructions:
        for _ in range(num):
            item = stacks[fr-1].pop()
            stacks[to-1].append(item)
    return ''.join([s[-1] for s in stacks])


def day_5_part_2(data):
    stacks, instructions = data
    for (num, fr, to) in instructions:
        item = stacks[fr - 1][-num:]
        stacks[fr - 1] = stacks[fr - 1][:-num]
        stacks[to - 1].extend(item)
    return ''.join([s[-1] for s in stacks])


def parse_input(data):
    n_stacks = 9
    line_crates_end = 8
    stacks = [list() for _ in range(n_stacks)]
    for line in reversed(data[0:line_crates_end]):
        for i in range(n_stacks):
            if line[1+i*4] != ' ':
                stacks[i].append(line[1+i*4])

    instructions = []
    for line in data[line_crates_end+2:]:
        instructions.append([int(item) for item in line.split() if item.isnumeric()])

    return stacks, instructions


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_5_data.txt")
    parsed = parse_input(data)
    # print("Part 1:", day_5_part_1(parsed))
    print("Part 2:", day_5_part_2(parsed))

    print(time.time() - t0)
