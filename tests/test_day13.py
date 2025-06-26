from src.day13.day13 import parse_input, count_tokens, count_tokens2

example = (
    "Button A: X+94, Y+34\n"
    "Button B: X+22, Y+67\n"
    "Prize: X=8400, Y=5400\n"
    "\n"
    "Button A: X+26, Y+66\n"
    "Button B: X+67, Y+21\n"
    "Prize: X=12748, Y=12176\n"
    "\n"
    "Button A: X+17, Y+86\n"
    "Button B: X+84, Y+37\n"
    "Prize: X=7870, Y=6450\n"
    "\n"
    "Button A: X+69, Y+23\n"
    "Button B: X+27, Y+71\n"
    "Prize: X=18641, Y=10279"
)


def test_parse_input():
    assert parse_input(example) == [
        {"A": (94, 34), "B": (22, 67), "prize": (8400, 5400)},
        {"A": (26, 66), "B": (67, 21), "prize": (12748, 12176)},
        {"A": (17, 86), "B": (84, 37), "prize": (7870, 6450)},
        {"A": (69, 23), "B": (27, 71), "prize": (18641, 10279)},
    ]


def test_of_acceptance():
    assert count_tokens(example) == 480


def test_of_acceptance2():
    assert count_tokens2(example) == 875318608908