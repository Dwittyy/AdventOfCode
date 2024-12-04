import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

def get_char(x,y,grid):
    if len(grid[0]) > x >= 0 and len(grid) > y >= 0:
        return grid[y][x]
    else:
        return ""

@run
def solve():
    wordsearch = read_lines(test=False)
    appearances = 0
    width, height = len(wordsearch[0]), len(wordsearch)
    for x in range(width):
        for y in range(height):
            if wordsearch[y][x] != "A":
                continue
            if get_char(x - 1, y - 1, wordsearch) + "A" + get_char(x + 1, y + 1, wordsearch) in ("MAS", "SAM"):
                if get_char(x - 1, y + 1, wordsearch) + "A" + get_char(x + 1, y - 1, wordsearch) in ("MAS", "SAM"):
                    appearances += 1
    return appearances

solve()