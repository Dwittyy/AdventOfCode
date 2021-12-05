import sys, os

sys.path.append(os.getcwd())
from util.read import read, read_nums

puzzle_input = read(2021, 5)

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
    if p1[0] == p2[0]:
        start = min(p1[1],p2[1])
        end = max(p1[1],p2[1])
        for y in range(start,end+1):
            grid[(p1[0],y)] = grid.get((p1[0],y),0) + 1
    if p1[1] == p2[1]:
        start = min(p1[0],p2[0])
        end = max(p1[0],p2[0])
        for x in range(start,end+1):
            grid[(x,p1[1])] = grid.get((x,p1[1]),0) + 1

# Count Dangers
def count_dangers(grid):
    return len([val for val in grid.values() if val >= 2])


print(count_dangers(grid))