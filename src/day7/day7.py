import math
from itertools import product, combinations_with_replacement


def total_calibration(input_):
    equations = parse_input(input_)
    return sum(
        value
        for value, numbers in equations.items()
        if is_true_equation(value, numbers)
    )


def parse_input(input_):
    result = dict()
    for line in input_.splitlines():
        line = line.split(":")
        numbers = line[1].strip().split()
        result[int(line[0])] = tuple(int(n) for n in numbers)
    return result


def is_true_equation(value, numbers):
    for eq in product([sum, math.prod, concat], repeat=len(numbers) - 1):
        result = numbers[0]
        for n, op in zip(numbers[1:], eq):
            result = op((result, n))

        if result == value:
            return True
    return False


def concat(l):
    return int("".join([str(n) for n in l]))


if __name__ == "__main__":
    with open("input", "r") as f:
        print(total_calibration(f.read()))
