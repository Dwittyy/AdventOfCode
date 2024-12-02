import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

@run
def solve():
    left = [int(line.split()[0]) for line in read_lines(test=False)]
    right = [int(line.split()[1]) for line in read_lines(test=False)]

    distances = [abs(x-y) for (x,y) in zip(sorted(left),sorted(right))]
    return sum(distances)

solve()