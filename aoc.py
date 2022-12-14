import os
import requests
from dateutil.utils import today


def new_aoc_template(day=today().day, year=today().year):
    with open(f"y{year}\day_{day}_data.txt", "w") as f:
        puzzle_input = get_puzzle_input(day)
        f.write(puzzle_input)

    with open("aoc_template", "r") as temp_f:
        lines = temp_f.readlines()

    day_py = f"y{year}\day_{day}.py"
    if not os.path.exists(day_py):
        with open(day_py, "w") as new_f:
            for line in lines:
                new_f.write(rf'{line.replace("xx", str(day))}')


def get_puzzle_input(day=today().day):
    session_id = os.getenv('AOC_SID_2022')
    cookies = {'session': session_id}
    resp = requests.get(f'https://adventofcode.com/2022/day/{day}/input', cookies=cookies)
    resp.raise_for_status()
    return resp.text


def load_data(fstr):
    with open(fstr, "r") as f:
        return [line.rstrip('\n') for line in f.readlines()]


if __name__ == "__main__":
    new_aoc_template()