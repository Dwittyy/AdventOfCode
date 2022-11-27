from math import perm
import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run
from itertools import product

def instruction(memory,address):
    opcode = memory[address]
    if opcode == 99:
        return True
    first, second, result = memory[address + 1], memory[address + 2], memory[address + 3]
    if opcode == 1:
        memory[result] = memory[first] + memory[second]
    if opcode == 2:
        memory[result] = memory[first] * memory[second]

def run_program(memory,address=0):
    while address < len(memory):
        if instruction(memory,address):
            break
        address += 4
    return memory

@run
def solve():
    initial_memory = [int(x) for x in read_lines()[0].split(',')]
    for noun, verb in product(range(100),repeat=2):
        memory = list(initial_memory)
        memory[1] = noun
        memory[2] = verb
        run_program(memory)
        if memory[0] == 19690720:
            return (noun,verb,(100*noun)+verb)
    return

solve()