from collections import defaultdict


def parse_input(numbers):
    return list(map(int, numbers.splitlines()))


def solve1(numbers):
    result = 0
    for n in numbers:
        for _ in range(2000):
            n = next_num(n)
        result += n
    return result


def next_num(n):
    n ^= (n * 64) % 16777216
    n ^= (n // 32) % 16777216
    n ^= (n * 2048) % 16777216
    return n


def solve2(numbers):
    seq_totals = defaultdict(int)
    for num in numbers:
        seen = set()
        outputs = []
        for _ in range(2001):
            outputs.append(num % 10)
            num = next_num(num)
        diffs = [y - x for x, y in zip(outputs, outputs[1:])]
        for n, *seq in zip(outputs[4:], diffs, diffs[1:], diffs[2:], diffs[3:]):
            seq = tuple(seq)
            if seq in seen:
                continue
            seq_totals[seq] += n
            seen.add(seq)

    return max(seq_totals.values())


if __name__ == "__main__":
    with open("input", "r") as f:
        numbers = parse_input(f.read())
    # print(solve1(numbers))
    print(solve2(numbers))