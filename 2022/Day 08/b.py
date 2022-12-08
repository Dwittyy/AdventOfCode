import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run
from math import prod

def visible_in_line(value, trees):
    visible = 0
    for tree in trees:
        visible += 1
        if tree >= value:
            break
    return visible

@run
def solve():
    forest = read_lines()
    height = len(forest)
    width = len(forest[0])
    max_scenic = 0
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            value = int(forest[y][x])

            left = visible_in_line(value, [int(forest[y][i]) for i in range(0,x)][::-1])
            right = visible_in_line(value, [int(forest[y][i]) for i in range(x+1,width)])
            top = visible_in_line(value, [int(forest[i][x]) for i in range(0,y)][::-1])
            bottom = visible_in_line(value, [int(forest[i][x]) for i in range(y+1,height)])
            
            scenic = prod([left,right,top,bottom])
            if scenic > max_scenic:
                max_scenic = scenic
    return max_scenic

solve()