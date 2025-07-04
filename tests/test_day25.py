from src.day25.day25 import parse_input, solve1


def example():
    with open("../src/day25/example") as f:
        return f.read()


def test_of_acceptance():
    assert solve1(parse_input(example())) == 3
