from pytest import mark

from src.day15.part2 import (
    parse_input,
    walk,
    move_robot,
    solve,
)


def large_map():
    with open("../src/day15/example", "r") as f:
        grid, _ = parse_input(f.read())
        return grid


def small_map():
    return [
        list(line)
        for line in (
            "##############\n"
            "##......##..##\n"
            "##..........##\n"
            "##....[][]@.##\n"
            "##....[]....##\n"
            "##..........##\n"
            "##############"
        ).splitlines()
    ]


def test_parse_input():
    assert "".join("".join(line) + "\n" for line in large_map()) == (
        "####################\n"
        "##....[]....[]..[]##\n"
        "##............[]..##\n"
        "##..[][]....[]..[]##\n"
        "##....[]@.....[]..##\n"
        "##[]##....[]......##\n"
        "##[]....[]....[]..##\n"
        "##..[][]..[]..[][]##\n"
        "##........[]......##\n"
        "####################\n"
    )


@mark.parametrize(
    "robot, grid, instruction, expected",
    [
        ((3, 10), small_map(), "<", (3, 9)),
        (*walk(small_map(), "<"), "v", (4, 9)),
        (*walk(small_map(), "<v"), "v", (5, 9)),
        (*walk(small_map(), "<vv"), "<", (5, 8)),
        (*walk(small_map(), "<vv<"), "<", (5, 7)),
        (*walk(small_map(), "<vv<<"), "^", (4, 7)),
        (*walk(small_map(), "<vv<<^"), "<", (4, 6)),
        (*walk(small_map(), "<vv<<^<"), "<", (4, 5)),
        (*walk(small_map(), "<vv<<^<<"), "^", (3, 5)),
        (*walk(small_map(), "<vv<<^<<^"), "^", (2, 5)),
    ],
)
def test_move_robot(robot, grid, instruction, expected):
    assert move_robot(robot, grid, instruction) == expected


def test_of_acceptance():
    with open("../src/day15/example", "r") as f:
        grid, moves = parse_input(f.read())
    _, grid = walk(grid, moves)
    assert solve(grid) == 9021

