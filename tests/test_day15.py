from pytest import mark

from src.day15.day15 import (
    parse_input,
    move_robot,
    parse_map,
    walk,
    sum_gps_coordinates,
)

small_example = (
    "########\n"
    "#..O.O.#\n"
    "##@.O..#\n"
    "#...O..#\n"
    "#.#.O..#\n"
    "#...O..#\n"
    "#......#\n"
    "########\n"
    "\n"
    "<^^>>>vv<v>>v<<"
)


def small_map():
    return parse_map(small_example.split("\n\n")[0])


def test_parse_input():
    assert parse_input(small_example) == (
        [
            ["#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", "O", ".", "O", ".", "#"],
            ["#", "#", "@", ".", "O", ".", ".", "#"],
            ["#", ".", ".", ".", "O", ".", ".", "#"],
            ["#", ".", "#", ".", "O", ".", ".", "#"],
            ["#", ".", ".", ".", "O", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#"],
        ],
        "<^^>>>vv<v>>v<<",
    )


@mark.parametrize(
    "robot, grid, instruction, expected",
    [
        ((2, 2), small_map(), "<", (2, 2)),
        (*walk(small_map(), "<"), "^", (1, 2)),
        (*walk(small_map(), "<^"), "^", (1, 2)),
        (*walk(small_map(), "<^^"), ">", (1, 3)),
        (*walk(small_map(), "<^^>"), ">", (1, 4)),
        (*walk(small_map(), "<^^>>"), ">", (1, 4)),
        (*walk(small_map(), "<^^>>"), "v", (2, 4)),
        (*walk(small_map(), "<^^>>v"), "v", (2, 4)),
        (*walk(small_map(), "<^^>>vv"), "<", (2, 3)),
        (*walk(small_map(), "<^^>>vv<"), "v", (3, 3)),
        (*walk(small_map(), "<^^>>vv<v"), ">", (3, 4)),
        (*walk(small_map(), "<^^>>vv<v>"), ">", (3, 5)),
        (*walk(small_map(), "<^^>>vv<v>>"), "v", (4, 5)),
        (*walk(small_map(), "<^^>>vv<v>>v"), "<", (4, 4)),
        (*walk(small_map(), "<^^>>vv<v>>v<"), "<", (4, 4)),
    ],
)
def test_move_robot(robot, grid, instruction, expected):
    assert move_robot(robot, grid, instruction) == expected


def test_of_acceptance():
    expected = parse_map(
        "##########\n"
        "#.O.O.OOO#\n"
        "#........#\n"
        "#OO......#\n"
        "#OO@.....#\n"
        "#O#.....O#\n"
        "#O.....OO#\n"
        "#O.....OO#\n"
        "#OO....OO#\n"
        "##########"
    )
    with open("../src/day15/example", "r") as f:
        grid, moves = parse_input(f.read())
        _, grid = walk(grid, moves)
        assert grid == expected
        assert sum_gps_coordinates(grid) == 10092