def parse(string: str):
    string = [int(x.strip()) for x in string]
    return string

def part1(values: str):
    window = 25
    for idx in range(window, len(values)):
        preamble = values[idx:idx+window]
        target = values[min(idx+window, len(values)-1)]
        if not any([(x is not y) and (x + y == target) for x in preamble for y in preamble]):
            return target
        

def part2(values: str, target: int):
    for start in range(len(values)):
        for end in range(start, len(values)):
            result = sum(values[start:end])
            if result > target:
                break
            if result == target:
                set = sorted(values[start:end])
                return set[0] + set[len(set)-1]

if __name__ == "__main__":
    with open("input.txt") as f:
        string = parse(f.readlines())
        target = part1(string)
        print(target)
        print(part2(string, target))
