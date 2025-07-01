import heapq


def parse_maze(maze):
    return [list(row) for row in maze.splitlines()]


def get_cost(maze):
    start = find_position(maze, "S")
    queue = [(0, *start, 0, 1)]
    seen = {(*start, 0, 1)}
    while queue:
        cost, r, c, dr, dc = heapq.heappop(queue)
        seen.add((r, c, dr, dc))
        if maze[r][c] == "E":
            return cost
        if maze[r + dr][c + dc] != "#" and (r + dr, c + dc, dr, dc) not in seen:
            heapq.heappush(queue, (cost + 1, r + dr, c + dc, dr, dc))
        for ndr, ndc in ((-dc, dr), (dc, -dr)):
            if (r, c, ndr, ndc) not in seen and maze[r + ndr][c + ndc] != "#":
                heapq.heappush(queue, (cost + 1000, r, c, ndr, ndc))
    assert False


def find_position(maze, pos="S"):
    for r, row in enumerate(maze):
        for c, val in enumerate(row):
            if val == pos:
                return r, c
    assert False, "No position found"


def count_tiles(maze):
    start = find_position(maze, "S")
    queue = [(0, *start, 0, 1, [start])]
    seen = {(*start, 0, 1)}
    best_cost = float("inf")
    tiles = set()

    while queue:
        cost, r, c, dr, dc, path = heapq.heappop(queue)
        seen.add((r, c, dr, dc))
        if maze[r][c] == "E":
            if cost <= best_cost:
                best_cost = cost  # it will get updated once
                for tile in path:
                    tiles.add(tile)
            else:
                break
        if maze[r + dr][c + dc] != "#" and (r + dr, c + dc, dr, dc) not in seen:
            heapq.heappush(
                queue, (cost + 1, r + dr, c + dc, dr, dc, path + [(r + dr, c + dc)])
            )
        for ndr, ndc in [(-dc, dr), (dc, -dr)]:
            if (r, c, ndr, ndc) not in seen and maze[r + ndr][c + ndc] != "#":
                heapq.heappush(queue, (cost + 1000, r, c, ndr, ndc, list(path)))
    return len(tiles)


if __name__ == "__main__":
    with open("input", "r") as f:
        maze = parse_maze(f.read())
        # print(get_cost(maze))
        print(count_tiles(maze))