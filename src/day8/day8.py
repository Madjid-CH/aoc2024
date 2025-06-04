from itertools import combinations, chain


def count_antinodes(input_):
    grid = parse_input(input_)
    frequencies = find_all_frequencies(grid)
    antinodes = antinodes_positions(frequencies, grid)
    antinodes = set(chain.from_iterable(antinodes.values()))
    return len(antinodes)


def parse_input(input_):
    lines = input_.splitlines()
    return [list(line) for line in lines]


def find_all_frequencies(grid):
    result = dict()
    for row, line in enumerate(grid):
        for col, c in enumerate(line):
            if c.isalnum():
                result[c] = result.get(c, set()).union({(row, col)})
    return result


def antinodes_positions(frequencies, grid):
    result = {k: set() for k in frequencies.keys()}
    for freq, antennas in frequencies.items():
        for pair in combinations(antennas, 2):
            result[freq].update(get_antinodes_positions2(pair, grid))
            result[freq].update(antennas)
    return result


def get_antinodes_positions(pair, grid):
    antenna1, antenna2 = pair
    x1, y1 = antenna1
    x2, y2 = antenna2
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if x1 < x2 and y1 < y2 or x1 > x2 and y1 > y2:
        antinode1 = min(x1, x2) - dx, min(y1, y2) - dy
        antinode2 = max(x1, x2) + dx, max(y1, y2) + dy
    else:
        antinode1 = min(x1, x2) - dx, max(y1, y2) + dy
        antinode2 = max(x1, x2) + dx, min(y1, y2) - dy
    ax1, ay1 = antinode1
    ax2, ay2 = antinode2
    result = set()
    if 0 <= ax1 < len(grid) and 0 <= ay1 < len(grid[0]):
        result.add(antinode1)
    if 0 <= ax2 < len(grid) and 0 <= ay2 < len(grid[0]):
        result.add(antinode2)
    return result


def get_antinodes_positions2(pair, grid):
    antenna1, antenna2 = pair
    x1, y1 = antenna1
    x2, y2 = antenna2
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    result = set()
    if x1 < x2 and y1 < y2 or x1 > x2 and y1 > y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        while x2 + dx < len(grid) and y2 + dy < len(grid[0]):
            antinode = x2 + dx, y2 + dy
            result.add(antinode)
            x1, x2 = x2, antinode[0]
            y1, y2 = y2, antinode[1]

        x1, y1 = antenna1
        x2, y2 = antenna2
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        while 0 <= x1 - dx and 0 <= y1 - dy:
            x1, x2 = x1 - dx, x1
            y1, y2 = y1 - dy, y1
            result.add((x1, y1))

    else:
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = max(y1, y2), min(y1, y2)
        while 0 <= x1 - dx and y1 + dy < len(grid[0]):
            x1, x2 = x1 - dx, x1
            y1, y2 = y1 + dy, y1
            result.add((x1, y1))

        x1, y1 = antenna1
        x2, y2 = antenna2
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = max(y1, y2), min(y1, y2)
        while x2 + dx < len(grid) and 0 <= y2 - dy:
            x1, x2 = x2, x2 + dx
            y1, y2 = y2, y2 - dy
            result.add((x2, y2))

    return result


if __name__ == "__main__":
    with open("input", "r") as f:
        print(count_antinodes(f.read()))
