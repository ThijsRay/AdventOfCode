from enum import Enum
from copy import deepcopy

class Seat(Enum):
    FREE = "L"
    OCCUPIED = "#"
    FLOOR = "."

    @classmethod
    def into(cls, value):
        if value == "L":
            return cls.FREE
        elif value == "#":
            return cls.OCCUPIED
        return cls.FLOOR

    def __repr__(self):
        return f"{self.value}"

def parse(string: str):
    string = [x.strip() for x in string]
    string = [[Seat.into(x) for x in y] for y in string]
    return string

def get_adjacent_1(values, x_coord, y_coord):
    adjacent = list()
    offsets = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]
    for x, y in [(x_coord+i,y_coord+j) for i,j in offsets]:
        if in_bound(values, x, y):
            adjacent.append((x,y))
    return adjacent

def in_bound(values, x, y):
    if x < 0: return False
    if y < 0: return False
    if y >= len(values): return False
    if x >= len(values[y]): return False
    return True

# This is a horrible and error prone solution but it is AoC so if it works, it is fine
def get_adjacent_2(values, x_coord, y_coord):
    adjacent = list()
    # North
    x = x_coord
    y = y_coord - 1
    while in_bound(values, x, y):
        if values[y][x] != Seat.FLOOR:
            adjacent.append((x, y))
            break
        y -= 1
    # North-East
    x = x_coord + 1
    y = y_coord - 1
    while in_bound(values, x, y):
        if values[y][x] != Seat.FLOOR:
            adjacent.append((x, y))
            break
        x += 1
        y -= 1
    # East
    x = x_coord + 1
    y = y_coord
    while in_bound(values, x, y):
        if values[y][x] != Seat.FLOOR:
            adjacent.append((x, y))
            break
        x += 1
    # South-East
    x = x_coord + 1
    y = y_coord + 1
    while in_bound(values, x, y):
        if values[y][x] != Seat.FLOOR:
            adjacent.append((x, y))
            break
        x += 1
        y += 1
    # South
    x = x_coord
    y = y_coord + 1
    while in_bound(values, x, y):
        if values[y][x] != Seat.FLOOR:
            adjacent.append((x, y))
            break
        y += 1
    # South-West
    x = x_coord - 1
    y = y_coord + 1
    while in_bound(values, x, y):
        if values[y][x] != Seat.FLOOR:
            adjacent.append((x, y))
            break
        x -= 1
        y += 1
    # West
    x = x_coord - 1
    y = y_coord
    while in_bound(values, x, y):
        if values[y][x] != Seat.FLOOR:
            adjacent.append((x, y))
            break
        x -= 1
    # North-West
    x = x_coord - 1
    y = y_coord - 1
    while in_bound(values, x, y):
        if values[y][x] != Seat.FLOOR:
            adjacent.append((x, y))
            break
        x -= 1
        y -= 1

    return adjacent


def iterate(values, get_adjacent, max_allowed):
    new_values = deepcopy(values)

    for y in range(len(values)):
        for x in range(len(values[y])):
            amount_occupied = sum([values[adj_y][adj_x] == Seat.OCCUPIED for (adj_x, adj_y) in get_adjacent(values, x, y)])
            if amount_occupied == 0 and values[y][x] == Seat.FREE:
                new_values[y][x] = Seat.OCCUPIED
            if amount_occupied >= max_allowed and values[y][x] == Seat.OCCUPIED:
                new_values[y][x] = Seat.FREE
    return new_values

def print_grid(values):
    for y in values:
        row = ""
        for seat in y:
            row += str(seat.value)
        print(row)

def part1(values):
    while True:
        new_values = iterate(values, get_adjacent_1, 4)
        print_grid(new_values)
        print()
        if values == new_values:
            return sum([seat == Seat.OCCUPIED for y in values for seat in y])
        values = new_values


def part2(values):
    while True:
        new_values = iterate(values, get_adjacent_2, 5)
        print_grid(new_values)
        print()
        if values == new_values:
            return sum([seat == Seat.OCCUPIED for y in values for seat in y])
        values = new_values

if __name__ == "__main__":
    with open("input.txt") as f:
        string = parse(f.readlines())
        #print(part1(string))
        print(part2(string))
