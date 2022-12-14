import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

def sand_rest(coordinates,blocks,max_row):
    x, y = coordinates

    if y == max_row:
        return None

    for i in (0,-1,1):
        if (x + i,y + 1) not in blocks:
            return sand_rest((x + i,y + 1),blocks,max_row)

    return (x,y)

@run
def solve():
    blocks = set()
    for line in read_lines():
        line_points = line.split(" -> ")
        for i in range(1,len(line_points)):
            p1 = tuple(map(int,line_points[i - 1].split(",")))
            p2 = tuple(map(int,line_points[i].split(",")))
            dx = {p1[0], p2[0]}
            dy = {p1[1], p2[1]}
            for x in range(min(dx),max(dx)+1):
                for y in range(min(dy),max(dy)+1):
                    blocks.add((x,y))

    source = (500,0)
    sand = 0
    max_row = max(block[1] for block in blocks)
    while True:
        rest = sand_rest(source,blocks,max_row)
        if rest:
            blocks.add(rest)
            sand += 1
        else:
            break
        
    return sand

solve()