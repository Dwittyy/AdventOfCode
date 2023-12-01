import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

@run
def solve():
    document = read_lines()
    calibration = 0
    for line in document:
        values = [int(x) for x in line if x.isdigit()]
        calibration += int(str(values[0]) + str(values[-1]))
    return calibration

solve()