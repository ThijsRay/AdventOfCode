def part1(string: str):
    string = string.split()
    return max([string_to_seat_id(entry) for entry in string])

def string_to_seat_id(string):
    lower_row = 0
    upper_row = 127
    lower_column = 0
    upper_column = 7
    for character in string:
        if character == "F" or character == "B":
            lower_row, upper_row = partition(lower_row, upper_row, character=="F")
        if character == "L" or character == "R":
            lower_column, upper_column = partition(lower_column, upper_column, character=="L")
    return seat_id(lower_row, lower_column)

def partition(lower_bound, upper_bound, first_half: bool): 
    if abs(lower_bound - upper_bound) == 1:
        midpoint = upper_bound
    else:
        midpoint = round((lower_bound + upper_bound) / 2)
    if first_half:
        return lower_bound, midpoint
    else:
        return midpoint, upper_bound

def seat_id(row, column):
    return row*8 + column

def part2(string: str):
    string = string.split()
    taken_seats = sorted([string_to_seat_id(entry) for entry in string])
    for i in range(1, len(taken_seats)-1):
        if taken_seats[i-1] != taken_seats[i]-1:
            return(taken_seats[i] - 1)
        if taken_seats[i+1] != taken_seats[i]+1:
            return(taken_seats[i] + 1)
    return []

if __name__ == "__main__":
    with open("input.txt") as f:
        print(part1(f.read()))
        print(part2(f.read()))
