import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

def has_adjacent_symbol(x, y, grid):
    for i in (y-1, y, y+1):
        if i < 0 or i >= len(grid):
            continue
        for j in (x-1, x, x+1):
            if j < 0 or j >= len(grid[0]):
                continue
            char = grid[i][j]
            if char not in "0123456789.":
                return True
    return False

@run
def solve():
    schematic = read_lines()
    part_numbers = []
    for y, line in enumerate(schematic):
        current_number = ""
        is_part = False
        for x, char in enumerate(line):
            if char.isdigit():
                current_number += char
                if has_adjacent_symbol(x, y, schematic):
                    is_part = True
            else:
                if is_part:
                    part_numbers.append(int(current_number))
                current_number = ""
                is_part = False
        if is_part:
            part_numbers.append(int(current_number))
    return sum(part_numbers)

solve()