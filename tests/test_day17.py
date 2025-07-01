from src.day17.day17 import run, parse_input, solve2

example = "Register A: 729\nRegister B: 0\nRegister C: 0\n\nProgram: 0,1,5,4,3,0"


def test_of_acceptance():
    registers, program = parse_input(example)
    assert run(registers, program) == [4, 6, 3, 5, 6, 3, 5, 2, 1, 0]


def test_parse_input():
    assert parse_input(example) == ({"A": 729, "B": 0, "C": 0}, [0, 1, 5, 4, 3, 0])


example2 = "Register A: 2024\nRegister B: 0\nRegister C: 0\n\nProgram: 0,3,5,4,3,0"


def test_of_acceptance2():
    registers, program = parse_input(example2)
    print(run(registers, program))
    assert solve2(registers, program) == 117440
