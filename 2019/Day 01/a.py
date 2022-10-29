import sys, os
sys.path.append(os.getcwd())
from util.read import read, read_nums
from util.time import timer
import math

def find_fuel(m):
    return math.floor(m/3) - 2

@timer
def solve():
    masses = read_nums(2019, 1)
    print(sum(find_fuel(m) for m in masses))
    return

solve()