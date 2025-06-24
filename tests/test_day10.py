from pytest import mark

from src.day10.day10 import (
    compute_score,
    parse_topographic_map,
    find_trailheads,
    count_hiking_trails,
    get_trailhead_rating,
    sum_ratings,
)

example = (
    "89010123\n78121874\n87430965\n96549874\n45678903\n32019012\n01329801\n10456732"
)


def test_of_acceptance():
    assert compute_score(example) == 36


def test_parse_input():
    assert parse_topographic_map(example) == [
        [8, 9, 0, 1, 0, 1, 2, 3],
        [7, 8, 1, 2, 1, 8, 7, 4],
        [8, 7, 4, 3, 0, 9, 6, 5],
        [9, 6, 5, 4, 9, 8, 7, 4],
        [4, 5, 6, 7, 8, 9, 0, 3],
        [3, 2, 0, 1, 9, 0, 1, 2],
        [0, 1, 3, 2, 9, 8, 0, 1],
        [1, 0, 4, 5, 6, 7, 3, 2],
    ]


def test_find_trailheads():
    grid = parse_topographic_map(example)
    trailheads = find_trailheads(grid)
    assert trailheads == [
        (0, 2),
        (0, 4),
        (2, 4),
        (4, 6),
        (5, 2),
        (5, 5),
        (6, 0),
        (6, 6),
        (7, 1),
    ]


@mark.parametrize(
    "tmap, trailhead, expected",
    [
        (
            parse_topographic_map(
                "...0...\n...1...\n...2...\n6543456\n7.....7\n8.....8\n9.....9"
            ),
            (0, 3),
            2,
        ),
        (
            parse_topographic_map(
                "..90..9\n...1.98\n...2..7\n6543456\n765.987\n876....\n987...."
            ),
            (0, 3),
            4,
        ),
        (
            parse_topographic_map(
                "10..9..\n2...8..\n3...7..\n4567654\n...8..3\n...9..2\n.....01"
            ),
            (0, 1),
            1,
        ),
        (
            parse_topographic_map(
                "10..9..\n2...8..\n3...7..\n4567654\n...8..3\n...9..2\n.....01"
            ),
            (6, 5),
            2,
        ),
        (parse_topographic_map(example), (0, 2), 5),
        (parse_topographic_map(example), (0, 4), 6),
    ],
)
def test_count_hiking_trails(tmap, trailhead, expected):
    assert count_hiking_trails(tmap, trailhead) == expected


@mark.parametrize(
    "tmap, trailhead, expected",
    [
        (
            parse_topographic_map(
                ".....0.\n..4321.\n..5..2.\n..6543.\n..7..4.\n..8765.\n..9...."
            ),
            (0, 5),
            3,
        ),
        (
            parse_topographic_map(
                "..90..9\n...1.98\n...2..7\n6543456\n765.987\n876....\n987...."
            ),
            (0, 3),
            13,
        ),
        (
            parse_topographic_map("012345\n123456\n234567\n345678\n4.6789\n56789."),
            (0, 0),
            227,
        ),
    ],
)
def test_get_trailhead_rating(tmap, trailhead, expected):
    assert get_trailhead_rating(tmap, trailhead) == expected


def test_of_acceptance2():
    assert sum_ratings(example) == 81
