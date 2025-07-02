from collections import namedtuple, deque


def parse_input(input_):
    lines = input_.splitlines()
    return [tuple(map(int, line.split(",")))[::-1] for line in lines]


State = namedtuple("State", ["r", "c", "distance"])


def count_steps(fallen_blocks, grid_dim):
    queue = deque([State(0, 0, 0)])
    seen = set()
    while queue:
        state = queue.popleft()
        if (state.r, state.c) in seen:
            continue
        seen.add((state.r, state.c))
        if state.r == grid_dim[0] - 1 and state.c == grid_dim[1] - 1:
            return state.distance
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = state.r + dr, state.c + dc
            if (
                0 <= nr < grid_dim[0]
                and 0 <= nc < grid_dim[1]
                and (nr, nc) not in fallen_blocks
            ):
                queue.append(State(nr, nc, state.distance + 1))

    return -1


def get_blocking_coordinates(blocks, grid_dim):
    lo, hi = 0, len(blocks) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if count_steps(blocks[: mid + 1], grid_dim) != -1:
            lo = mid + 1
        else:
            hi = mid
    return blocks[lo]


if __name__ == "__main__":
    with open("input", "r") as f:
        blocks = parse_input(f.read())
    # print(count_steps(blocks[:1024], (71, 71)))
    print(get_blocking_coordinates(blocks, (71, 71)))
