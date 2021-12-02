from copy import deepcopy

def parse(string: str):
    return string

def part1(values):
    pass

def part2(values):
    pass

if __name__ == "__main__":
    with open("input.txt") as f:
        values = parse(f.read())
        print(values)
        print(part1(deepcopy(values)))
        print(part2(deepcopy(values)))
