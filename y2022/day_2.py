import aoc
import time


def day_2_part_1(data):
    roundscore = {'A': {'X': 3, 'Y': 6, 'Z': 0},
                  'B': {'X': 0, 'Y': 3, 'Z': 6},
                  'C': {'X': 6, 'Y': 0, 'Z': 3}}
    handscore = {'X': 1, 'Y': 2, 'Z': 3}
    score = 0
    for r in data:
        score += roundscore[r[0]][r[2]]
        score += handscore[r[2]]
    return score


def day_2_part_2(data):
    roundscore = {'A': {'X': 3, 'Y': 1, 'Z': 2},
                  'B': {'X': 1, 'Y': 2, 'Z': 3},
                  'C': {'X': 2, 'Y': 3, 'Z': 1}}
    handscore = {'X': 0, 'Y': 3, 'Z': 6}
    score = 0
    for r in data:
        score += roundscore[r[0]][r[2]]
        score += handscore[r[2]]
    return score


def parse_input(data):

    return data


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_2_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_2_part_1(parsed))
    print("Part 2:", day_2_part_2(parsed))

    print(time.time() - t0)
