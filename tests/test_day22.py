from src.day22.day22 import parse_input, solve1, solve2


def test_of_acceptance():
    example = "1\n10\n100\n2024"
    assert solve1(parse_input(example)) == 37327623


def test_of_acceptance2():
    example2 = "1\n2\n3\n2024"
    assert solve2(parse_input(example2)) == 23

