from copy import deepcopy
from collections import defaultdict

small = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''

medium = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
'''

large = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
'''

class Node():
    def __init__(self, name: str):
        self.name = name
        self.neighbours: list[Node] = []
    
    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def is_big(self):
        return self.name.isupper()
    
    def __repr__(self):
        s = self.name
        for neighbour in self.neighbours:
            s += "\n"
            s += "\t"
            s += neighbour.name
        return s


class CaveSystem():
    def __init__(self):
        self.nodes: dict[str, Node] = dict()
        self.visited = defaultdict(lambda: False)
   
    def add_edge(self, a: str, b: str):
       if a not in self.nodes:
           self.nodes[a] = Node(a)
       if b not in self.nodes:
           self.nodes[b] = Node(b)
       self.nodes[a].add_neighbour(self.nodes[b])
       self.nodes[b].add_neighbour(self.nodes[a])

    def __repr__(self):
        s = ""
        for node in self.nodes.values():
            s += repr(node)
            s += "\n"
        return s



def parse(input: str) -> CaveSystem:
    edges = [x.split('-') for x in input.splitlines()]
    caves = CaveSystem()
    for edge in edges:
        caves.add_edge(edge[0], edge[1])
    return caves

def star1(input: str) -> int:
    caves = parse(input)
    start = caves.nodes["start"]
    return visit_neighbours(caves, start)

def visit_neighbours(caves: CaveSystem, node: Node):
    #print("Visiting the node ", node)
    caves.visited[node] = True 
    if node.name == "end":
        print("reach end")
        return 1
    endings = 0
    for neighbour in node.neighbours:
        if (not caves.visited[neighbour]) or neighbour.is_big():
            #caves = deepcopy(caves)
            endings += visit_neighbours(caves, neighbour)
    return endings

def star2(input: str) -> int:
    return 0

def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return "".join(f.readlines())

print( star1(small) )
assert star1(small) == 10
assert star1(medium) == 19
assert star1(large) == 226
print("Day 12 - Star 1:", star1(read_file("input.txt")))
print("Day 12 - Star 2:", star2(read_file("input.txt")))
