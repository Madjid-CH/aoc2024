from collections import Counter


def compute_checksum(disk_map):
    disk_map = parse_disk_map(disk_map)
    disk_map = compact_disk_map(disk_map)
    disk_map = fragment_blocks(disk_map)
    return sum(b * i for i, b in enumerate(disk_map) if isinstance(b, int))


def parse_disk_map(disk_map):
    return [int(p) for p in (list(disk_map))]


def compact_disk_map(disk_map):
    result = list()
    for i, blocks in enumerate(disk_map):
        if i % 2 == 0:
            result.extend(i // 2 for _ in range(blocks))
        else:
            result.extend("." for _ in range(blocks))
    return result


def fragment_blocks(expanded_map: list):
    for i, block in enumerate(reversed(expanded_map)):
        if isinstance(block, int):
            i_free = expanded_map.index(".")
            if len(expanded_map) - i - 1 < i_free:
                break
            expanded_map[i_free] = block
            expanded_map[-i - 1] = "."
    return expanded_map


def fragment_files(expanded_map: list):
    empty_blocks = get_empty_blocks(expanded_map)
    file_sizes = Counter(expanded_map)
    file_sizes.pop(".")
    file_sizes = sorted(file_sizes.items(), key=lambda t: t[0], reverse=True)
    for file_size in file_sizes:
        block, size = file_size
        for i, empty_block in enumerate(empty_blocks):
            if size <= empty_block[1]:
                j = expanded_map.index(block)
                if empty_block[0] > j:
                    break
                for ii in range(size):
                    expanded_map[empty_block[0] + ii] = block
                    expanded_map[j + ii] = "."
                empty_blocks[i] = (empty_block[0] + size, empty_block[1] - size)
                break
    return expanded_map


def get_empty_blocks(expanded_map):
    result = []
    i = expanded_map.index(".")
    size = 0
    while i < len(expanded_map):
        if expanded_map[i] == ".":
            size += 1
        elif size > 0:
            result.append((i - size, size))
            size = 0
        i += 1

    return result


def compute_checksum2(disk_map):
    disk_map = parse_disk_map(disk_map)
    disk_map = compact_disk_map(disk_map)
    disk_map = fragment_files(disk_map)
    return sum(b * i for i, b in enumerate(disk_map) if isinstance(b, int))


if __name__ == "__main__":
    with open("input", "r") as f:
        print(compute_checksum2(f.read()))

