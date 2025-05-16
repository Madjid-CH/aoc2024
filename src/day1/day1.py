from collections import Counter


def parse_input(input_: str):
    lines = input_.splitlines()
    rl, ll = [], []
    for line in lines:
        r, l = parse_line(line)
        rl.append(r)
        ll.append(l)
    return rl, ll


def parse_line(line):
    line = line.split(" ")
    return int(line[0]), int(line[-1])


def compute_distance(rl: list, ll: list):
    rl.sort(), ll.sort()
    distance = 0
    for r, l in zip(rl, ll):
        distance += abs(r - l)
    return distance


def solve1(input_):
    rl, ll = parse_input(input_)
    return compute_distance(rl, ll)


def similarity_score(rl, ll):
    coefficients = Counter(ll)
    return sum(r * coefficients[r] for r in rl)


def solve2(input_):
    rl, ll = parse_input(input_)
    return similarity_score(rl, ll)


if __name__ == "__main__":
    with open("input", "r") as file:
        print(solve2(file.read()))
