from itertools import chain

sample_input = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''

def parse(input: str) -> list[list[int]]:
    x = [x for x in input.splitlines()]
    return x

def is_opening_bracket(c: chr) -> bool:
    return c == '(' or c == '[' or c == '{' or c == '<'

def is_closing_bracket(c: chr) -> bool:
    return c == ')' or c == ']' or c == '}' or c == '>'

def inverse(c: chr) -> chr:
    if c == ')': return '('
    if c == ']': return '['
    if c == '}': return '{'
    if c == '>': return '<'
    if c == '(': return ')'
    if c == '[': return ']'
    if c == '{': return '}'
    if c == '<': return '>'

def score_1(c: chr) -> int:
    if c == ')': return 3
    if c == ']': return 57
    if c == '}': return 1197
    if c == '>': return 25137

def score_2(c: chr) -> int:
    if c == '(': return 1
    if c == '[': return 2
    if c == '{': return 3
    if c == '<': return 4

def is_corrupt(line: chr) -> tuple[list[chr], int, bool]:
    stack = []
    for i in range(len(line)):
        c = line[i]
        if is_opening_bracket(c):
            stack.append(c) 
        if is_closing_bracket(c):
            should_match = inverse(stack.pop())
            if c != should_match:
                return (stack, i, True)
    return (stack, None, False)


def star1(input: str) -> int:
    lines = parse(input)
    illegal_score = 0

    for line in lines:
        stack, idx, corrupt = is_corrupt(line)
        if corrupt:
            illegal_score += score_1(line[idx])

    return illegal_score 


def star2(input: str) -> int:
    lines = parse(input)
    scores = []
    for line in lines:
        stack, idx, corrupt = is_corrupt(line)
        score = 0
        if corrupt:
            continue
        while len(stack) > 0:
            score *= 5
            score += score_2(stack.pop()) 
        scores.append(score)
    scores = sorted(scores)
    return (scores[len(scores)//2])
    
def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return "".join(f.readlines())

assert star1(sample_input) == 26397
assert star2(sample_input) == 288957
print("Day 10 - Star 1:", star1(read_file("input.txt")))
print("Day 10 - Star 2:", star2(read_file("input.txt")))
