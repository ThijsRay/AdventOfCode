def parse(string: str):
    string = [int(x.strip()) for x in string]
    return sorted(string)

def device(values):
    return values[len(values)-1] + 3


def part1(values):
    next_values = values[1:]
    next_values.append(device(values))
    differences = [y-x for x,y in zip(values, next_values)]
    jolts1 = differences.count(1) + values[0]
    jolts3 = differences.count(3)
    return jolts1 * jolts3

def previous_steps(values, steps, idx, step):
    if idx - step >= 0:
        if values[idx] - values[idx-step] <= 3:
            return steps[idx-step]
    return 0

def part2(values):
    values = [0] + values + [device(values)]
    steps = [0]*len(values)
    steps[0] = 1
    for idx in range(1, len(values)):
        steps[idx] = sum([previous_steps(values, steps, idx, x) for x in range(1,4)])
    return max(steps)

if __name__ == "__main__":
    with open("input.txt") as f:
        string = parse(f.readlines())
        print(string)
        print(part1(string))
        print(part2(string))
