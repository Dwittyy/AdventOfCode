import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

def run_program(opcodes,pos=0):
    code = opcodes[pos]
    if code == 99:
        return opcodes
    first, second, result = opcodes[pos + 1], opcodes[pos + 2], opcodes[pos + 3]
    if code == 1:
        opcodes[result] = opcodes[first] + opcodes[second]
    if code == 2:
        opcodes[result] = opcodes[first] * opcodes[second]
    pos += 4
    run_program(opcodes, pos)        

@run
def solve():
    opcodes = [int(x) for x in read_lines()[0].split(',')]
    opcodes[1] = 12
    opcodes[2] = 2
    run_program(opcodes)
    return opcodes

solve()