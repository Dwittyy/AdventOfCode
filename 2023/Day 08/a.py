import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

@run
def solve():
    document = read_sections()
    turns = document[0][0]
    maps = dict()
    for line in document[1]:
        node, splits = line.split(' = ')
        splits = tuple(splits.replace('(','').replace(')','').split(', '))
        maps[node] = splits
    node = 'AAA'
    step = 0
    while node != 'ZZZ':
        turn = {"L": 0 , "R": 1}[turns[step % len(turns)]]
        node = maps[node][turn]
        step += 1
    return step

solve()