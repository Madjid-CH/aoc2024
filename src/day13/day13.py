import re


def parse_input(input_):
    result = []
    for i in input_.split("\n\n"):
        result.append(parse_configuration(i))
    return result


def parse_configuration(conf):
    conf = conf.splitlines()
    result = dict()
    result["A"] = tuple(
        map(int, re.findall("Button A: X\+(\d+), Y\+(\d+)", conf[0])[0])
    )
    result["B"] = tuple(
        map(int, re.findall("Button B: X\+(\d+), Y\+(\d+)", conf[1])[0])
    )
    result["prize"] = tuple(map(int, re.findall("Prize: X=(\d+), Y=(\d+)", conf[2])[0]))
    return result


def count_tokens(input_):
    configurations = parse_input(input_)
    total = 0
    for conf in configurations:
        total += _count_tokens(conf)
    return total


def _count_tokens(conf):
    for a in range(100):
        for b in range(100):
            if (
                a * conf["A"][0] + b * conf["B"][0] == conf["prize"][0]
                and a * conf["A"][1] + b * conf["B"][1] == conf["prize"][1]
            ):
                return 3 * a + b
    return 0


def count_tokens2(input_):
    confs = parse_input(input_)
    update_prizes_locations(confs)
    total = 0
    for c in confs:
        c = _count_tokens2(c)
        total += c
    return total


def _count_tokens2(conf):
    # https://en.wikipedia.org/wiki/Cramer%27s_rule
    x = ((conf["prize"][0] * conf["B"][1]) - (conf["B"][0] * conf["prize"][1])) / (
        (conf["A"][0] * conf["B"][1]) - (conf["B"][0] * conf["A"][1])
    )
    y = ((conf["A"][0] * conf["prize"][1]) - (conf["prize"][0] * conf["A"][1])) / (
        (conf["A"][0] * conf["B"][1]) - (conf["B"][0] * conf["A"][1])
    )

    if int(x) == x and int(y) == y:
        return 3 * int(x) + int(y)
    return 0


def update_prizes_locations(confs):
    for c in confs:
        c["prize"] = (c["prize"][0] + 10000000000000, c["prize"][1] + 10000000000000)


if __name__ == "__main__":
    with open("input", "r") as f:
        print(count_tokens2(f.read()))