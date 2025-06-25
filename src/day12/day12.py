from collections import deque


def fence_price(garden):
    regions = get_regions(parse_garden(garden))
    return sum(len(region) * perimeter(region) for region in regions)


def parse_garden(garden):
    return [list(row) for row in garden.splitlines()]


def get_regions(garden):
    regions = []
    seen = set()
    num_rows = len(garden)
    num_cols = len(garden[0])
    for r in range(num_rows):
        for c in range(num_cols):
            if (r, c) in seen:
                continue

            region = set()
            queue = deque([(r, c)])
            while queue:
                current_r, current_c = queue.popleft()
                region.add((current_r, current_c))

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_r = current_r + dr
                    next_c = current_c + dc
                    if (
                        (next_r, next_c) not in seen
                        and 0 <= next_r < num_rows
                        and 0 <= next_c < num_cols
                        and garden[next_r][next_c] == garden[current_r][current_c]
                    ):
                        queue.append((next_r, next_c))
                        seen.add((next_r, next_c))

            regions.append(region)

    return regions


def perimeter(region: set[tuple[int]]) -> int:
    total = 0
    for r, c in region:
        num_neighbors = sum(
            (r + dr, c + dc) in region for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
        )
        total += 4 - num_neighbors
    return total


def price_with_discount(garden):
    regions = get_regions(parse_garden(garden))
    return sum(len(r) * sides(r) for r in regions)


def sides(region: set[tuple[int]]) -> int:
    up, down, left, right = get_region_borders(region)
    count = 0
    for r, c in up:
        if (r, c) in left:
            count += 1
        if (r, c) in right:
            count += 1
        if (r - 1, c - 1) in right and (r, c) not in left:
            count += 1
        if (r - 1, c + 1) in left and (r, c) not in right:
            count += 1

    for r, c in down:
        if (r, c) in left:
            count += 1
        if (r, c) in right:
            count += 1
        if (r + 1, c - 1) in right and (r, c) not in left:
            count += 1
        if (r + 1, c + 1) in left and (r, c) not in right:
            count += 1

    return count


def get_region_borders(region):
    up, down, left, right = (set() for _ in range(4))
    for r, c in region:
        if (r - 1, c) not in region:
            up.add((r, c))
        if (r + 1, c) not in region:
            down.add((r, c))
        if (r, c - 1) not in region:
            left.add((r, c))
        if (r, c + 1) not in region:
            right.add((r, c))
    return up, down, left, right


if __name__ == "__main__":
    with open("input", "r") as f:
        print(price_with_discount(f.read()))
