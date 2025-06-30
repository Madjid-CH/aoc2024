def parse_input(input_):
    map_, moves = input_.split("\n\n")
    return parse_map(map_), parse_moves(moves)


def parse_moves(moves):
    return moves.replace("\n", "")


def parse_map(map_):
    return [list(line) for line in map_.splitlines()]


def get_robot_position(grid):
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "@":
                return r, c
    return None


def move_robot(robot, grid, instruction):
    r, c = robot
    match instruction:
        case "^":
            while grid[r][c] not in (".", "#"):
                r -= 1
            if grid[r][c] == ".":
                for i in range(r, robot[0] + 1):
                    grid[i][c] = grid[i + 1][c]
                else:
                    grid[i][c] = "."
                    return robot[0] - 1, c
        case ">":
            row = grid[r]
            while row[c] not in (".", "#"):
                c += 1
            if row[c] == ".":
                for i in range(c, robot[1] - 1, -1):
                    row[i] = row[i - 1]
                else:
                    row[i] = "."
                return r, robot[1] + 1
        case "v":
            while grid[r][c] not in (".", "#"):
                r += 1
            if grid[r][c] == ".":
                for i in range(r, robot[0] - 1, -1):
                    grid[i][c] = grid[i - 1][c]
                else:
                    grid[i][c] = "."
                return robot[0] + 1, c
        case "<":
            row = grid[r]
            while row[c] not in (".", "#"):
                c -= 1
            if row[c] == ".":
                for i in range(c, robot[1] + 1):
                    row[i] = row[i + 1]
                else:
                    row[i] = "."
                return r, robot[1] - 1

    return robot


def walk(grid, instructions):
    robot = get_robot_position(grid)
    for i in instructions:
        robot = move_robot(robot, grid, i)
    return robot, grid


def sum_gps_coordinates(grid):
    total = 0
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "O":
                total += 100 * r + c
    return total


if __name__ == "__main__":
    with open("input", "r") as f:
        grid, moves = parse_input(f.read())
        _, grid = walk(grid, moves)
        print(sum_gps_coordinates(grid))