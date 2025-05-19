from itertools import chain


def count_accuracies(input_):
    grid = parse_input(input_)
    results = []
    for search_fn in (
        search_forward,
        search_backward,
        search_vertically_up,
        search_vertically_down,
        search_diagonally_up_forward,
        search_diagonally_down_forward,
        search_diagonally_up_backward,
        search_diagonally_down_backward,
    ):
        results.append(search_fn(grid))
    flattened = chain.from_iterable(results)
    flattened = filter(lambda x: x, flattened)
    return sum(len(l) for l in flattened)


def parse_input(input_):
    lines = input_.splitlines()
    return [list(line) for line in lines]


def search_forward(grid):
    result = []
    for x, line in enumerate(grid):
        indexes = []
        for y, _ in enumerate(line):
            if xmas_exist(line, y):
                indexes.append(y)
        result.append(indexes)
    return result


def xmas_exist(line, y):
    return (
        len(line) - y > 3
        and line[y] == "X"
        and line[y + 1] == "M"
        and line[y + 2] == "A"
        and line[y + 3] == "S"
    )


def search_backward(grid):
    result = []
    for x, line in enumerate(grid):
        indexes = []
        r = list(reversed(line))
        for y, _ in enumerate(r):
            if xmas_exist(r, y):
                indexes.insert(0, len(r) - y - 1)
        result.append(indexes)
    return result


def search_vertically_down(grid):
    result = []
    for x, line in enumerate(grid):
        indexes = []
        for y, _ in enumerate(line):
            if xmas_found_vertically(grid, x, y):
                indexes.append(y)
        result.append(indexes)
    return result


def xmas_found_vertically(grid, x, y):
    return (
        len(grid) - x > 3
        and grid[x][y] == "X"
        and grid[x + 1][y] == "M"
        and grid[x + 2][y] == "A"
        and grid[x + 3][y] == "S"
    )


def search_vertically_up(grid):
    result = []
    reversed_grid = list(reversed(grid))
    for x, line in enumerate(reversed_grid):
        indexes = []
        for y, _ in enumerate(line):
            if xmas_found_vertically(reversed_grid, x, y):
                indexes.append(y)
        result.append(indexes)
    return list(reversed(result))


def search_diagonally_down_forward(grid, word="XMAS"):
    result = []
    for x, line in enumerate(grid):
        indexes = []
        for y, _ in enumerate(line):
            if word_found_diagonally(grid, x, y, word):
                indexes.append(y)
        result.append(indexes)
    return result


def search_diagonally_up_forward(grid, word="XMAS"):
    grid = list(reversed(grid))
    result = search_diagonally_down_forward(grid, word)
    return list(reversed(result))


def word_found_diagonally(grid, x, y, word="XMAS"):
    return (
        len(grid) - x > len(word) - 1
        and len(grid[x]) - y > len(word) - 1
        and all(grid[x + i][y + i] == c for i, c in enumerate(word))
    )


def search_diagonally_down_backward(grid, word="XMAS"):
    grid = [list(reversed(l)) for l in grid]
    return search_diagonally_backward(grid, word)


def search_diagonally_up_backward(grid, word="XMAS"):
    reversed_grid = [list(reversed(l)) for l in reversed(grid)]
    result = search_diagonally_backward(reversed_grid, word)
    return list(reversed(result))


def search_diagonally_backward(reversed_grid, word="XMAS"):
    result = []
    for x, line in enumerate(reversed_grid):
        indexes = []
        for y, _ in enumerate(line):
            if word_found_diagonally(reversed_grid, x, y, word):
                indexes.insert(0, len(line) - y - 1)
        result.append(indexes)
    return result


def count_x_mas(input_):
    grid = parse_input(input_)
    down_forward = search_diagonally_down_forward(grid, "MAS")
    down_backward = search_diagonally_down_backward(grid, "MAS")
    up_forward = search_diagonally_up_forward(grid, "MAS")
    up_backward = search_diagonally_up_backward(grid, "MAS")
    counter = 0
    for x, line in enumerate(down_forward):
        for i in line:
            if i in up_forward[x + 2]:
                counter += 1
            if i + 2 in down_backward[x]:
                counter += 1

    for x, line in enumerate(up_backward):
        for i in line:
            if i - 2 in up_forward[x]:
                counter += 1
            if i in down_backward[x - 2]:
                counter += 1

    return counter


if __name__ == "__main__":
    with open("input", "r") as f:
        print(count_x_mas(f.read()))
