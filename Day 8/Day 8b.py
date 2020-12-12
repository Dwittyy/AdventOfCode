puzzle_input = open("Day 8/puzzleinput.txt").read().splitlines()

import re

pattern = re.compile("([a-z]+) ([+-][0-9]+)")

def run_program(instructions):
    accumulator = 0
    index = 0
    executed = []

    while index not in executed:
        executed.append(index)
        line = instructions[index]
        action, num = re.match(pattern,line).groups()
        num = int(num)
        if action == "nop":
            index += 1
        if action == "acc":
            accumulator += num
            index += 1
        if action == "jmp":
            index += num
        if index == len(instructions) - 1:
            return ("Success", accumulator)
    
    return ("Fail", accumulator, executed)

def alter(instructions,index):
    altered_instructions = instructions.copy()
    altered_instructions[index] = altered_instructions[index].replace("jmp","x").replace("nop","jmp").replace("x","nop")
    return altered_instructions

pool = [x for x in run_program(puzzle_input)[2] if "acc" not in puzzle_input[x]]

results = [run_program(alter(puzzle_input,y))[0:2] for y in pool]

print(results)