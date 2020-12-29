from copy import deepcopy

def parse(string: str):
    values = [int(x) for x in string.strip().split(',')]
    return {values[x]: x for x in range(len(values))}

def next_number(last_number, index, values):
    return_value = 0
    if values.get(last_number) != None:
        return_value = index - values[last_number]
    values[last_number] = index
    return (return_value, values)
assert(next_number(6, 2, {0:0, 3:1, 6:2}) == (0, {0:0, 3:1, 6:2}))
assert(next_number(0, 3, {0:0, 3:1, 6:2}) == (3, {0:3, 3:1, 6:2}))
assert(next_number(3, 4, {0:3, 3:1, 6:2}) == (3, {0:3, 3:4, 6:2}))
assert(next_number(3, 5, {0:3, 3:4, 6:2}) == (1, {0:3, 3:5, 6:2}))
assert(next_number(1, 6, {0:3, 3:5, 6:2}) == (0, {0:3, 3:5, 6:2, 1:6}))
assert(next_number(0, 7, {0:3, 3:5, 6:2, 1:6}) == (4, {0:7, 3:5, 6:2, 1:6}))
assert(next_number(4, 8, {0:7, 3:5, 6:2, 1:6}) == (0, {0:7, 3:5, 6:2, 1:6, 4:8}))

def get_nth_element(values, nth):
    last_element = max(values, key=values.get)
    print(last_element, values)
    for i in range(len(values)-1, nth-1):
        last_element, values = next_number(last_element, i, values)
    return last_element

def part1(values):
    return get_nth_element(values, 2020)
assert(part1(parse("0,3,6")) == 436)
assert(part1(parse("1,3,2")) == 1)
assert(part1(parse("2,1,3")) == 10)
assert(part1(parse("1,2,3")) == 27)
assert(part1(parse("2,3,1")) == 78)
assert(part1(parse("3,2,1")) == 438)
assert(part1(parse("3,1,2")) == 1836)

def part2(values):
    return get_nth_element(values, 30000000)
assert(part2(parse("0,3,6")) == 175594)
assert(part2(parse("1,3,2")) == 2578)
assert(part2(parse("2,1,3")) == 3544142)
assert(part2(parse("1,2,3")) == 261214)
assert(part2(parse("2,3,1")) == 6895259)
assert(part2(parse("3,2,1")) == 18)
assert(part2(parse("3,1,2")) == 362)

if __name__ == "__main__":
    with open("input.txt") as f:
        values = parse(f.read())
        print(part1(deepcopy(values)))
        print(part2(deepcopy(values)))
