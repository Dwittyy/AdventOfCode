import sys, os

sys.path.append(os.getcwd())
from util.read import *

# Parse
puzzle_input = read_lines()
splitter = puzzle_input.index("")
dots = {(int(entry.split(",")[0]),int(entry.split(",")[1])) for entry in puzzle_input[:splitter]}
folds = []
for fold in puzzle_input[splitter + 1:]:
    split_fold = fold.replace("fold along ","").split("=")
    split_fold[1] = int(split_fold[1])
    folds.append(tuple(split_fold))

def fold(grid,axis,value):
    indexer = {"x": 0, "y": 1}[axis]
    for p in [p for p in grid if p[indexer] > value]:
        new = value - (p[indexer] - value)
        grid.add([(new,p[1]),(p[0],new)][indexer])
        grid.remove(p)    
    return grid

for f in folds:
    fold(dots,f[0],f[1])

for y in range(10):
    print_line = ""
    for x in range(50):
        print_line += "#" if (x,y) in dots else " "
    print(print_line)