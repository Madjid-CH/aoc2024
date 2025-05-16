import pytest

from src.day3.day3 import execute, parse_input, execute2, parse_conditional_input


@pytest.mark.parametrize(
    "input_, expected",
    [
        ("mul(44,46)", [(44, 46)]),
        ("mul(1,2)mul(4,2)", [(1, 2), (4, 2)]),
        ("$omul(4,2)", [(4, 2)]),
        ("mul[4,2)", []),
        ("mul[4,2]", []),
        ("?(1,2)", []),
        ("mul ( 2 , 4 )", []),
        ("xmul(2,4)%&mul[3,7]", [(2, 4)]),
        (
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)\n+mul(32,64]then(mul(11,8)mul(8,5))",
            [(2, 4), (5, 5), (11, 8), (8, 5)],
        ),
    ],
)
def test_parse_input(input_, expected):
    assert parse_input(input_) == expected


def test_of_acceptance():
    input_ = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert execute(input_) == 161


@pytest.mark.parametrize(
    "input_, expected",
    [
        ("mul(44,46)", [(44, 46)]),
        ("mul(1,2)mul(4,2)", [(1, 2), (4, 2)]),
        ("$omul(4,2)", [(4, 2)]),
        ("mul[4,2)", []),
        ("mul[4,2]", []),
        ("?(1,2)", []),
        ("mul ( 2 , 4 )", []),
        ("xmul(2,4)%&mul[3,7]", [(2, 4)]),
        (
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)\n+mul(32,64]then(mul(11,8)mul(8,5))",
            [(2, 4), (5, 5), (11, 8), (8, 5)],
        ),
        ("mul(2,4)do()mul(2,4)", [(2, 4), "do()", (2, 4)]),
        ("mul(2,4)don't()mul(2,4)", [(2, 4), "don't()", (2, 4)]),
        (
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
            [(2, 4), "don't()", (5, 5), (11, 8), "do()", (8, 5)],
        ),
    ],
)
def test_parse_conditional_input(input_, expected):
    assert parse_conditional_input(input_) == expected


def test_of_acceptance2():
    input_ = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert execute2(input_) == 48
