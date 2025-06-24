from functools import cache

from anytree import Node


def parse_input(input_: str):
    rocks = input_.split()
    rocks = [int(r) for r in rocks]
    root = Node(None)
    [Node(r, parent=root) for r in rocks]
    return root


def blink(arrangement):
    for leaf in arrangement.leaves:
        if leaf.name == 0:
            leaf.name = 1
        elif even_number_of_digits(leaf.name):
            n = str(leaf.name)
            n1 = int(n[: len(n) // 2])
            n2 = int(n[len(n) // 2 :])
            _left_node = Node(n1, parent=leaf)
            _right_node = Node(n2, parent=leaf)
        else:
            leaf.name *= 2024
    return arrangement


def even_number_of_digits(n):
    return len(str(n)) % 2 == 0


def count_stones(tree, n):
    tree = repeat_func(blink, tree, n)
    return len(tree.leaves)


def repeat_func(func, value, times):
    for i in range(times):
        value = func(value)
    return value


@cache
def count_stones(val: int, blinks: int) -> int:
    if blinks == 0:
        return 1
    if val == 0:
        return count_stones(1, blinks - 1)
    str_val = str(val)
    len_str_val = len(str_val)
    if len_str_val % 2 == 0:
        return count_stones(
            int(str_val[: len_str_val // 2]), blinks - 1
        ) + count_stones(int(str_val[len_str_val // 2 :]), blinks - 1)
    return count_stones(val * 2024, blinks - 1)


def solve2(stones, n):
    return sum(count_stones(s, n) for s in stones)


if __name__ == "__main__":
    with open("input", "r") as f:
        tree = parse_input(f.read())
        stones = [l.name for l in tree.leaves]
        print(solve2(stones, 75))
