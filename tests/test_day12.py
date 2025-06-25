from pytest import mark

from src.day12.day12 import fence_price, price_with_discount

example = (
    "RRRRIICCFF\n"
    "RRRRIICCCF\n"
    "VVRRRCCFFF\n"
    "VVRCCCJFFF\n"
    "VVVVCJJCFE\n"
    "VVIVCCJJEE\n"
    "VVIIICJJEE\n"
    "MIIIIIJJEE\n"
    "MIIISIJEEE\n"
    "MMMISSJEEE"
)


@mark.parametrize(
    "garden, expected",
    [
        ("AAAA\nBBCD\nBBCC\nEEEC", 140),
        ("OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO", 772),
        (example, 1930),
    ],
)
def test_of_acceptance(garden, expected):
    assert fence_price(garden) == expected


@mark.parametrize(
    "garden, expected",
    [
        ("AAAA\nBBCD\nBBCC\nEEEC", 80),
        ("EEEEE\nEXXXX\nEEEEE\nEXXXX\nEEEEE", 236),
        ("OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO", 436),
        ("AAAAAA\nAAABBA\nAAABBA\nABBAAA\nABBAAA\nAAAAAA", 368),
        (example, 1206)
    ],
)
def test_of_acceptance2(garden, expected):
    assert price_with_discount(garden) == expected
