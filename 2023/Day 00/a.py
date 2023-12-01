import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

@run
def solve():
    puzzle_input = read_lines()
    ###
    return puzzle_input

solve()