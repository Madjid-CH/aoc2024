import pytest

from src.day24.day24 import parse_input, solve1


def example():
    return (
        "x00: 1\n"
        "x01: 1\n"
        "x02: 1\n"
        "y00: 0\n"
        "y01: 1\n"
        "y02: 0\n"
        "\n"
        "x00 AND y00 -> z00\n"
        "x01 XOR y01 -> z01\n"
        "x02 OR y02 -> z02"
    )


def example2():
    with open("../src/day24/example") as f:
        return f.read()


@pytest.mark.parametrize("input_, expected", [(example(), 4), (example2(), 2024)])
def test_of_acceptance(input_, expected):
    initials, wire_map = parse_input(input_)
    assert solve1(initials, wire_map) == expected
