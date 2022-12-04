import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

def ranges(pair):
    ranges = []
    for p in pair.split(","):
        low,high = (int(x) for x in p.split("-"))
        ranges.append((low,high))
    return tuple(ranges)
    
@run
def solve():
    assignments = read_lines()
    overlaps = 0
    for pair in assignments:
        first, second = ranges(pair)
        first_set = set(range(first[0],first[1]+1))
        second_set = set(range(second[0],second[1]+1))
        if first_set & second_set:
            overlaps += 1
    return overlaps

solve()