import sys, os

sys.path.append(os.getcwd())
from util.read import *

puzzle_input = read_lines()

def parse_line(line):
    return_line = []
    for coordinates in line.split(" -> "):
        return_line.append([int(x) for x in coordinates.split(",")])
    return return_line   

# Plot Lines
grid = {}
for line in puzzle_input:
    parsed_line = parse_line(line)
    p1, p2 = parsed_line[0], parsed_line[1]
    x0, y0 = p1
    x1, y1 = p2
    if p1 == p2:
        continue
    x_direction = 1 if x1 >= x0 else -1
    y_direction = 1 if y1 >= y0 else -1
    x, y = x0, y0
    while True:
        #print(f"from {x0},{y0} to {x1},{y1} at point {x},{y}")
        grid[(x,y)] = grid.get((x,y),0) + 1
        if x == x1 and y == y1:
            break
        x += (x0 != x1) * x_direction
        y += (y0 != y1) * y_direction

# Count Dangers
def count_dangers(grid):
    return len([val for val in grid.values() if val >= 2])

print(count_dangers(grid))
