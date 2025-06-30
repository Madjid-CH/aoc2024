from src.day15 import day15


def parse_input(input_):
    map_, moves = input_.split("\n\n")
    return parse_map(map_), day15.parse_moves(moves)


def parse_map(map_: str):
    map_ = map_.replace("#", "##")
    map_ = map_.replace("O", "[]")
    map_ = map_.replace(".", "..")
    map_ = map_.replace("@", "@.")
    return day15.parse_map(map_)


def move_robot(robot, grid, instruction):
    moves_map = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
    dr, dc = moves_map[instruction]
    do_move = True
    to_move = [robot]
    i = 0
    while i < len(to_move):
        rr, cc = to_move[i]
        i += 1
        nr, nc = rr + dr, cc + dc
        if (nr, nc) in to_move:
            continue
        if grid[nr][nc] == "#":
            do_move = False
            break
        if grid[nr][nc] == ".":
            continue
        if grid[nr][nc] == "[":
            to_move.extend([(nr, nc), (nr, nc + 1)])
        elif grid[nr][nc] == "]":
            to_move.extend([(nr, nc), (nr, nc - 1)])
        else:
            assert False

    if not do_move:
        return robot
    grid_copy = [list(row) for row in grid]
    for rr, cc in to_move:
        grid[rr][cc] = "."
    for rr, cc in to_move:
        grid[rr + dr][cc + dc] = grid_copy[rr][cc]

    return robot[0] + dr, robot[1] + dc


def walk(grid, instructions):
    robot = day15.get_robot_position(grid)
    for i in instructions:
        robot = move_robot(robot, grid, i)
    return robot, grid


def solve(grid):
    return sum(
        r * 100 + c
        for r, row in enumerate(grid)
        for c, val in enumerate(row)
        if val == "["
    )


if __name__ == "__main__":
    with open("input", "r") as f:
        grid, moves = parse_input(f.read())
        _, grid = walk(grid, moves)
        print(solve(grid))