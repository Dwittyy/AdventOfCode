import sys, os

sys.path.append(os.getcwd())
from util.read import *

from statistics import median

positions = [int(x) for x in read_lines()[0].split(",")]

def fuel_usage(x,m):
    s = abs(x-m)
    return int(((s*(s+1))/2))

def total_fuel_usage(values,m):
    return sum([fuel_usage(p,m) for p in values])

def find_best(values):
    usages = []
    for i in range(min(values),max(values)):
        usages.append(total_fuel_usage(values,i))
    return min(usages)


print(positions)
print(find_best(positions))