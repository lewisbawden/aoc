import aoc
import time
import itertools
import operator


def day_16_part_1(data):
    b = Bits(data)
    b.parse_packet(0)
    return b.version_sum


def day_16_part_2(data):
    b = Bits(data)
    return b.parse_packet(0)


class Bits:
    def __init__(self, data):
        self.data = data[0]
        self.bin = ''.join(self.hex_to_bin(h) for h in self.data)
        self.version_sum = 0

        self.operators = {0: self.sum, 1: self.mul, 2: self.min, 3: self.max, 5: operator.gt, 6: operator.lt, 7: operator.eq}

    @staticmethod
    def mul(*v):
        operands = [1] + list(v)
        res = list(itertools.accumulate(operands, operator.mul))
        return res[-1]

    @staticmethod
    def sum(*v):
        return sum(v)

    @staticmethod
    def min(*v):
        return min(v)

    @staticmethod
    def max(*v):
        return max(v)

    @staticmethod
    def hex_to_bin(v):
        return f'{int(v, 16):b}'.zfill(4)

    @staticmethod
    def bin_to_dec(v):
        lenv = len(v)
        return sum(int(vi) * (2 ** (lenv - i - 1)) for i, vi in enumerate(v))

    def parse_packet(self, idx):
        version = self.bin_to_dec(self.bin[idx: idx + 3])
        tid = self.bin_to_dec(self.bin[idx + 3: idx + 6])
        self.version_sum += version

        result = None
        if tid != 4:
            operands = self.parse_operator(idx + 6)
            result = int(self.operators[tid](*operands))
        else:
            result = self.parse_literal(idx + 6)
        return result

    def parse_literal(self, idx):
        vals = []
        while self.bin[idx] != '0':
            vals.append(self.bin[idx + 1: idx + 5])
            idx += 5
        vals.append(self.bin[idx + 1: idx + 5])
        idx += 5

        self.idx = idx
        return self.bin_to_dec(''.join(vals))

    def parse_operator(self, idx):
        lid = self.bin[idx]
        subpackets = []
        if lid == '0':
            nbits = self.bin[idx + 1: idx + 16]
            nbits = self.bin_to_dec(nbits)
            idx += 16
            startidx = idx
            remaining_bits = nbits - (idx - startidx)
            while remaining_bits >= 11:
                res = self.parse_packet(idx)
                subpackets.append(res)
                idx = self.idx
                remaining_bits = nbits - (idx - startidx)
        elif lid == '1':
            nbits = 11
            nsubpackets = self.bin[idx + 1: idx + 1 + nbits]
            nsubpackets = self.bin_to_dec(nsubpackets)
            idx += nbits + 1
            while len(subpackets) < nsubpackets:
                res = self.parse_packet(idx)
                subpackets.append(res)
                idx = self.idx
        self.idx = idx
        return subpackets


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_16_data.txt")
    print("Part 1:", day_16_part_1(data))
    print("Part 2:", day_16_part_2(data))

    print(time.time() - t0)
