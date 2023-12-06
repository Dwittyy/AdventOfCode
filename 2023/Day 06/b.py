import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run
from math import prod

@run
def solve():
    document = read_lines()
    time = int(document[0].replace('Time:','').replace(' ',''))
    record = int(document[1].replace('Distance:','').replace(' ',''))
    ends = []
    for i in range(1, time):
        if (time - i) * i > record:
            ends.append(i)
            break
    for i in reversed(range(1, time)):
        if (time - i) * i > record:
            ends.append(i)
            break
    return ends[1] - ends[0]

solve()