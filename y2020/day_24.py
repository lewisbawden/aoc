import aoc
import time
import matplotlib.pyplot as plt

compass = {"ne": (0, 1), "e": (1, 1), "se": (1, 0), "sw": (0, -1), "w": (-1, -1), "nw": (-1, 0)}
sqrt3over2 = 0.86602540378


def day_24_part_1(lines):
    return len(first_tiles(lines))


def first_tiles(lines):
    tiles = set()
    for line in lines:
        i, j = 0, 0
        for cmd in line:
            i += compass[cmd][0]
            j += compass[cmd][1]
        if (i, j) in tiles:
            tiles.remove((i, j))
        else:
            tiles.add((i, j))
    return tiles


def hex_to_xy(i, j):
    return 0.5 * i + 0.5 * j, (-sqrt3over2) * i + sqrt3over2 * j


def day_24_part_2(lines):
    tiles = first_tiles(lines)
    for day in range(0, 100):
        debug_tiles(day, tiles, True, True)
        tiles = flip_tiles(tiles)
    return len(tiles)


def debug_tiles(day, tiles, doprint=False, doplot=False):
    if doprint:
        print(day, len(tiles))
    if doplot:
        fig, ax = plt.subplots()
        ax.scatter([hex_to_xy(*ij)[0] for ij in tiles],
                   [hex_to_xy(*ij)[1] for ij in tiles], c="black", marker="h", s=30)
        ax.set_aspect("equal")
        ax.grid(axis="both")
        plt.show()


def flip_tiles(tiles):
    black_to_flip = set()
    potential_white_to_flip = set()
    white_to_flip = set()

    def flip_tile(_black, _tile, _tiles):
        adjacent = {(_tile[0] + i, _tile[1] + j) for i, j in compass.values()}
        occupied = adjacent.intersection(_tiles)
        if not _black and len(occupied) == 2:  # white tiles must have two black neighbour tiles
            white_to_flip.add(_tile)
        if _black:
            potential_white_to_flip.update(adjacent.difference(occupied))  # add all white tiles around a black tile (to a set)
            if len(occupied) == 0 or len(occupied) > 2:  # black tile can be flipped
                black_to_flip.add(_tile)

    for tile in tiles:  # find all black tiles to flip, populate white tile checklist
        flip_tile(True, tile, tiles)
    for tile in potential_white_to_flip:  # remove potential white to flip that are disqualified
        flip_tile(False, tile, tiles)

    final_tiles = tiles.difference(black_to_flip)
    final_tiles.update(white_to_flip)
    return final_tiles


if __name__ == "__main__":
    t0 = time.time()

    data = aoc.load_data(r"day_24_data.txt")
    print(day_24_part_2([line.replace("e", "e ").replace("w", "w ").split() for line in data]))

    print(time.time() - t0)
