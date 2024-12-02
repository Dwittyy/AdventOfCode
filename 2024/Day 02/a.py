import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

def is_safe(report):
    differences = [y - x for (x,y) in zip(report,report[1:])]
    if any(abs(num) > 3 for num in differences):
        return False
    if all(num > 0 for num in differences) or all(num < 0 for num in differences):
        return True
    return False

@run
def solve():
    reports = read_lines(test=False)
    safe = 0
    for report in reports:
        if is_safe([int(x) for x in report.split()]):
            safe += 1
    return safe

solve()