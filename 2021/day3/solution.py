from copy import deepcopy

sample_input = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''

def parse(input: str) -> list[list[int]]:
    lines = [x for x in input.splitlines()]
    return [[int(digit, 2) for digit in line] for line in lines]

def invert(ints: list[int]) -> list[int]:
    return [(x+1)%2 for x in ints]

def to_decimal(ints: list[int]) -> int:
    return int("".join([str(x) for x in ints]), 2)

def most_common(digits: list[list[int]]) -> list[int]:
    amount = [0]*len(digits[0])
    for line in digits:
        for idx in range(len(line)):
            digit = line[idx]
            if digit == 0:
                amount[idx] -= 1
            if digit == 1:
                amount[idx] += 1

    for idx in range(len(amount)):
        if amount[idx] < 0:
            amount[idx] = 0
        elif amount[idx] > 0:
            amount[idx] = 1
        else:
            amount[idx] = 1
    return amount


def star1(input: str) -> int:
    digits = parse(input)
    amount = most_common(digits)

    gamma = to_decimal(amount)
    epsilon = to_decimal(invert(amount))
    return gamma * epsilon

def star2(input: str) -> int:
    digits = parse(input)
    
    # Collect all digits that are relevant for this iteration
    oxygen = deepcopy(digits)

    for idx in range(len(oxygen[0])):
        # Calculate the most common bit in the nth position for the nth iteration
        common = most_common(oxygen)
        # Filter out all digits that don't match
        oxygen = [digit for digit in oxygen if digit[idx] == common[idx]]

    assert len(oxygen) == 1
    oxygen = to_decimal(oxygen[0])

    co2 = deepcopy(digits)
    for idx in range(len(co2[0])):
        least_common = invert(most_common(co2))
        co2 = [digit for digit in co2 if digit[idx] == least_common[idx]]
        if len(co2) == 1:
            break

    assert len(co2) == 1
    co2 = to_decimal(co2[0])
    return oxygen * co2
    

def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return "".join(f.readlines())

print("Day 3 - Star 1:", star1(read_file("input.txt")))
print("Day 3 - Star 2:", star2(read_file("input.txt")))
assert star1(sample_input) == 198
assert star2(sample_input) == 230
