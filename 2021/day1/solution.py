sample_input = '''199
200
208
210
200
207
240
269
260
263'''

def get_depths(input: str) -> list[int]:
    return [int(depth) for depth in input.splitlines()]

def star1(input: str) -> int:
    depths = get_depths(input)
    measurement = depths[0]
    increased = 0
    for depth in depths[1:]:
        increased += 1 if depth-measurement>0 else 0
        measurement = depth
    return increased

def star2(input: str) -> int:
    depths = get_depths(input)
    previous = 0
    increased = -1
    for i in range(len(depths)-2):
        measurement = sum(depths[i:i+3])
        increased += 1 if measurement-previous>0 else 0
        previous = measurement
    print(increased)
    return increased

def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return "".join(f.readlines())

print("Day 1 - Star 1:", star1(read_file("input.txt")))
print("Day 1 - Star 2:", star2(read_file("input.txt")))
assert star1(sample_input) == 7
assert star2(sample_input) == 5
