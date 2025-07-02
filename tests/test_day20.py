from src.day20.day20 import parse_grid, solve1

example = (
    "###############\n"
    "#...#...12....#\n"
    "#.#.#.#.#.###.#\n"
    "#S#...#.#.#...#\n"
    "#######.#.#.###\n"
    "#######.#.#...#\n"
    "#######.#.###.#\n"
    "###..E#...#...#\n"
    "###.#######.###\n"
    "#...###...#...#\n"
    "#.#####.#.###.#\n"
    "#.#...#.#.#...#\n"
    "#.#.#.#.#.#.###\n"
    "#...#...#...###\n"
    "###############"
)


def test_of_acceptance():
    grid = parse_grid(example)
    assert solve1(grid, max_cheat=2, target_saving=1) == 46


def test_of_acceptance2():
    grid = parse_grid(example)
    assert solve1(grid, max_cheat=20, target_saving=50) == 285
