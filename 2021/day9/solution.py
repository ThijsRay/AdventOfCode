from itertools import chain

sample_input = '''2199943210
3987894921
9856789892
8767896789
9899965678
'''

from typing import TypeVar, Generic
T = TypeVar('T')

def parse(input: str) -> list[list[int]]:
    x = [[int(x) for x in y] for y in input.splitlines()]
    return x

def risk(height: int) -> int:
    return height + 1

def dimensions(map: list[list[T]]) -> tuple[int, int]:
    x = len(map)
    y = len(map[0])
    return (x,y)

def neighbours(map: list[list[T]], x: int, y: int) -> list[tuple[int, int, T]]:
    dim_x, dim_y = dimensions(map)
    neighbours = []
    if x > 0:
        neighbours.append((x-1, y, map[x-1][y]))
    if x < dim_x-1:
        neighbours.append((x+1, y, map[x+1][y]))
    if y > 0:
        neighbours.append((x, y-1, map[x][y-1]))
    if y < dim_y-1:
        neighbours.append((x, y+1, map[x][y+1]))
    return neighbours

def is_low_point(map: list[list[int]], x: int, y: int) -> bool:
    value = map[x][y]
    return all([value < neighbour for _, _, neighbour in neighbours(map, x, y)])

def star1(input: str) -> int:
    map = parse(input) 
    dim_x, dim_y = dimensions(map)
    
    low_points = []
    for x in range(dim_x):
        for y in range(dim_y):
            if is_low_point(map, x, y):
                low_points.append(map[x][y])
    print(low_points)

    return sum([risk(x) for x in low_points])

def star2(input: str) -> int:
    map = parse(input) 
    basin_map = [[(x, 0) for x in y] for y in map]
    dim_x, dim_y = dimensions(basin_map)

    color = 1
    for x in range(dim_x):
        for y in range(dim_y):
            flood_fill(basin_map, (x,y), color)
            color += 1
    lengths = sorted([len([(v,c) for x in basin_map for v,c in x if v != 9 and nc == c]) for nc in range(color)])
    return product(lengths[-3:])

def product(list) -> int:
    curr = 1
    out = [(curr:=curr*v) for v in list]
    return curr

def flood_fill(map: list[list[tuple[int, int]]], node: tuple[int,int], new_color: int):
    x, y = node
    dim_x, dim_y = dimensions(map)
    # outside of the map
    if x >= dim_x or y >= dim_y or x < 0 or y < 0:
        return
    value, color = map[x][y]
    # It is a border or already colored
    if value == 9 or color != 0:
        return
    map[x][y] = (value, new_color)
    for x,y,n in neighbours(map, x, y):
        flood_fill(map, (x,y), new_color)
    

def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return "".join(f.readlines())

assert star1(sample_input) == 15
assert star2(sample_input) == 1134
print("Day 9 - Star 1:", star1(read_file("input.txt")))
print("Day 9 - Star 2:", star2(read_file("input.txt")))
