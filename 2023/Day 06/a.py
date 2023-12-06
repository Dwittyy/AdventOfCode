import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run
from math import prod

@run
def solve():
    document = read_lines()
    times = [int(x) for x in document[0].split(' ')[1:] if x]
    records = [int(x) for x in document[1].split(' ')[1:] if x]
    all_ways = []
    for j in range(len(times)):
        ways = 0
        for i in range(1, times[j]):
            if (times[j] - i) * i > records[j]:
                ways += 1
        all_ways.append(ways)
    return prod(all_ways)

solve()