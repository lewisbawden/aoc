import aoc
import time
from re import match


class State:
    before_ta = 0
    in_ta = 1
    after_ta = 2


class Target:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def rel_to_target_area(self, r, axis):
        if axis == 0:
            if r < self.x1:
                return State.before_ta
            if r > self.x2:
                return State.after_ta
            if self.x1 <= r <= self.x2:
                return State.in_ta
        elif axis == 1:
            if r > self.y2:
                return State.before_ta
            if r < self.y1:
                return State.after_ta
            if self.y1 <= r <= self.y2:
                return State.in_ta


class Probe:
    def __init__(self, vx, vy, target):
        self.x0 = 0
        self.y0 = 0
        self.vx0 = vx
        self.vy0 = vy

        self.x = 0
        self.y = 0
        self.vx = vx
        self.vy = vy

        self.maxy = self.y
        self.target = target
        self.xstate = State.before_ta
        self.ystate = State.before_ta

    @property
    def in_ta(self):
        return self.xstate == State.in_ta and self.ystate == State.in_ta

    @property
    def before_ta(self):
        return self.xstate == State.before_ta and self.ystate == State.before_ta

    @property
    def after_ta(self):
        return self.xstate == State.after_ta or self.ystate == State.after_ta

    @property
    def drag(self):
        if self.vx > 0:
            return 1
        elif self.vx == 0:
            return 0
        else:
            return -1

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.maxy = max(self.y, self.maxy)
        self.vx -= self.drag
        self.vy -= 1
        self.xstate = self.target.rel_to_target_area(self.x, 0)
        self.ystate = self.target.rel_to_target_area(self.y, 1)

    def launch_to_target(self):
        while not self.after_ta:
            self.update()
            if self.in_ta:
                break
        return self.x, self.y, self.vx, self.vy, self.xstate, self.ystate


def day_17_part_1(target):
    p = get_max_velocity_probe(target)
    return p.vx0, p.vy0, p.maxy


def get_max_velocity_probe(target):
    vx, vy = 1, 1
    while True:
        p = Probe(vx, vy, target)
        p.launch_to_target()
        if p.xstate != State.before_ta:
            break
        vx += 1
    maxy = 0
    prev_p = p
    while True:
        p = Probe(vx, vy, target)
        p.launch_to_target()
        if prev_p.in_ta and not p.in_ta and vy > abs(target.y1 / 2):
            maxy = max(prev_p.maxy, maxy)
            break
        prev_p = p
        vy += 1
    return prev_p


def day_17_part_2(target):
    return get_all_possible_velocities(target)


def get_all_possible_velocities(target):
    count = 0
    vx, vy = 1, 1
    minvx, maxvx = 0, target.x2
    while True:
        p = Probe(vx, vy, target)
        p.launch_to_target()
        if p.xstate != State.before_ta:
            minvx = vx
            break
        vx += 1

    p = get_max_velocity_probe(target)
    maxvy = p.vy0
    minvy = target.y1
    for vx in range(minvx, maxvx + 1):
        for vy in range(minvy, maxvy + 1):
            p = Probe(vx, vy, target)
            p.launch_to_target()
            count += int(p.in_ta)
    return count


def parse_input(data):
    m = match('target area: x=(-*\d*)\.\.(-*\d*), y=(-*\d*)\.\.(-*\d*)', data[0])
    return Target(*[int(m.group(i)) for i in range(1,5)])


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_17_data.txt")
    parsed = parse_input(data)
    print("Part 1:", day_17_part_1(parsed))
    print("Part 2:", day_17_part_2(parsed))

    print(time.time() - t0)
