def parse(string: str):
    string = [x.strip().split() for x in string]
    return string

def execute(instructions, line, accumulator):
    instruction = instructions[line]
    operation = instruction[0]
    arguments = instruction[1:]

    if operation == "acc":
        accumulator += int(arguments[0])
    elif operation == "jmp":
        line += int(arguments[0]) - 1
    elif operation == "nop":
        pass
    return line + 1, accumulator

def part1(string: str):
    visited_lines = {0}
    line = 0
    acc = 0
    while True:
        line, acc = execute(string, line, acc)
        if line in visited_lines:
            return acc
        else:
            visited_lines.add(line)
    return acc

def swap_instructions(instructions, index, a, b):
    if instructions[index][0] == a:
        instructions[index][0] = "REPLACE THIS"
    if instructions[index][0] == b:
        instructions[index][0] = a
    if instructions[index][0] == "REPLACE THIS":
        instructions[index][0] = b
    return instructions

def part2(string: str):
    for i in range(len(string)):
        instructions = swap_instructions(string, i, "jmp", "nop")
        print(instructions)

        visited_lines = {0}
        loop = False
        line = 0
        acc = 0
        while True:
            line, acc = execute(instructions, line, acc)
            # Line number is the after the last line, we terminated
            if line == len(instructions):
                return acc
            if line in visited_lines:
                loop = True
                break
            else:
                visited_lines.add(line)

        instructions = swap_instructions(string, i, "jmp", "nop")

if __name__ == "__main__":
    with open("input.txt") as f:
        string = parse(f.readlines())
        print(part1(string))
        print(part2(string))
