from collections import defaultdict


def parse_connections(connections):
    connections = connections.splitlines()
    return tuple(set(c.split("-")) for c in connections)


def solve1(connections):
    connections = get_3_connected(connections)
    connections = filter(is_t_in_connection, connections)
    return len(tuple(connections))


def get_3_connected(connections: tuple[set]):
    pcs = defaultdict(set)
    for c in connections:
        pc1, pc2 = tuple(c)
        pcs[pc1].add(pc2)
        pcs[pc2].add(pc1)
    triples = set()
    for pc1, cnx in pcs.items():
        for pc2 in cnx:
            for pc3 in pcs[pc2].intersection(cnx):
                triples.add(frozenset((pc1, pc2, pc3)))
    return triples


def is_t_in_connection(connection):
    for pc in connection:
        if pc.startswith("t"):
            return True
    return False


def solve2(connections):
    def build_set(conn: str, group: set[str]):
        password = ",".join(sorted(group))
        if password in passwords:
            return
        passwords.add(password)
        for pc in pcs[conn]:
            if pc in group:
                continue
            if any(pc not in pcs[node] for node in group):
                continue
            build_set(pc, {*group, pc})

    pcs = defaultdict(set)
    for c in connections:
        pc1, pc2 = tuple(c)
        pcs[pc1].add(pc2)
        pcs[pc2].add(pc1)

    passwords = set()
    for p in pcs:
        build_set(p, {p})
    return max(passwords, key=len)


if __name__ == "__main__":
    with open("input", "r") as f:
        connections = parse_connections(f.read())
    print(solve2(connections))
