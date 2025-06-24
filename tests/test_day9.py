from pytest import mark

from src.day9.day9 import (
    compute_checksum,
    parse_disk_map,
    compact_disk_map,
    fragment_blocks,
    fragment_files,
    get_empty_blocks,
    compute_checksum2,
)

example = "2333133121414131402"


def test_of_acceptance():
    assert compute_checksum(example) == 1928


@mark.parametrize(
    "disk_map, expected",
    [
        ("1", [1]),
        ("12", [1, 2]),
        ("12345", [1, 2, 3, 4, 5]),
    ],
)
def test_parse_disk_map(disk_map, expected):
    assert parse_disk_map(disk_map) == expected


def parse_expended_disk_map(s):
    return [int(ch) if ch.isdigit() else ch for ch in s]


@mark.parametrize(
    "disk_map, expected",
    [
        ([1], [0]),
        ([2], [0, 0]),
        ([5], [0, 0, 0, 0, 0]),
        ([1, 2], [0, ".", "."]),
        (list(range(1, 6)), [0, ".", ".", 1, 1, 1, ".", ".", ".", ".", 2, 2, 2, 2, 2]),
        (
            parse_disk_map(example),
            parse_expended_disk_map("00...111...2...333.44.5555.6666.777.888899"),
        ),
    ],
)
def test_compact_disk_map(disk_map, expected):
    assert compact_disk_map(disk_map) == expected


@mark.parametrize(
    "expanded_map, expected",
    [
        (
            parse_expended_disk_map("0..111....22222"),
            parse_expended_disk_map("022111222......"),
        ),
        (
            parse_expended_disk_map("00...111...2...333.44.5555.6666.777.888899"),
            parse_expended_disk_map("0099811188827773336446555566.............."),
        ),
    ],
)
def test_fragment_blocks(expanded_map, expected):
    assert fragment_blocks(expanded_map) == expected


@mark.parametrize(
    "expanded_map, expected",
    [
        (
            parse_expended_disk_map("00...111...2...333.44.5555.6666.777.888899"),
            parse_expended_disk_map("00992111777.44.333....5555.6666.....8888.."),
        ),
    ],
)
def test_fragment_files(expanded_map, expected):
    assert to_string(fragment_files(expanded_map)) == to_string(expected)

def to_string(l):
    return "".join(map(str, l))
@mark.parametrize("expanded_map, expected", [
    (
        parse_expended_disk_map("00...111...2...333.44.5555.6666.777.888899"),
        [(2, 3), (8, 3), (12, 3), (18, 1), (21, 1), (26, 1), (31, 1), (35, 1)]
    )
])
def test_get_empty_blocks(expanded_map, expected):
    assert get_empty_blocks(expanded_map) == expected



def test_of_acceptance2():
    assert compute_checksum2(example) == 2858





