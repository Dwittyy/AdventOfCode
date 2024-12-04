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
            if wordsearch[y][x] != "X":
                continue
            for direction in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                word = "X" + get_char(x + direction[0], y + direction[1], wordsearch) + get_char(x + 2 * direction[0], y + 2 * direction[1], wordsearch) + get_char(x + 3 * direction[0], y + 3 * direction[1], wordsearch)
                if word == "XMAS":
                    appearances += 1
    return appearances

solve()