import re
from functools import cache


def parse_designs(input_):
    patterns, designs = input_.split("\n\n")
    patterns = tuple(re.findall("(\\w+)", patterns))
    designs = designs.splitlines()
    return patterns, designs


@cache
def is_valid(patterns: set[str], design: str):
    if design == "":
        return True
    for p in patterns:
        if design.startswith(p):
            if is_valid(patterns, design[len(p) :]):
                return True
    return False


@cache
def count_combinations(patterns, design):
    if design == "":
        return 1
    count = 0
    for p in patterns:
        if design.startswith(p):
            count += count_combinations(patterns, design.removeprefix(p))
    return count


def count_valid_designs(patterns, designs):
    valid_designs = [d for d in designs if is_valid(patterns, d)]
    return len(valid_designs)


def count_all_combinations(patterns, designs):
    return sum(count_combinations(patterns, d) for d in designs)


if __name__ == "__main__":
    with open("input", "r") as f:
        patterns, designs = parse_designs(f.read())
    # print(count_valid_designs(patterns, designs))
    print(count_all_combinations(patterns, designs))