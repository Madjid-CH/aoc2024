from src.day18.day18 import parse_input, count_steps, get_blocking_coordinates

example = (
    "5,4\n"
    "4,2\n"
    "4,5\n"
    "3,0\n"
    "2,1\n"
    "6,3\n"
    "2,4\n"
    "1,5\n"
    "0,6\n"
    "3,3\n"
    "2,6\n"
    "5,1\n"
    "1,2\n"
    "5,5\n"
    "2,5\n"
    "6,5\n"
    "1,4\n"
    "0,4\n"
    "6,4\n"
    "1,1\n"
    "6,1\n"
    "1,0\n"
    "0,5\n"
    "1,6\n"
    "2,0"
)


def test_of_acceptance():
    blocks = parse_input(example)
    assert count_steps(blocks[:12], grid_dim=(7, 7)) == 22


def test_of_acceptance2():
    blocks = parse_input(example)
    assert get_blocking_coordinates(blocks, (7, 7)) == (6, 1)
