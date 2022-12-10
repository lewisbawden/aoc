import aoc
import time


class CPU:
    def __init__(self):
        self.register = 1
        self.cycle = 0
        self.interesting = [20 + i*40 for i in range(6)]
        self.signal_strengths = []
        self.pixels = []

    def print(self):
        out = ['']
        for i, p in enumerate(self.pixels):
            out[-1] += p
            if (i + 1) % 40 == 0:
                out.append('')
        for line in out:
            print(line)

    def iterate(self, data):
        for line in data:
            args = line.split()
            if args[0] == 'noop':
                self.noop()
            elif args[0] == 'addx':
                self.addx(args[1])

    def draw_pixel(self):
        if abs(self.register - (self.cycle % 40)) < 2:
            pixel = '#'
        else:
            pixel = '.'
        self.pixels.append(pixel)

    def check_register(self):
        if self.cycle in self.interesting:
            self.signal_strengths.append(self.register*self.cycle)

    def addx(self, v):
        self.draw_pixel()
        self.cycle += 1
        self.check_register()
        self.draw_pixel()
        self.cycle += 1
        self.register += int(v)
        self.check_register()

    def noop(self):
        self.draw_pixel()
        self.cycle += 1
        self.check_register()


def day_10_part_1(data):
    cpu = CPU()
    cpu.iterate(data)
    return sum(cpu.signal_strengths)


def day_10_part_2(data):
    cpu = CPU()
    cpu.iterate(data)
    cpu.print()


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_10_data.txt")
    print("Part 1:", day_10_part_1(data))
    print("Part 2:", day_10_part_2(data))

    print(time.time() - t0)
