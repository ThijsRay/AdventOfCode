def part1(string: str):
    string = [int(x) for x in string]
    for x in string:
        for y in string:
            if x + y == 2020:
                return x * y

def part2(string: str):
    string = [int(x) for x in string]
    for x in string:
        for y in string:
            for z in string:
                if x + y + z == 2020:
                    return x * y * z

if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.readlines()
        print(part1(string))
        print(part2(string))
