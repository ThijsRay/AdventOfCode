from collections import defaultdict

sample_input = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''
class Line():
    def __init__(self, line: str):
        b = line[0].split(',')
        e = line[1].split(',')
        self.begin = (int(b[0]), int(b[1]))
        self.end = (int(e[0]), int(e[1]))
        self.by, self.bx = self.begin
        self.ey, self.ex = self.end
        self.dy = self.ey - self.by
        self.dx = self.ex - self.bx

    def is_straight(self):
        return self.dx == 0 or self.dy == 0

    def __repr__(self):
        return f"{self.begin} -> {self.end}" 

class Board():
    def __init__(self):
        self.map = defaultdict(lambda: 0)

    def add_line(self, line: Line):
        dx = line.dx
        dy = line.dy

        step_amount = 0
        step_y = 0
        step_x = 0
        
        if dy != 0:
            step_amount= dy
            step_y = int(dy/dy)
            step_x = int(dx/dy)
        elif dx != 0:
            step_amount = dx
            step_y = int(dy/dx)
            step_x = int(dx/dx)

        if step_amount < 0:
            step_amount *= -1
            step_y *= -1
            step_x *= -1

        for i in range(step_amount+1):
            y = line.by + (i*step_y)
            x = line.bx + (i*step_x)
            self.map[(x,y)] += 1

    def dimensions(self):
        max_x = 0
        max_y = 0
        for x,y in self.map:
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        return (max_x, max_y)

    def __repr__(self):
        x, y = self.dimensions()
        s = ""
        for x in range(x+1):
            for y in range(y+1):
                val = self.map[(x,y)]
                if val == 0:
                    s += "*"
                else:
                    s += str(val)
            s += "\n"
        return s
        

def parse(input: str) -> list[Line]:
    lines = [y.split(" -> ") for y in input.splitlines()]
    lines = [Line(y) for y in lines]
    return lines

def star1(input: str) -> int:
    lines = parse(input)
    board = Board()
    amount = 0
    for line in lines:
        if line.is_straight():
            board.add_line(line)
    for coord, value in board.map.items():
        if value >= 2:
            amount += 1
    print(board)
    print(amount)
    return amount

def star2(input: str) -> int:
    lines = parse(input)
    board = Board()
    amount = 0
    for line in lines:
        board.add_line(line)
    for coord, value in board.map.items():
        if value >= 2:
            amount += 1
    print(board)
    print(amount)
    return amount

def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return "".join(f.readlines())

assert star1(sample_input) == 5
assert star2(sample_input) == 12
print("Day 5 - Star 1:", star1(read_file("input.txt")))
print("Day 5 - Star 2:", star2(read_file("input.txt")))
