import aoc
import time
from operator import add, sub, mul, truediv


class Monkey:
    ops = {'+': add, '-': sub, '*': mul, '/': truediv}

    def __init__(self, i):
        self.id = i
        self.items = []
        self.op = None
        self.operand = None
        self.test_val = 0
        self.throw_to_ids = None
        self.inspections = 0

    def inspect(self, item):
        self.inspections += 1
        if self.operand is not None:
            return self.op(item, self.operand)
        else:
            return self.op(item, item)

    def test(self, worry):
        return worry % self.test_val == 0

    def throw(self, item, monkeys):
        test = self.test(item)
        to_monkey = monkeys[self.throw_to_ids[test]]
        to_monkey.items.append(item)

    def throw_items(self, monkeys, gcd=None):
        while len(self.items) > 0:
            item = self.items.pop(0)
            new_item = self.inspect(item)
            # Part 1 or Part 2 if using Greatest Common Divisor
            if gcd is None:
                new_item = int(new_item / 3)
            else:
                new_item = new_item % gcd
            self.throw(new_item, monkeys)


def day_11_part_1(monkeys):
    n_rounds = 20
    for _ in range(n_rounds):
        for monkey in monkeys:
            monkey.throw_items(monkeys)

    most_active_monkeys = sorted(monkeys, key=lambda m: m.inspections)

    return most_active_monkeys[-2].inspections * most_active_monkeys[-1].inspections


def day_11_part_2(monkeys):
    n_rounds = 10000
    _t0 = time.time()

    def print_out(rn, _monkeys):
        print(f'== After round {rn} ==')
        for i in range(len(_monkeys)):
            print(f'Monkey {i} inspected items {_monkeys[i].inspections} times.')
        print(f'Duration: {time.time() - _t0}')

    # Prevent numbers from getting too large by providing the item modulo the GCD of all monkeys
    monkey_gcd = 1
    for monkey in monkeys:
        monkey_gcd *= monkey.test_val

    for n_round in range(n_rounds):
        # Check output on the test data by printing
        if n_round == 1 or n_round == 20:
            print_out(n_round, monkeys)
        if n_round % 1000 == 0 and n_round != 0:
            print_out(n_round, monkeys)

        for monkey in monkeys:
            monkey.throw_items(monkeys, monkey_gcd)

    most_active_monkeys = sorted(monkeys, key=lambda m: m.inspections)

    return most_active_monkeys[-2].inspections * most_active_monkeys[-1].inspections


def parse_input(data):
    i = 0
    monkeys = []
    while i < len(data):
        line1 = data[i].lstrip('Monkey').rstrip(':')
        line2 = data[i + 1].lstrip('Starting items:').split(',')
        line3 = data[i + 2].split()
        line4 = data[i + 3].split()[-1]
        line5 = data[i + 4].split()[-1]
        line6 = data[i + 5].split()[-1]

        m = Monkey(int(line1))
        m.items = [int(n) for n in line2]
        m.op = Monkey.ops[line3[-2]]
        m.operand = int(line3[-1]) if line3[-1].isnumeric() else None
        m.test_val = int(line4)
        m.throw_to_ids = {True: int(line5), False: int(line6)}

        monkeys.append(m)

        i += 7

    return monkeys


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_11_data.txt")
    parsed = parse_input(data)
    # print("Part 1:", day_11_part_1(parsed))
    print("Part 2:", day_11_part_2(parsed))

    print(time.time() - t0)
