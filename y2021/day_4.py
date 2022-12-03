import numpy as np
import aoc
import time


def day_4_part_1(nums, mats):
    w = get_next_winners(nums, mats, np.zeros(shape=mats.shape))
    return w.scores


def day_4_part_2(nums, mats):
    w = get_next_winners(nums, mats, np.zeros(shape=mats.shape))
    while w.loser_mats.shape[0] > 0:
        w = get_next_winners(w.remaining_nums, w.loser_mats, w.loser_mats_check)
    return w.scores


class WinnerOutput:
    def __init__(self, nums, mats, mats_check, winners, winning_num_idx):
        self.mats = mats
        self.mats_check = mats_check

        self.losers = list(filter(lambda n: n not in winners, range(mats.shape[0])))
        self.remaining_nums = nums[winning_num_idx + 1:]
        self.loser_mats = mats[self.losers, :, :]
        self.loser_mats_check = mats_check[self.losers, :, :]
        self.winners = winners
        self.winner_mats = mats[self.winners, :, :]
        self.winner_mats_check = mats_check[self.winners, :, :]
        self.winning_num = nums[winning_num_idx]

        self.scores = {wn: self.get_score(wn) for wn in self.winners}

    def get_score(self, wn):
        board_sum = self.mats[wn, :, :].sum(axis=0).sum()
        marked_sum = (self.mats_check[wn, :, :] * self.mats[wn, :, :]).sum(axis=0).sum()
        unmarked_sum = board_sum - marked_sum
        return self.winning_num * unmarked_sum


def get_next_winners(nums, mats, mats_check):
    i = 0
    winners = list()
    while len(winners) == 0:
        num_found = mats == nums[i]
        mats_check += num_found
        winners = check_winners(mats_check)
        i += 1

    return WinnerOutput(nums, mats, mats_check, winners, i - 1)


def check_winners(mats_check: np.array):
    winners = []
    for i in range(mats_check.shape[0]):
        mat = mats_check[i, :, :]
        if mat.max() == 0:
            continue
        if mat.sum(axis=0).sum() > mat.shape[0] and check_winner(mat):
            winners.append(i)
    return winners


def check_winner(mat):
    for i in range(mat.shape[0]):
        if mat[:, i].min() == 1 or mat[i, :].min() == 1:
            return True
    return False


def parse_input(data):
    nums = [int(i) for i in data[0].split(',')]
    mats = list()
    mat = list()

    for line in data[1:]:
        if len(line) == 0:
            if len(mat) != 0:
                mats.append(mat)
                mat = list()
            continue
        mat.append([int(i) for i in line.split()])

    if len(mat) != 0:
        mats.append(mat)
    return nums, np.array(mats)


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_4_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_4_part_1(*parsed))
    print("Part 2:", day_4_part_2(*parsed))

    print(time.time() - t0)
