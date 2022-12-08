import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

@run
def solve():
    forest = read_lines()
    visible = 0
    height = len(forest)
    width = len(forest[0])
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            value = int(forest[y][x])
            if value > max(int(forest[y][i]) for i in range(0,x)):
                visible +=1
            elif value > max(int(forest[y][i]) for i in range(x+1,width)):
                visible +=1
            elif value > max(int(forest[i][x]) for i in range(0,y)):
                visible +=1
            elif value > max(int(forest[i][x]) for i in range(y+1,height)):
                visible +=1
    visible += (2 * height) + (2 * width) - 4
    return visible

solve()
