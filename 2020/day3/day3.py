def part1(string: str):
    return trees_for_slope(string, 3, 1)

def part2(string: str):
    product = 1 
    product *= trees_for_slope(string, 1, 1)
    product *= trees_for_slope(string, 3, 1)
    product *= trees_for_slope(string, 5, 1)
    product *= trees_for_slope(string, 7, 1)
    product *= trees_for_slope(string, 1, 2)
    return product

def trees_for_slope(string, x_slope, y_slope):
    x = 0
    y = 0
    trees = 0
    while y < len(string)-1:
        if tree_on_position(string, x, y):
            trees += 1
        x += x_slope
        y += y_slope
    return trees

def tree_on_position(string, x, y) -> bool:
    return string[y][x % determine_pattern_length(string)] == "#"

def determine_pattern_length(string):
    return len(string[0])

if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.read().split('\n')
        print(part1(string))
        print(part2(string))
