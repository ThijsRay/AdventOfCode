sample_input = '''forward 5
down 5
forward 8
up 3
down 8
forward 2
'''

def parse(input: str) -> list[tuple[str, int]]:
    lines = [line.split(" ") for line in input.splitlines()]
    return [(line[0], int(line[1])) for line in lines]

def star1(input: str) -> int:
    instructions = parse(input)
    horizontal = 0
    depth = 0
    for instruction, amount in instructions:
        if instruction == "forward": horizontal += amount
        if instruction == "down": depth += amount
        if instruction == "up": depth -= amount
    return horizontal * depth

def star2(input: str) -> int:
    instructions = parse(input)
    horizontal = 0
    depth = 0
    aim = 0
    for instruction, amount in instructions:
        if instruction == "forward": 
            horizontal += amount
            depth += aim*amount
        if instruction == "down": aim += amount
        if instruction == "up": aim -= amount
    return horizontal * depth

def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return "".join(f.readlines())

print("Day 2 - Star 1:", star1(read_file("input.txt")))
print("Day 2 - Star 2:", star2(read_file("input.txt")))
assert star1(sample_input) == 150
assert star2(sample_input) == 900
