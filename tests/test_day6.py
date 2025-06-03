from pytest import mark

from src.day6.day6 import (
    positions_visited,
    parse_input,
    find_agent_position,
    walk_up,
    turn,
    walk_right,
    walk_down,
    walk_left,
    in_borders,
    path_traversed_right,
    path_traversed_down,
    number_of_obstructions,
)

example = (
    "....#.....\n"
    ".........#\n"
    "..........\n"
    "..#.......\n"
    ".......#..\n"
    "..........\n"
    ".#..^.....\n"
    "........#.\n"
    "#.........\n"
    "......#..."
)


def test_of_acceptance():
    assert positions_visited(example) == 41


@mark.parametrize(
    "input_, expected",
    [
        ("", []),
        ("...#.", [[".", ".", ".", "#", "."]]),
        ("...#.\n.....", [[".", ".", ".", "#", "."], [".", ".", ".", ".", "."]]),
        (
            example,
            [
                [".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", "#", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", "#", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", "#", ".", ".", "^", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
                ["#", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
            ],
        ),
    ],
)
def test_parse_input(input_, expected):
    assert parse_input(input_) == expected


@mark.parametrize(
    "grid, expected",
    [
        ([[".", ".", ".", "#", "."], [".", ".", ".", ".", "."]], ()),
        (
            parse_input(example),
            (6, 4),
        ),
    ],
)
def test_find_agent_position(grid, expected):
    assert find_agent_position(grid) == expected


@mark.parametrize(
    "grid, agent_position, expected",
    [
        (
            [[".", ".", "."], [".", ".", "^"]],
            (1, 2),
            ([[".", ".", "X"], [".", ".", "X"]], (0, 2)),
        ),
        (
            [[".", ".", "."], [".", ".", "."], [".", "^", "."]],
            (2, 1),
            ([[".", "X", "."], [".", "X", "."], [".", "X", "."]], (0, 1)),
        ),
        (
            [[".", "#", "."], [".", ".", "."], [".", "^", "."]],
            (2, 1),
            ([[".", "#", "."], [".", "^", "."], [".", "X", "."]], (1, 1)),
        ),
    ],
)
def test_walk_up(grid, agent_position, expected):
    assert walk_up(grid, agent_position) == expected


@mark.parametrize(
    "grid, agent_position, expected",
    [
        (
            [["#", "."], ["^", "."]],
            (1, 0),
            ([["#", "."], [">", "."]]),
        ),
        (
            [["#", "#"], [">", "#"]],
            (1, 0),
            ([["#", "#"], ["v", "#"]]),
        ),
        (
            [["#", "v"], ["#", "#"]],
            (0, 1),
            ([["#", "<"], ["#", "#"]]),
        ),
        (
            [["#", "<"], ["#", "#"]],
            (0, 1),
            ([["#", "^"], ["#", "#"]]),
        ),
    ],
)
def test_turn(grid, agent_position, expected):
    assert turn(grid, agent_position) == expected


@mark.parametrize(
    "grid, agent_position, expected",
    [
        (
            [[".", ".", "."], [">", ".", "."]],
            (1, 0),
            ([[".", ".", "."], ["X", "X", "X"]], (1, 2)),
        ),
        (
            [[">", ".", "#"], [".", ".", "."], [".", ".", "."]],
            (0, 0),
            ([["X", ">", "#"], [".", ".", "."], [".", ".", "."]], (0, 1)),
        ),
    ],
)
def test_walk_right(grid, agent_position, expected):
    assert walk_right(grid, agent_position) == expected


@mark.parametrize(
    "grid, agent_position, expected",
    [
        (
            [["v", ".", "."], [".", ".", "."]],
            (0, 0),
            ([["X", ".", "."], ["X", ".", "."]], (1, 0)),
        ),
        (
            [["v", "."], [".", "."], ["#", "."]],
            (0, 0),
            ([["X", "."], ["v", "."], ["#", "."]], (1, 0)),
        ),
    ],
)
def test_walk_down(grid, agent_position, expected):
    assert walk_down(grid, agent_position) == expected


@mark.parametrize(
    "grid, agent_position, expected",
    [
        (
            [[".", ".", "."], [".", ".", "<"]],
            (1, 2),
            ([[".", ".", "."], ["X", "X", "X"]], (1, 0)),
        ),
        (
            [["#", ".", "<"], [".", ".", "."], [".", ".", "."]],
            (0, 2),
            ([["#", "<", "X"], [".", ".", "."], [".", ".", "."]], (0, 1)),
        ),
    ],
)
def test_walk_left(grid, agent_position, expected):
    assert walk_left(grid, agent_position) == expected


@mark.parametrize(
    "grid, position, expected",
    [
        ([[".", ".", "."], [".", ".", "."], [".", ".", "."]], (1, 1), False),
        ([[".", ".", "."], [".", ".", "."], [".", ".", "."]], (0, 1), True),
        ([[".", ".", "."], [".", ".", "."], [".", ".", "."]], (2, 1), True),
        ([[".", ".", "."], [".", ".", "."], [".", ".", "."]], (1, 0), True),
        ([[".", ".", "."], [".", ".", "."], [".", ".", "."]], (1, 2), True),
    ],
)
def test_in_borders(grid, position, expected):
    assert in_borders(grid, position) == expected


@mark.parametrize(
    "grid, position, expected",
    [
        ([["X", "X", "#"], [".", ".", "."], [".", ".", "."]], (0, 0), True),
        (
            [[".", "X", "X", "#"], [".", ".", ".", "."], [".", ".", ".", "."]],
            (0, 0),
            True,
        ),
        (
            [[".", "X", "X", "."], [".", ".", ".", "."], [".", ".", ".", "."]],
            (0, 0),
            False,
        ),
        (
            [[".", "X", "#", "X"], [".", "X", ".", "X"], [".", "#", ".", "X"]],
            (0, 0),
            False,
        ),
    ],
)
def test_path_traversed(grid, position, expected):
    assert path_traversed_right(grid, position) == expected


@mark.parametrize(
    "grid, position, expected",
    [
        ([["X", ".", "."], ["X", ".", "."], ["X", ".", "."]], (0, 0), False),
        (
            [[".", ".", ".", "."], ["X", ".", ".", "."], ["X", ".", ".", "."]],
            (0, 0),
            False,
        ),
        (
            [[".", "X", "#", "."], [".", "#", ".", "."], [".", "X", ".", "."]],
            (0, 0),
            False,
        ),
    ],
)
def test_path_down(grid, position, expected):
    assert path_traversed_down(grid, position) == expected


def test_of_acceptance2():
    assert number_of_obstructions(example) == 6
