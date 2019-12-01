import re
import sys
import time
    
sys.setrecursionlimit(3000)
    
def makeGrid(filename):
    with open(filename) as f:
        lines = [line.rstrip() for line in f.readlines()]
            
    data = []
    for line in lines:
        a, b, c = map(int, re.findall('\d+', line))
        data += [(a, a, b, c)] if line[0] == 'x' else [(b, c, a, a)]

    Z = zip(*data)
    minX = min(Z[0])
    maxX = max(Z[1])
    minY = min(Z[2])
    maxY = max(Z[3])
        
    grid = [['.']*(maxX - minX + 2) for _ in xrange(maxY + 1)]
    for x1, x2, y1, y2 in data:
        for x in xrange(x1, x2 + 1):
            for y in xrange(y1, y2 + 1):
                grid[y][x - minX + 1] = '#'
                    
    return grid, minX, maxX, minY, maxY
    
def flow(grid, x, y, d):
    if grid[y][x] == '.':
        grid[y][x] = '|'
    if y == len(grid) - 1:
        return
    if grid[y][x] == '#':
        return x
    if grid[y+1][x] == '.':
        flow(grid, x, y+1, 0)
            
    if grid[y+1][x] in '~#':
        if d:
            return flow(grid, x+d, y, d)
        else:
            leftX = flow(grid, x-1, y, -1)
            rightX = flow(grid, x+1, y, 1)
            if grid[y][leftX] == '#' and grid[y][rightX] == '#':
                for fillX in xrange(leftX + 1, rightX):
                    grid[y][fillX] = '~'
    else:
         return x
    
def solve(filename):
    grid, minX, maxX, minY, maxY = makeGrid(filename)
    springX, springY = 500 - minX + 1, 0
    grid[springY][springX] = '+'
    
    flow(grid, springX, springY, 0)
    
    still = flowing = 0
    for y in xrange(minY, maxY + 1):
        for x in xrange(len(grid[0])):
            if grid[y][x] == '|':
                flowing += 1
            elif grid[y][x] == '~':
                still += 1
               
    return still + flowing, still
    
startTime = time.time()
ans1, ans2 = solve('input')
endTime = time.time()
print '\nfinished in %.6f sec' % (endTime - startTime)
print 'ans (part 1): ' + str(ans1)
print 'ans (part 2): ' + str(ans2)
