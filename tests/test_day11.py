from pytest import mark
from anytree import PreOrderIter
from src.day11.day11 import parse_input, blink, repeat_func, count_stones
from functools import reduce

example = "125 17"


def test_parse_input():
    tree = parse_input(example)
    assert [node.name for node in PreOrderIter(tree)] == [None, 125, 17]


@mark.parametrize(
    "arrangement, expected",
    [
        (parse_input(example), [253000, 1, 7]),
        (blink(parse_input(example)), [253, 0, 2024, 14168]),
        (repeat_func(blink, parse_input(example), 2), [512072, 1, 20, 24, 28676032]),
        (
            repeat_func(blink, parse_input(example), 3),
            [512, 72, 2024, 2, 0, 2, 4, 2867, 6032],
        ),
        (
            repeat_func(blink, parse_input(example), 4),
            [1036288, 7, 2, 20, 24, 4048, 1, 4048, 8096, 28, 67, 60, 32],
        ),
        (
            repeat_func(blink, parse_input(example), 5),
            [
                2097446912,
                14168,
                4048,
                2,
                0,
                2,
                4,
                40,
                48,
                2024,
                40,
                48,
                80,
                96,
                2,
                8,
                6,
                7,
                6,
                0,
                3,
                2,
            ],
        ),
    ],
)
def test_blink(arrangement, expected):
    tree = blink(arrangement)
    assert [l.name for l in tree.leaves] == expected


def test_of_acceptance():
    assert count_stones(parse_input(example), n=25) == 55312
