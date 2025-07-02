from collections import deque, defaultdict

from src.day16.day16 import find_position


def parse_grid(grid):
    return list(map(str.strip, grid.splitlines()))


def solve1(grid, max_cheat, target_saving):
    distances = get_distances(grid)
    shortcuts = defaultdict(int)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in distances:
                continue
            for cheat in range(2, max_cheat + 1):
                for dr in range(cheat + 1):
                    dc = cheat - dr
                    for r2, c2 in {
                        (r + dr, c + dc),
                        (r + dr, c - dc),
                        (r - dr, c + dc),
                        (r - dr, c - dc),
                    }:
                        if (r2, c2) not in distances:
                            continue
                        time_saved = distances[(r2, c2)] - distances[(r, c)] - cheat
                        if time_saved >= target_saving:
                            shortcuts[time_saved] += 1
    return sum(c for c in shortcuts.values())


def get_distances(grid):
    r, c = find_position(grid, "S")
    queue = deque([(r, c, 0)])
    distances = {}
    while queue:
        r, c, d = queue.popleft()
        if (r, c) in distances:
            continue
        distances[(r, c)] = d
        for nr, nc in [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]:
            if grid[nr][nc] != "#":
                queue.appendleft((nr, nc, d + 1))

    return distances


if __name__ == "__main__":
    with open("input", "r") as f:
        grid = parse_grid(f.read())
        print(solve1(grid, 20, 100))