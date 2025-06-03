from pytest import mark

from src.day7.day7 import total_calibration, parse_input, is_true_equation

example = (
    "190: 10 19\n"
    "3267: 81 40 27\n"
    "83: 17 5\n"
    "156: 15 6\n"
    "7290: 6 8 6 15\n"
    "161011: 16 10 13\n"
    "192: 17 8 14\n"
    "21037: 9 7 18 13\n"
    "292: 11 6 16 20"
)


def test_of_acceptance():
    assert total_calibration(example) == 11387


@mark.parametrize(
    "input_, expected",
    [
        ("190: 10 19", {190: (10, 19)}),
        ("190: 10 19\n3267: 81 40 27\n", {190: (10, 19), 3267: (81, 40, 27)}),
        (
            example,
            {
                83: (17, 5),
                156: (15, 6),
                190: (10, 19),
                192: (17, 8, 14),
                292: (11, 6, 16, 20),
                3267: (81, 40, 27),
                7290: (6, 8, 6, 15),
                21037: (9, 7, 18, 13),
                161011: (16, 10, 13),
            },
        ),
    ],
)
def test_parse_input(input_, expected):
    assert parse_input(input_) == expected


@mark.parametrize(
    "value, numbers, expected",
    [
        (190, (10, 19), True),
        (156, (15, 6), True),
        (3267, (81, 40, 27), True),
        (292, (11, 6, 16, 20), True),
    ],
)
def test_is_true_equation(value, numbers, expected):
    assert is_true_equation(value, numbers) == expected
