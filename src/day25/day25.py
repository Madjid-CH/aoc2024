def parse_input(inputs):
    inputs = list(map(str.strip, inputs.split("\n\n")))
    items = {"#": [], ".": []}
    for grid in inputs:
        grid = list(zip(*grid.split("\n")))
        items[grid[0][0]].append([c.count("#") for c in grid])
    return items


def solve1(items):
    return sum(
        all(l + k <= 7 for l, k in zip(lock, key))
        for lock in items["#"]
        for key in items["."]
    )


if __name__ == "__main__":
    with open("input", "r") as f:
        print(solve1(parse_input(f.read())))