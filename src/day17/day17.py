import re


def parse_input(input_):
    registers, program = input_.split("\n\n")
    registers = re.findall("Register ([ABC]): (\\d+)", registers)
    registers = {k: int(v) for k, v in registers}
    program = re.findall("(\\d)", program)
    program = [int(v) for v in program]
    return registers, program


def run(registers, program):
    pointer = 0
    output = []
    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]
        if opcode == 3:
            if registers["A"] != 0:
                pointer = opcodes[opcode](registers, operand)
                continue
        elif opcode == 5:
            output.append(opcodes[opcode](registers, operand))
        else:
            opcodes[opcode](registers, operand)
        pointer += 2

    return output


def combo_operand(registers, operand):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return registers["A"]
        case 5:
            return registers["B"]
        case 6:
            return registers["C"]
    assert False


def adv(registers, operand):
    registers["A"] >>= combo_operand(registers, operand)


def bxl(registers, operand):
    registers["B"] ^= operand


def bst(registers, operand):
    registers["B"] = combo_operand(registers, operand) % 8


def jnz(_registers, operand):
    return operand


def bxc(registers, _operand):
    registers["B"] ^= registers["C"]


def out(registers, operand):
    return combo_operand(registers, operand) % 8


def bdv(registers, operand):
    registers["B"] = int(registers["A"] >> combo_operand(registers, operand))


def cdv(registers, operand):
    registers["C"] = int(registers["A"] >> combo_operand(registers, operand))


opcodes = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}


def solve2(registers, program):
    candidates = [0]
    for l in range(len(program)):
        next_candidates = []
        for val in candidates:
            for i in range(8):
                target = (val << 3) + i
                registers["A"] = target
                if run(registers, program) == program[-l - 1:]:
                    next_candidates.append(target)
        candidates = next_candidates

    return min(candidates)


if __name__ == "__main__":
    with open("input", "r") as f:
        registers, program = parse_input(f.read())
        # print(",".join(map(str(run(registers, program)))))
        print(solve2(registers, program))
