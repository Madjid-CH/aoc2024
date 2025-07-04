import pytest

from src.day16.day16 import get_cost, parse_maze, count_tiles

example1 = (
    "###############\n"
    "#.......#....E#\n"
    "#.#.###.#.###.#\n"
    "#.....#.#...#.#\n"
    "#.###.#####.#.#\n"
    "#.#.#.......#.#\n"
    "#.#.#####.###.#\n"
    "#...........#.#\n"
    "###.#.#####.#.#\n"
    "#...#.....#.#.#\n"
    "#.#.#.###.#.#.#\n"
    "#.....#...#.#.#\n"
    "#.###.#.#.#.#.#\n"
    "#S..#.....#...#\n"
    "###############"
)
example2 = (
    "#################\n"
    "#...#...#...#..E#\n"
    "#.#.#.#.#.#.#.#.#\n"
    "#.#.#.#...#...#.#\n"
    "#.#.#.#.###.#.#.#\n"
    "#...#.#.#.....#.#\n"
    "#.#.#.#.#.#####.#\n"
    "#.#...#.#.#.....#\n"
    "#.#.#####.#.###.#\n"
    "#.#.#.......#...#\n"
    "#.#.###.#####.###\n"
    "#.#.#...#.....#.#\n"
    "#.#.#.#####.###.#\n"
    "#.#.#.........#.#\n"
    "#.#.#.#########.#\n"
    "#S#.............#\n"
    "#################"
)


def test_parse_maze():
    assert parse_maze(example1) == [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", "E", "#"],
        ["#", ".", "#", ".", "#", "#", "#", ".", "#", ".", "#", "#", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", "#", ".", "#", ".", ".", ".", "#", ".", "#"],
        ["#", ".", "#", "#", "#", ".", "#", "#", "#", "#", "#", ".", "#", ".", "#"],
        ["#", ".", "#", ".", "#", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
        ["#", ".", "#", ".", "#", "#", "#", "#", "#", ".", "#", "#", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
        ["#", "#", "#", ".", "#", ".", "#", "#", "#", "#", "#", ".", "#", ".", "#"],
        ["#", ".", ".", ".", "#", ".", ".", ".", ".", ".", "#", ".", "#", ".", "#"],
        ["#", ".", "#", ".", "#", ".", "#", "#", "#", ".", "#", ".", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#", ".", "#", ".", "#"],
        ["#", ".", "#", "#", "#", ".", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
        ["#", "S", ".", ".", "#", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]


@pytest.mark.parametrize(
    "maze, expected",
    [
        (parse_maze(example1), 7036),
        (parse_maze(example2), 11048),
    ],
)
def test_of_acceptance(maze, expected):
    assert get_cost(maze) == expected


@pytest.mark.parametrize(
    "maze, expected",
    [
        (parse_maze(example1), 45),
        (parse_maze(example2), 64),
    ],
)
def test_of_acceptance2(maze, expected):
    assert count_tiles(maze) == expected
