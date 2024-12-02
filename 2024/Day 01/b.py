import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

@run
def solve():
    left = [int(line.split()[0]) for line in read_lines(test=False)]
    right = [int(line.split()[1]) for line in read_lines(test=False)]

    scores = [num * right.count(num) for num in left]
    return sum(scores)

solve()