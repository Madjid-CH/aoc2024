from functools import partial


def solve1(input_):
    rules, updates = input_.split("\n\n")
    rules = parse_rules(rules)
    updates = parse_printing_order(updates)
    correct_updates = filter(partial(correctly_ordered, rules=rules), updates)
    middle_pages = map(middle_page, correct_updates)
    return sum(middle_pages)


def middle_page(pages):
    return pages[len(pages) // 2]


def parse_rules(input_):
    rules = dict()
    for rule in input_.splitlines():
        rule = rule.split("|")
        p1, p2 = int(rule[0]), int(rule[1])
        if rules.get(p1):
            rules[p1].add(p2)
        else:
            rules[p1] = {p2}
    return rules


def parse_printing_order(input_):
    result = []
    for line in input_.splitlines():
        line = line.split(",")
        result.append(tuple(int(page) for page in line))
    return result


def correctly_ordered(update: tuple, rules: dict):
    for i, page in enumerate(update):
        if rule := rules.get(page):
            if len(rule.intersection(set(update[:i]))) > 0:
                return False
    return True


def solve2(input_):
    rules, updates = input_.split("\n\n")
    rules = parse_rules(rules)
    updates = parse_printing_order(updates)
    incorrect_updates = filter(partial(incorrectly_ordered, rules=rules), updates)
    correct_updates = map(partial(correct, rules=rules), incorrect_updates)
    middle_pages = map(middle_page, correct_updates)
    return sum(middle_pages)


def incorrectly_ordered(update, rules):
    return not correctly_ordered(update, rules)


def correct(update, rules):
    update = list(update)
    for i, page in enumerate(update):
        if rule := rules.get(page):
            while len(rule.intersection(set(update[:i]))) > 0:
                swap(update, i)
                i -= 1
    return tuple(update)


def swap(update, i):
    update[i - 1], update[i] = update[i], update[i - 1]


if __name__ == "__main__":
    with open("input", "r") as f:
        print(solve2(f.read()))
