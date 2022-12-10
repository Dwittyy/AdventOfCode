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
    rows = ["" for _ in range(6)]
    
    while line < len(program):
        cycle += 1

        row, pos = divmod(cycle - 1, 40)
        if pos in range(X-1,X+2):
            rows[row] += "#"
        else:
            rows[row] += "."

        if not command:
            command = program[line].split()
            duration = 2 if command[0] == "addx" else 1
        duration -= 1
        if duration == 0:
            if command[0] == "addx":
                X += int(command[1])
            line += 1
            command = []

    return rows

for row in solve():
    print(row.replace(".", " "))