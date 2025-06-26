import pytest

from src.day14.day14 import (
    parse_input,
    Robot,
    parse_line,
    move_robot,
    get_safety_factor,
)

example = (
    "p=0,4 v=3,-3\n"
    "p=6,3 v=-1,-3\n"
    "p=10,3 v=-1,2\n"
    "p=2,0 v=2,-1\n"
    "p=0,0 v=1,3\n"
    "p=3,0 v=-2,-2\n"
    "p=7,6 v=-1,-3\n"
    "p=3,0 v=-1,-2\n"
    "p=9,3 v=2,3\n"
    "p=7,3 v=-1,2\n"
    "p=2,4 v=2,-3\n"
    "p=9,5 v=-3,-3"
)


def test_parse_input():
    assert parse_input(example) == [
        Robot(position=(0, 4), velocity=(3, -3)),
        Robot(position=(6, 3), velocity=(-1, -3)),
        Robot(position=(10, 3), velocity=(-1, 2)),
        Robot(position=(2, 0), velocity=(2, -1)),
        Robot(position=(0, 0), velocity=(1, 3)),
        Robot(position=(3, 0), velocity=(-2, -2)),
        Robot(position=(7, 6), velocity=(-1, -3)),
        Robot(position=(3, 0), velocity=(-1, -2)),
        Robot(position=(9, 3), velocity=(2, 3)),
        Robot(position=(7, 3), velocity=(-1, 2)),
        Robot(position=(2, 4), velocity=(2, -3)),
        Robot(position=(9, 5), velocity=(-3, -3)),
    ]


@pytest.mark.parametrize(
    "robot, expected",
    [
        (parse_line("p=2,4 v=2,-3"), parse_line("p=4,1 v=2,-3")),
        (parse_line("p=4,1 v=2,-3"), parse_line("p=6,5 v=2,-3")),
        (parse_line("p=6,5 v=2,-3"), parse_line("p=8,2 v=2,-3")),
        (parse_line("p=8,2 v=2,-3"), parse_line("p=10,6 v=2,-3")),
        (parse_line("p=10,6 v=2,-3"), parse_line("p=1,3 v=2,-3")),
    ],
)
def test_move_robot(robot, expected):
    assert move_robot(robot, (11, 7)) == expected


def test_of_acceptance():
    assert get_safety_factor(parse_input(example), (11, 7), 100) == 12