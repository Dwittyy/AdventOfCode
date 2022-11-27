import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run
import math

def find_fuel(m):
    return math.floor(m/3) - 2

@run
def solve():
    masses = read_nums()
    return sum(find_fuel(m) for m in masses)

solve()