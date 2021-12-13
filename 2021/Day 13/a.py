import sys, os

sys.path.append(os.getcwd())
from util.read import read

# Parse
puzzle_input = read(2021, 13)
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

first_fold = folds[0]
fold(dots,first_fold[0],first_fold[1])
print(len(dots))