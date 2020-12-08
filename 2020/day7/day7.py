def parse(string: str):
    string = string.split("\n")
    string = [x.split("bags contain") for x in string]
    string = [[x.split(",") for x in y] for y in string]
    string = [[[x.strip() for x in y] for y in z] for z in string]
    bags = {}
    for i in string:
        if i == [['']]:
            continue
        key = i[0][0]
        values = i[1]
        if values[0] == "no other bags.":
            del values[0]
        values = [x.replace("bags", "").replace("bag", "").replace(".", "").strip() for x in values]
        bags[key] = values
    return bags

def part1(string: str):
    old_size = 0
    gold_list = {"shiny gold"}
    new_gold_list = set()
    for x in bags:
        for key in bags:
            for gold in gold_list:
                for bag in bags[key]:
                    if gold in bag:
                        new_gold_list.add(key)
            gold_list = gold_list | new_gold_list
    return len(gold_list) - 1

def amount_of_bags(bags, color):
    if bags[color] == []:
        return 1
    else:
        amount = 0
        for bag in bags[color]:
            bag = bag.split(" ")
            print(bag[0], bag[1:])
            amount += int(bag[0]) * amount_of_bags(bags, " ".join(bag[1:]))
        print()
        return 1+amount

def part2(bags: str):
    return amount_of_bags(bags, "shiny gold") - 1

if __name__ == "__main__":
    with open("input.txt") as f:
        bags = parse(f.read())
        #print(part1(bags))
        print(part2(bags))
