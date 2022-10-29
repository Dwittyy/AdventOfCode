import sys, os
sys.path.append(os.getcwd())
from util.read import read, read_nums
from util.time import timer
import math

def find_fuel(m):
    fuel = math.floor(m/3) - 2
    if fuel <= 0:
        return 0
    return fuel + find_fuel(fuel)

@timer
def solve():
    masses = read_nums(2019, 1)
    print(sum(find_fuel(m) for m in masses))
    return 

solve()