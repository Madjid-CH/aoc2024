import re
from re import findall


def execute(input_):
    params = parse_input(input_)
    return sum(x * y for x, y in params)


def parse_input(input_: str):
    instructions = findall(r"mul\(\d+,\d+\)", input_)
    params = []
    for token in instructions:
        token = token.removeprefix("mul")
        params.append(eval(token))
    return params


def execute2(input_):
    params = parse_conditional_input(input_)
    result = 0
    enabled = True
    for i, p in enumerate(params):
        if p == "don't()":
            enabled = False
        if p == "do()":
            enabled = True
            continue
        if enabled:
            x, y = p
            result += x * y
    return result


def parse_conditional_input(input_: str):
    instructions = findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input_)
    params = []
    for token in instructions:
        token = token.removeprefix("mul")
        if token not in ("do()", "don't()"):
            params.append(eval(token))
        else:
            params.append(token)
    return params


if __name__ == "__main__":
    with open("input", "r") as f:
        print(execute2(f.read()))
