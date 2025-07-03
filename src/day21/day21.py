from collections import deque
from functools import cache
from itertools import product


def parse_codes(codes):
    return codes.splitlines()


def sum_complexities(codes):
    return sum(int(code[:-1]) * get_complexity(code) for code in codes)


num_pad = {
    (0, 0): "7",
    (0, 1): "8",
    (0, 2): "9",
    (1, 0): "4",
    (1, 1): "5",
    (1, 2): "6",
    (2, 0): "1",
    (2, 1): "2",
    (2, 2): "3",
    (3, 1): "0",
    (3, 2): "A",
}
dir_pad = {
    (0, 1): "^",
    (0, 2): "A",
    (1, 0): "<",
    (1, 1): "v",
    (1, 2): ">",
}


def find_best_path(keypad, from_: tuple[int, int], to):
    if from_ == to:
        return ["A"]
    # state = r, c, path
    queue = deque([(*from_, "")])
    best_length = 100
    optimal_paths = []
    while queue:
        r, c, path = queue.popleft()
        for nr, nc, move in (
            (r + 1, c, "v"),
            (r - 1, c, "^"),
            (r, c + 1, ">"),
            (r, c - 1, "<"),
        ):
            if (nr, nc) not in keypad:
                continue
            if len(path) + 1 > best_length:
                return optimal_paths
            if (nr, nc) == to:
                optimal_paths.append(path + move + "A")
                best_length = min(len(path) + 2, best_length)
            else:
                queue.append((nr, nc, path + move))

    return optimal_paths


num_pad_paths = {
    (num_pad[p1], num_pad[p2]): find_best_path(num_pad, p1, p2)
    for p1 in num_pad
    for p2 in num_pad
}
dir_pad_paths = {
    (dir_pad[p1], dir_pad[p2]): find_best_path(dir_pad, p1, p2)
    for p1 in dir_pad
    for p2 in dir_pad
}


def get_complexity(code):
    best_length = float("inf")
    for path1 in get_paths_for_code(num_pad_paths, code):
        for path2 in get_paths_for_code(dir_pad_paths, path1):
            for path3 in get_paths_for_code(dir_pad_paths, path2):
                best_length = min(len(path3), best_length)
    return best_length


def get_paths_for_code(keypad_paths, code):
    paths = [keypad_paths[(b1, b2)] for b1, b2 in zip("A" + code, code)]
    return ["".join(segment) for segment in product(*paths)]


@cache
def get_length(code, depth):
    if depth == 0:
        return len(code)
    length = 0
    for p1, p2 in zip("A" + code, code):
        length += min(get_length(seq, depth - 1) for seq in dir_pad_paths[(p1, p2)])
    return length


def solve2(codes, depth):
    result = 0
    for code in codes:
        best_length = float("inf")
        for path in get_paths_for_code(num_pad_paths, code):
            best_length = min(best_length, get_length(path, depth))
        result += int(code[:-1]) * best_length
    return result


if __name__ == "__main__":
    with open("input", "r") as f:
        codes = parse_codes(f.read())
    # print(sum_complexities(codes))
    print(solve2(codes, 25))
