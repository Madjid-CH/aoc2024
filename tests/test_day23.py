from src.day23.day23 import parse_connections, solve1, solve2


def example():
    with open("../src/day23/example") as f:
        return f.read()


def test_of_acceptance():
    connections = parse_connections(example())
    assert solve1(connections) == 7


def example2():
    return "ka-co\nta-co\nde-co\nta-ka\nde-ta\nka-de"


def test_of_acceptance2():
    assert solve2(parse_connections(example2())) == "co,de,ka,ta"


