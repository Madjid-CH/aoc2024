from pickle import FALSE

from pytest import mark

from src.day2.day2 import (
    count_safe_reports,
    parse_input,
    is_safe,
    is_strictly_monotonic,
    no_gap_bigger_then_3,
    count_safe_reports_with_dampener,
)


@mark.parametrize(
    "input_, expected",
    [
        ("", []),
        ("7 6 4 2 1", [[7, 6, 4, 2, 1]]),
        ("7 6 4 2 1\n1 2 7 8 9", [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9]]),
    ],
)
def test_parse_input(input_, expected):
    assert parse_input(input_) == expected


@mark.parametrize(
    "report, expected",
    [
        ((7, 6, 4, 2, 1), True),
        ((1, 2, 7, 8, 9), True),
        ((9, 7, 6, 2, 1), True),
        ((1, 3, 2, 4, 5), False),
    ],
)
def test_is_strictly_monotonic(report, expected):
    assert is_strictly_monotonic(report) == expected


@mark.parametrize(
    "report, expected",
    [
        ((7, 6, 4, 2, 1), True),
        ((1, 2, 7, 8, 9), False),
        ((9, 7, 6, 2, 1), False),
        ((1, 3, 2, 4, 5), True),
    ],
)
def test_no_gap_bigger_then_3(report, expected):
    assert no_gap_bigger_then_3(report) == expected


@mark.parametrize(
    "report, expected",
    [
        ((7, 6, 4, 2, 1), True),
        ((1, 2, 7, 8, 9), False),
        ((9, 7, 6, 2, 1), False),
        ((1, 3, 2, 4, 5), False),
    ],
)
def test_is_safe(report, expected):
    assert is_safe(report) == expected


def test_of_acceptance():
    input_ = "7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9"
    assert count_safe_reports(input_) == 2


def test_of_acceptance2():
    input_ = "7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9"
    assert count_safe_reports_with_dampener(input_) == 4
