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
        levels = [int(x) for x in report.split()]
        if is_safe(levels):
            safe += 1
        else:
            for i in range(len(levels)):
                dampened = levels[:i] + levels[i+1:]
                if is_safe(dampened):
                    safe += 1
                    break
    return safe

solve()