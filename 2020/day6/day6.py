def parse(string: str):
    string = string.split("\n\n")
    string = [x.split("\n") for x in string]
    string = [" ".join(x).strip().split(" ") for x in string]
    return string

def part1(string: str):
    return sum([len(set("".join(x))) for x in string])

def part2(answers: str):
    total = 0
    for group in answers:
        amount = dict()
        for person in group:
            for answer in person:
                if answer not in amount:
                    amount[answer] = 1
                else:
                    amount[answer] += 1
        total += sum([amount[x] == len(group) for x in amount])
    return total

if __name__ == "__main__":
    with open("input.txt") as f:
        string = parse(f.read())
        #print(string)
        print(part1(string))
        print(part2(string))
