import re
from dataclasses import dataclass


@dataclass
class Connection:
    ins: list[str]
    op: str
    out: str

    def __str__(self) -> str:
        return f"{self.out} = {self.ins[0]} {self.op} {self.ins[1]}"

    def __eq__(self, other) -> bool:
        return self.ins == other.ins and self.op == other.op


operations = {
    "OR": lambda x1, x2: x1 | x2,
    "AND": lambda x1, x2: x1 & x2,
    "XOR": lambda x1, x2: x1 ^ x2,
}


def parse_input(input_):
    init_pairs = re.findall(r"(.{3}): ([01])", input_)
    initials = {k: int(v) for k, v in init_pairs}
    wire_map = {}
    for line in input_.split("\n\n")[1].splitlines():
        in1, op, in2, _, out = line.split(" ")
        wire_map[out] = Connection([in1, in2], op, out)
    return initials, wire_map


def solve1(initials, wire_map):
    def run_wire(wire):
        if wire in initials:
            return initials[wire]
        connection = wire_map[wire]
        return operations[connection.op](
            run_wire(connection.ins[0]), run_wire(connection.ins[1])
        )

    result = [
        run_wire(w)
        for w in sorted([w for w in wire_map if w.startswith("z")], reverse=True)
    ]
    return int("".join(map(str, result)), 2)


def solve2(wire_map):
    def validate(n: int) -> bool:
        for x in range(2):
            for y in range(2):
                for c in range(2):
                    init_x = [0] * (44 - n) + [x]
                    init_y = [0] * (44 - n) + [y]
                    if n > 0:
                        init_x += [c] + [0] * (n - 1)
                        init_y += [c] + [0] * (n - 1)
                    elif c > 0:
                        continue
                    init_x, init_y = list(reversed(init_x)), list(reversed(init_y))
                    z = run_wire2(make_wire("z", n), {"x": init_x, "y": init_y})
                    if z != (x + y + c) % 2:
                        return False
        return True

    def run_wire2(w: str, init: dict[list[int]]) -> int:
        if res := re.match(r"(x|y)(\d{2})", w):
            var, num = res.groups()
            return init[var][int(num)]
        conn = wire_map[w]
        return operations[conn.op](
            run_wire2(conn.ins[0], init), run_wire2(conn.ins[1], init)
        )

    def find_wire(
        op: str | None = None, in1: str | None = None, in2: str | None = None
    ):
        for wire in wire_map.values():
            if op and op != wire.op:
                continue
            if in1 and in1 not in wire.ins:
                continue
            if in2 and in2 not in wire.ins:
                continue
            return wire

    def swap(w1: str, w2: str) -> None:
        wire_map[w1], wire_map[w2] = wire_map[w2], wire_map[w1]

    def make_wire(var, num):
        return var + str(num).zfill(2)

    def fix_bit_n(n: int) -> list[str]:
        """
        zn = nxor XOR m1
        nxor = xn XOR yn
        m1 = m2 OR prevand
        prevand = xn-1 AND yn-1
        m2 = prevxor AND (something else from prev)
        prevxor = xn-1 XOR yn-1

        know m2 is good or would have crashed on prev validation
        """
        print(f"Issue with n = {n}")
        prevand = find_wire(
            op="AND", in1=make_wire("x", n - 1), in2=make_wire("y", n - 1)
        )
        prevxor = find_wire(
            op="XOR", in1=make_wire("x", n - 1), in2=make_wire("y", n - 1)
        )
        m2 = find_wire(op="AND", in1=prevxor.out)
        m1 = find_wire(op="OR", in1=m2.out, in2=prevand.out)
        nxor = find_wire("XOR", in1=make_wire("x", n), in2=make_wire("y", n))
        zn = find_wire(op="XOR", in1=nxor.out, in2=m1.out)
        if zn is None:
            zn = wire_map[make_wire("z", n)]
            to_swap = list(set(zn.ins) ^ set([nxor.out, m1.out]))
        if zn.out != make_wire("z", n):
            to_swap = [make_wire("z", n), zn.out]
        swap(*to_swap)
        return to_swap

    result = []
    for i in range(45):
        if validate(i):
            continue
        result.extend(fix_bit_n(i))
    return ",".join(sorted(result))


if __name__ == "__main__":
    with open("input", "r") as f:
        initials, wire_map = parse_input(f.read())
    print(solve2(wire_map))