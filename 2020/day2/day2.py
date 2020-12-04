def parse(string):
    string = string.strip().split(' ')
    string[0] = [int(x) for x in string[0].split('-')]
    string[1] = string[1][:-1]
    return string

def part1(string: str):
    string = [parse(x) for x in string]
    return sum([is_valid_part1(entry) for entry in string])

def is_valid_part1(entry):
    amount = entry[2].count(entry[1])
    return amount >= entry[0][0] and amount <= entry[0][1]

def part2(string: str):
    string = [parse(x) for x in string]
    return sum([is_valid_part2(entry) for entry in string])

def is_valid_part2(entry):
    letter = entry[1]
    i = entry[0][0] - 1
    j = entry[0][1] - 1
    return bool(entry[2][i] == letter) ^ bool(entry[2][j] == letter)

if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.readlines()
        print(part1(string))
        print(part2(string))
