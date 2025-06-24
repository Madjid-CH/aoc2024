def compute_score(topographic_map):
    tmap = parse_topographic_map(topographic_map)
    trailheads = find_trailheads(tmap)
    result = 0
    for trailhead in trailheads:
        result += count_hiking_trails(tmap, trailhead)
    return result


def parse_topographic_map(tmap):
    tmap = [list(line) for line in tmap.splitlines()]
    for i, l in enumerate(tmap):
        for j, c in enumerate(l):
            tmap[i][j] = int(c) if c.isdigit() else -1
    return tmap


def find_trailheads(tmap):
    result = []
    for row, line in enumerate(tmap):
        for col, height in enumerate(line):
            if height == 0:
                result.append((row, col))
    return result


def count_hiking_trails(tmap, trailhead):
    up = (0, -1)
    down = (0, 1)
    left = (-1, 0)
    right = (1, 0)
    trails = {(0, trailhead)}
    while not all(height == 9 for height, _ in trails):
        for trail in list(trails):
            height, (x, y) = trail
            for dx, dy in (up, down, left, right):
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < len(tmap) and 0 <= new_y < len(tmap[0]):
                    if tmap[new_x][new_y] == height + 1:
                        trails.add((height + 1, (new_x, new_y)))
            if height != 9:
                trails.remove(trail)
    return len(trails)


def get_trailhead_rating(tmap, trailhead):
    up = (0, -1)
    down = (0, 1)
    left = (-1, 0)
    right = (1, 0)
    trails = [(0, trailhead)]
    while not all(height == 9 for height, _ in trails):
        for i, trail in enumerate(trails):
            height, (x, y) = trail
            for dx, dy in (up, down, left, right):
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < len(tmap) and 0 <= new_y < len(tmap[0]):
                    if tmap[new_x][new_y] == height + 1:
                        trails.append((height + 1, (new_x, new_y)))
            if height != 9:
                trails.pop(i)
    return len(trails)


def sum_ratings(tmap):
    tmap = parse_topographic_map(tmap)
    trailheads = find_trailheads(tmap)
    result = 0
    for trailhead in trailheads:
        result += get_trailhead_rating(tmap, trailhead)
    return result


if __name__ == "__main__":
    with open("input", "r") as f:
        print(sum_ratings(f.read()))