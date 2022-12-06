import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

@run
def solve():
    datastream = read_lines()[0]
    c = 14
    for i in range(c,len(datastream)):
        if len(set(datastream[i-c:i])) == c:
            return datastream[i-c:i], i

solve()