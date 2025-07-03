from src.day21.day21 import parse_codes, sum_complexities

example = "029A\n980A\n179A\n456A\n379A"


def test_of_acceptance():
    assert sum_complexities(parse_codes(example)) == 126384