import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

@run
def solve():
    program = read_lines()
    line = 0
    cycle = 0
    X = 1
    command = []
    duration = 0
    strengths = []
    strength_cycles = [(20 + 40 * i) for i in range(6)]
    
    while cycle <= max(strength_cycles):
        cycle += 1

        if cycle in strength_cycles:
            strengths.append(X * cycle)
        
        if not command:
            command = program[line].split()
            duration = 2 if command[0] == "addx" else 1
        duration -= 1
        if duration == 0:
            if command[0] == "addx":
                X += int(command[1])
            line += 1
            command = []

    return sum(strengths)

solve()