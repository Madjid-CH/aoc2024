from src.day19.day19 import (
    parse_designs,
    count_valid_designs,
    count_all_combinations,
)

example = (
    "r, wr, b, g, bwu, rb, gb, br\n"
    "\n"
    "brwrr\n"
    "bggr\n"
    "gbbr\n"
    "rrbgbr\n"
    "ubwu\n"
    "bwurrg\n"
    "brgr\n"
    "bbrgwb"
)


def test_of_acceptance():
    patterns, designs = parse_designs(example)
    assert count_valid_designs(patterns, designs) == 6


def test_of_acceptance2():
    patterns, designs = parse_designs(example)
    assert count_all_combinations(patterns, designs) == 16
