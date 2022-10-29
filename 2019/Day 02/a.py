import sys, os
sys.path.append(os.getcwd())
from util.read import read, read_nums
from util.time import timer

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

@timer
def solve():
    opcodes = [int(x) for x in read(2019, 2)[0].split(',')]
    opcodes[1] = 12
    opcodes[2] = 2
    run_program(opcodes)
    print(opcodes)
    return

solve()