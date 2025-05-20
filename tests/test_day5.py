from pytest import mark

from src.day5.day5 import (
    solve1,
    parse_rules,
    parse_printing_order,
    correctly_ordered,
    solve2,
    correct,
)

example = (
    "47|53\n"
    "97|13\n"
    "97|61\n"
    "97|47\n"
    "75|29\n"
    "61|13\n"
    "75|53\n"
    "29|13\n"
    "97|29\n"
    "53|29\n"
    "61|53\n"
    "97|53\n"
    "61|29\n"
    "47|13\n"
    "75|47\n"
    "97|75\n"
    "47|61\n"
    "75|61\n"
    "47|29\n"
    "75|13\n"
    "53|13\n"
    "\n"
    "75,47,61,53,29\n"
    "97,61,53,29,13\n"
    "75,29,13\n"
    "75,97,47,61,53\n"
    "61,13,29\n"
    "97,13,75,29,47"
)


def test_of_acceptance():
    assert solve1(example) == 143


@mark.parametrize(
    "input_, expected",
    [
        ("1|2", {1: {2}}),
        ("1|2\n3|4", {1: {2}, 3: {4}}),
        ("1|2\n1|3", {1: {2, 3}}),
    ],
)
def test_parse_rules(input_, expected):
    assert parse_rules(input_) == expected


@mark.parametrize(
    "input_, expected",
    [
        ("1,2,3", [(1, 2, 3)]),
        (
            "75,47,61,53,29\n97,61,53,29,13\n",
            [(75, 47, 61, 53, 29), (97, 61, 53, 29, 13)],
        ),
    ],
)
def test_parse_printing_order(input_, expected):
    assert parse_printing_order(input_) == expected


def get_rules_from_example():
    rules = example.split("\n\n")[0]
    return parse_rules(rules)


def get_updates_from_example():
    updates = example.split("\n\n")[1]
    return parse_printing_order(updates)


@mark.parametrize(
    "updates, rules, expected",
    [
        ((1, 2), {1: {2}}, True),
        ((2, 1), {1: {2}}, False),
        ((3, 1, 2), {1: {2, 3}}, False),
        ((4, 1, 2), {1: {2, 3}}, True),
        (get_updates_from_example()[0], get_rules_from_example(), True),
        (get_updates_from_example()[1], get_rules_from_example(), True),
        (get_updates_from_example()[2], get_rules_from_example(), True),
        (get_updates_from_example()[3], get_rules_from_example(), False),
        (get_updates_from_example()[4], get_rules_from_example(), False),
        (get_updates_from_example()[5], get_rules_from_example(), False),
    ],
)
def test_correctly_ordered(updates, rules, expected):
    assert correctly_ordered(updates, rules) == expected


def test_of_acceptance2():
    assert solve2(example) == 123


@mark.parametrize(
    "update, rules, expected",
    [
        ((1, 2), {1: {2}}, (1, 2)),
        ((2, 1), {1: {2}}, (1, 2)),
        ((3, 1, 2), {1: {2, 3}}, (1, 3, 2)),
        ((4, 1, 2), {1: {2, 3}}, (4, 1, 2)),
        ((3, 2, 1), {1: {2, 3}}, (1, 3, 2)),
        ((75, 97, 47, 61, 53), get_rules_from_example(), (97, 75, 47, 61, 53)),
        ((61, 13, 29), get_rules_from_example(), (61, 29, 13)),
        ((97, 13, 75, 29, 47), get_rules_from_example(), (97, 75, 47, 29, 13)),
    ],
)
def test_correct(update, rules, expected):
    assert correct(update, rules) == expected
