sample_input = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''

class Octopi():
    def __init__(self, octopi):
        self.octopi = octopi
        self.dim_y = len(octopi)
        self.dim_x = len(octopi[0])
        self.reset_flash()

    def neighbours(self, x, y) -> list[tuple[int,int]]:
        neighbours = []
        if x > 0: 
            neighbours.append((x-1, y))
            if y > 0:
                neighbours.append((x-1, y-1))
        if y > 0: 
            neighbours.append((x, y-1))
            if x < self.dim_x-1:
                neighbours.append((x+1, y-1))
        if x < self.dim_x-1: 
            neighbours.append((x+1, y))
            if y < self.dim_y-1:
                neighbours.append((x+1, y+1))
        if y < self.dim_y-1: 
            neighbours.append((x, y+1))
            if x > 0:
                neighbours.append((x-1, y+1))
        return neighbours

    def phase1(self):
        for x in range(self.dim_x):
            for y in range(self.dim_y):
                self.octopi[x][y] += 1

    def phase2(self):
        for x in range(self.dim_x):
            for y in range(self.dim_y):
                self.flash(x, y)

    def flash(self, x, y):
        if self.octopi[x][y] > 9:
            if not self.flashed[x][y]:
                self.flashed[x][y] = True
                neighbours = self.neighbours(x,y)
                for nx,ny in neighbours:
                    self.octopi[nx][ny] += 1
                for nx,ny in neighbours:
                    self.flash(nx, ny)

    def reset_flash(self):
        self.flashed = [[False]*self.dim_x for _ in range(self.dim_y)]


    def phase3(self) -> int:
        amount_of_flashes = 0
        for x in range(self.dim_x):
            for y in range(self.dim_y):
                if self.flashed[x][y]:
                    amount_of_flashes += 1
                if self.octopi[x][y] > 9:
                    self.octopi[x][y] = 0
        if all([all(x) for x in self.flashed]):
            return -1
        self.reset_flash()
        return amount_of_flashes

    def step(self) -> int:
        self.phase1()
        self.phase2()
        flashes = self.phase3()
        return flashes

    def __repr__(self):
        s = ""
        for x in range(self.dim_x):
            for y in range(self.dim_y):
                if self.flashed[x][y]:
                    s += "*"
                s += str(self.octopi[x][y])
                if self.flashed[x][y]:
                    s += "*"
                s += "\t"
            s += "\n"
        return s

    
def parse(input: str) -> list[list[int]]:
    x = [[int(y) for y in x] for x in input.splitlines()]
    return x

def star1(input: str) -> int:
    octopi = Octopi(parse(input))
    return sum([octopi.step() for _ in range(100)])

def star2(input: str) -> int:
    octopi = Octopi(parse(input))
    for i in range(10000000):
        if octopi.step() == -1:
            return i+1

def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return "".join(f.readlines())

assert star1(sample_input) == 1656
assert star2(sample_input) == 195
print("Day 10 - Star 1:", star1(read_file("input.txt")))
print("Day 10 - Star 2:", star2(read_file("input.txt")))
