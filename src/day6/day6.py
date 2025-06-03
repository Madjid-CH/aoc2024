from pprint import pprint


def positions_visited(input_):
    grid = parse_input(input_)
    agent_position = find_agent_position(grid)
    while not in_borders(grid, agent_position):
        grid, agent_position = walk(grid, agent_position)
        grid = turn(grid, agent_position)
    return sum(line.count("X") for line in grid)


def walk(grid, agent_position):
    x, y = agent_position
    direction = grid[x][y]
    match direction:
        case "^":
            return walk_up(grid, agent_position)
        case ">":
            return walk_right(grid, agent_position)
        case "v":
            return walk_down(grid, agent_position)
        case "<":
            return walk_left(grid, agent_position)
    return grid, agent_position


def in_borders(grid, position):
    x, y = position
    return x in (0, len(grid) - 1) or y in (0, len(grid[x]) - 1)


def parse_input(input_):
    return [list(line) for line in input_.splitlines()]


def find_agent_position(grid):
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c == "^":
                return i, j
    return ()


def walk_up(grid, agent_position):
    x, y = agent_position
    for i in range(x, -1, -1):
        if grid[i][y] == "#":
            grid[i + 1][y] = "^"
            return grid, (i + 1, y)
        grid[i][y] = "X"
    return grid, (0, y)


def turn(grid, agent_position):
    x, y = agent_position
    direction = grid[x][y]
    if direction == "^":
        grid[x][y] = ">"
    elif direction == ">":
        grid[x][y] = "v"
    elif direction == "v":
        grid[x][y] = "<"
    elif direction == "<":
        grid[x][y] = "^"
    return grid


def walk_right(grid, agent_position):
    x, y = agent_position
    for i in range(y, len(grid[x])):
        if grid[x][i] == "#":
            grid[x][i - 1] = ">"
            return grid, (x, i - 1)
        grid[x][i] = "X"
    return grid, (x, len(grid[x]) - 1)


def walk_down(grid, agent_position):
    x, y = agent_position
    for i in range(x, len(grid)):
        if grid[i][y] == "#":
            grid[i - 1][y] = "v"
            return grid, (i - 1, y)
        grid[i][y] = "X"
    return grid, (len(grid) - 1, y)


def walk_left(grid, agent_position):
    x, y = agent_position
    for i in range(y, -1, -1):
        if grid[x][i] == "#":
            grid[x][i + 1] = "<"
            return grid, (x, i + 1)
        grid[x][i] = "X"
    return grid, (x, 0)


def path_traversed_right(grid, position):
    x, y = position
    for i in range(y, len(grid[x]) - 1):
        if grid[x][i] == "X" and grid[x][i + 1] == "X":
            while grid[x][i] == "X":
                i += 1
                if grid[x][i] == "#":
                    return True
    return False


def path_traversed_down(grid, position):
    x, y = position
    for i in range(x, len(grid) - 1):
        if grid[i][y] == "X" and grid[i + 1][y] == "X":
            while i < len(grid) and grid[i][y] == "X":
                i += 1
                if i < len(grid) and grid[i][y] == "#":
                    return True
    return False


def path_traversed_up(grid, position):
    x, y = position
    for i in range(x, 0, -1):
        if grid[i][y] == "X" and grid[i - 1][y] == "X":
            while grid[i][y] == "X":
                i -= 1
                if grid[i][y] == "#":
                    return True
    return False


def path_traversed_left(grid, position):
    x, y = position
    for i in range(y, 0, -1):
        if grid[x][i] == "X" and grid[x][i - 1] == "X":
            while grid[x][i] == "X":
                i -= 1
                if grid[x][i] == "#":
                    return True
    return False


def check_for_loop(grid):
    x, y = find_agent_position(grid)
    direction = "^"
    visited = set()

    while True:
        if (x, y, direction) in visited:
            return True
        visited.add((x, y, direction))
        if not in_borders(grid, (x, y)):
            return False
        grid, agent_position = walk(grid, agent_position)
        grid = turn(grid, agent_position)
        x, y = agent_position


def number_of_obstructions(input_):
    grid = parse_input(input_)
    result = 0
    for ro in range(len(grid)):
        for co in range(len(grid[0])):
            if grid[ro][co] != ".":
                continue
            grid[ro][co] = "#"
            if check_for_loop(grid):
                result += 1
            grid[ro][co] = "."
    return result


if __name__ == "__main__":
    with open("input", "r") as f:
        print(number_of_obstructions(f.read()))
