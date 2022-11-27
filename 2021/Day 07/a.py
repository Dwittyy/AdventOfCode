import sys, os

sys.path.append(os.getcwd())
from util.read import *

from statistics import median

positions = [int(x) for x in read_lines()[0].split(",")]

def find_median(values):
    m = int(median(values))
    return m

def sum_distances(values,x):
    return sum([abs(x-v) for v in values])

print(sum_distances(positions,find_median(positions)))