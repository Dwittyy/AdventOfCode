import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run
import re

def move_crates(stacks,amount,target,destination):
    for _ in range(amount):
        stacks[destination].append(stacks[target].pop())

@run
def solve():
    puzzle_input = read_lines()
    splitter = puzzle_input.index('')

    stacks = dict()
    for idx, num in enumerate(puzzle_input[:splitter][-1]):
        if num.isdigit():
            stacks[int(num)] = [x[idx] for x in puzzle_input[:splitter-1] if x[idx].isalpha()][::-1]
    
    moves = [[int(x) for x in re.findall("[0-9]+",move)] for move in puzzle_input[splitter+1:]]

    for move in moves:
        move_crates(stacks,*move)

    return "".join([x[-1] for x in stacks.values()])

solve()