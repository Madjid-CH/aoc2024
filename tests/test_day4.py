import pytest

from src.day4.day4 import (
    count_accuracies,
    parse_input,
    search_forward,
    search_backward,
    search_vertically_up,
    search_vertically_down,
    search_diagonally_down_forward,
    search_diagonally_down_backward,
    search_diagonally_up_forward,
    search_diagonally_up_backward,
    count_x_mas,
)

example = (
    "MMMSXXMASM\n"
    "MSAMXMSMSA\n"
    "AMXSXMAAMM\n"
    "MSAMASMSMX\n"
    "XMASAMXAMM\n"
    "XXAMMXXAMA\n"
    "SMSMSASXSS\n"
    "SAXAMASAAA\n"
    "MAMMMXMMMM\n"
    "MXMXAXMASX"
)


def test_of_acceptance():
    assert count_accuracies(example) == 18


@pytest.mark.parametrize(
    "input_, expected",
    [
        ("MMMSXXMASM", [["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"]]),
        (
            example,
            [
                ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
                ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
                ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
                ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
                ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
                ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
                ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
                ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
                ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
                ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"],
            ],
        ),
    ],
)
def test_parse_input(input_, expected):
    assert parse_input(input_) == expected


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"]], [[5]]),
        ([["M", "M", "M", "S", "X", "X", "M", "A"]], [[]]),
        ([["X", "M", "A", "S", "X", "X", "M", "A", "S", "M"]], [[0, 5]]),
        (
            [
                ["X", "M", "A", "S", "X", "X", "M", "A", "S", "M"],
                ["X", "M", "A", "S", "X", "X", "M", "A", "S", "M"],
            ],
            [[0, 5], [0, 5]],
        ),
    ],
)
def test_search_forward_horizontally(grid, expected):
    assert search_forward(grid) == expected


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([["M", "S", "A", "M", "X", "X", "S", "M", "M", "M"]], [[4]]),
        ([["M", "M", "M", "S", "X", "X", "M", "A"]], [[]]),
        ([["M", "S", "A", "M", "X", "X", "S", "A", "M", "X"]], [[4, 9]]),
        (
            [
                ["M", "S", "A", "M", "X", "X", "S", "A", "M", "X"],
                ["M", "S", "A", "M", "X", "X", "S", "A", "M", "X"],
            ],
            [[4, 9], [4, 9]],
        ),
    ],
)
def test_search_backward_horizontally(grid, expected):
    assert search_backward(grid) == expected


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([["X"], ["M"], ["A"], ["S"], ["M"]], [[0], [], [], [], []]),
        ([["X"], ["M"], ["A"]], [[], [], []]),
        ([["X", "X"], ["M", "M"], ["A", "A"], ["S", "S"]], [[0, 1], [], [], []]),
    ],
)
def test_search_vertical_downward(grid, expected):
    assert search_vertically_down(grid) == expected


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([["M"], ["S"], ["A"], ["M"], ["X"]], [[], [], [], [], [0]]),
        ([["X"], ["M"], ["A"]], [[], [], []]),
        ([["S", "S"], ["A", "A"], ["M", "M"], ["X", "X"]], [[], [], [], [0, 1]]),
    ],
)
def test_search_vertical_upward(grid, expected):
    assert search_vertically_up(grid) == expected


@pytest.mark.parametrize(
    "grid, expected",
    [
        (parse_input("AAAA\nAMAA\nAAAA\nAAAS"), [[], [], [], []]),
        (parse_input("XAAA\nAMAA\nAAAA\nAAAS"), [[0], [], [], []]),
        (parse_input("XAAA\nAMAA\nAAAA"), [[], [], []]),
    ],
)
def test_search_diagonally_down_forward(grid, expected):
    assert search_diagonally_down_forward(grid) == expected


@pytest.mark.parametrize(
    "grid, expected",
    [
        (parse_input("AAAA\nAMAA\nAAAA\nAAAS"), [[], [], [], []]),
        (parse_input("AAAX\nAAMA\nAAAA\nSAAA"), [[3], [], [], []]),
        (parse_input("XAAA\nAMAA\nAAAA"), [[], [], []]),
    ],
)
def test_search_diagonally_down_backward(grid, expected):
    assert search_diagonally_down_backward(grid) == expected


@pytest.mark.parametrize(
    "grid, expected",
    [
        (parse_input("AAAA\nAMAA\nAAAA\nAAAS"), [[], [], [], []]),
        (parse_input("AAAS\nAAAA\nAMAA\nXAAA"), [[], [], [], [0]]),
        (parse_input("AAAA\nAAMA\nAAAX"), [[], [], []]),
    ],
)
def test_search_diagonally_up_forward(grid, expected):
    assert search_diagonally_up_forward(grid) == expected


@pytest.mark.parametrize(
    "grid, expected",
    [
        (parse_input("AAAA\nAMAA\nAAAA\nAAAS"), [[], [], [], []]),
        (parse_input("SAAA\nAAAA\nAAMA\nAAAX"), [[], [], [], [3]]),
        (parse_input("AAAA\nAAMA\nAAAX"), [[], [], []]),
    ],
)
def test_search_diagonally_up_backward(grid, expected):
    assert search_diagonally_up_backward(grid) == expected


def test_of_acceptance2():
    assert count_x_mas(example) == 9


@pytest.mark.parametrize(
    "grid",
    [
        (parse_input("M.S\n.A.\nM.S")),
    ],
)
def test_finding_x_mas(grid):
    a = search_diagonally_down_forward(grid, "MAS")
    b = search_diagonally_up_forward(grid, "MAS")
    x = 0
    y = 0
    assert a[x][y] == b[x + 2][y]


@pytest.mark.parametrize(
    "grid",
    [
        (parse_input("M.M\n.A.\nS.S")),
    ],
)
def test_finding_x_mas2(grid):
    a = search_diagonally_down_forward(grid, "MAS")
    b = search_diagonally_down_backward(grid, "MAS")
    x, y = 0, 0
    assert a[x][y] + 2 == b[x][y]


@pytest.mark.parametrize(
    "grid",
    [
        (parse_input("S.S\n.A.\nM.M")),
    ],
)
def test_finding_x_mas3(grid):
    a = search_diagonally_up_forward(grid, "MAS")
    b = search_diagonally_up_backward(grid, "MAS")
    x, y = 2, 0
    assert a[x][y] + 2 == b[x][y]


@pytest.mark.parametrize(
    "grid",
    [
        (parse_input("S.M\n.A.\nS.M")),
    ],
)
def test_finding_x_mas4(grid):
    a = search_diagonally_up_backward(grid, "MAS")
    b = search_diagonally_down_backward(grid, "MAS")
    x, y = 2, 0
    assert a[x][y] == b[x - 2][y]
