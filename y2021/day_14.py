import aoc
import time


def day_14_part_1(inp, rules, its):
    counter = get_init_count(inp, rules)
    for _ in range(its):
        counter = iterate_count(counter, rules)
    return get_output(counter)


def get_output(counter):
    length = sum(v for v in counter.values()) + 1
    letters = {}
    for a, b in counter.keys():
        letters[a] = letters.get(f'{a}', 0) + counter.get(f'{a}{b}', 0)
        letters[b] = letters.get(f'{b}', 0) + counter.get(f'{a}{b}', 0)
    for k in letters.keys():
        letters[k] = round(letters[k] / 2)

    return length, letters, max(letters.values()) - min(letters.values())


def iterate_count(counter, rules):
    it = {}
    for i in range(len(rules)):
        for j in range(len(rules)):
            jstr_in = rules[j][0]
            istr_out = rules[i][1]
            num_istr_in = counter[rules[i][0]]
            if (num_istr_in > 0 or i == j) and jstr_in in istr_out:
                it[rules[j][0]] = it.get(rules[j][0], 0) + num_istr_in
    out = {k: it.get(k, 0) for k in counter.keys()}
    return out


def get_init_count(inp, rules):
    out = {}
    for i, o in rules:
        inp_temp = inp[:]
        out[i] = 0
        while i in inp_temp:
            idx = inp_temp.find(i)
            out[i] += 1
            inp_temp = inp_temp[idx+1:]
    return out


def day_14_part_2(inp, rules, its):
    return day_14_part_1(inp, rules, its)


def parse_input(data):
    rules = []
    for l in data[2:]:
        i, o = l.split(' -> ')
        rules.append([i, ''.join([i[0], o, i[1]])])
    return data[0], rules


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_14_data.txt")
    parsed = parse_input(data)
    # print("Part 1:", day_14_part_1(*parsed, 10))
    print("Part 2:", day_14_part_2(*parsed, 40))

    print(time.time() - t0)
