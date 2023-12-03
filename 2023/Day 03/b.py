import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run
from collections import defaultdict
from math import prod

def adjacent_gears(x, y, grid):
    gears = []
    for i in (y-1, y, y+1):
        if i < 0 or i >= len(grid):
            continue
        for j in (x-1, x, x+1):
            if j < 0 or j >= len(grid[0]):
                continue
            if grid[i][j] == "*":
                gears.append((j,i))
    return gears

@run
def solve():
    schematic = read_lines()
    gears = defaultdict(list)
    for y, line in enumerate(schematic):
        current_number = ""
        current_adjacent_gears = set()
        for x, char in enumerate(line):
            if char.isdigit():
                current_number += char
                current_adjacent_gears.update(adjacent_gears(x, y, schematic))
            else:
                for gear in current_adjacent_gears:
                    gears[gear].append(int(current_number))
                current_number = ""
                current_adjacent_gears = set()
        for gear in current_adjacent_gears:
            gears[gear].append(int(current_number))
    
    return sum([prod(gears[gear]) for gear in gears if len(gears[gear]) == 2])
solve()