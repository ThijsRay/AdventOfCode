from copy import deepcopy

sample_input = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''

class Board:
    def __init__(self, board: str): 
        assert len(board) == 5
        self.board = [[int(i) for i in row.split()] for row in board]
        self.marked = [[False]*5 for _ in range(5)]

    def has_bingo(self) -> bool:
        rotated_m = [list(i) for i in zip(*self.marked)]
        for direction in [self.marked, rotated_m]:
            for row in direction:
                temp = True
                for column in row:
                    temp &= column
                if temp:
                    return True
        return False

    def mark(self, number: int):
        for row_idx in range(len(self.board)):
            for col_idx in range(len(self.board[row_idx])):
                if self.board[row_idx][col_idx] == number:
                    self.marked[row_idx][col_idx] = True
                    break

    def sum_unmarked_numbers(self) -> int:
        sum = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if not self.marked[i][j]:
                    sum += self.board[i][j]
        return sum


    def __repr__(self):
        s = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                element = self.board[i][j]
                if self.marked[i][j]:
                    s += "*"
                    s += str(element)
                    s += "*"
                else:
                    s += str(element)
                s += "\t"
            s += "\n"
        return s

def parse(input: str) -> tuple[list[int], list[Board]]:
    lines = [x for x in input.splitlines()]
    draws = [int(x) for x in lines[0].split(",")]

    cards = [lines[i+1:i+6] for i in range(1, len(lines), 6)]
    boards = [Board(card) for card in cards]
    return (draws, boards)

def star1(input: str) -> int:
    draws, boards = parse(input)
    for draw in draws:
        print("DRAWING", draw)
        for board in boards:
            board.mark(draw)
            print(board)
            if board.has_bingo():
                return board.sum_unmarked_numbers() * draw

def star2(input: str) -> int:
    draws, boards = parse(input)
    has_bingo = set()
    for draw in draws:
        for board in boards:
            board.mark(draw)
            if board.has_bingo():
                has_bingo.add(board)
            if len(boards) - len(has_bingo) == 0:
                return board.sum_unmarked_numbers() * draw
    

def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return "".join(f.readlines())

assert star1(sample_input) == 4512
assert star2(sample_input) == 1924
print("Day 4 - Star 1:", star1(read_file("input.txt")))
print("Day 4 - Star 2:", star2(read_file("input.txt")))
