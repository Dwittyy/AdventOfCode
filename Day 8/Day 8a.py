puzzle_input = open("Day 8/puzzleinput.txt").read().splitlines()

import re

pattern = re.compile("([a-z]+) ([+-][0-9]+)")
accumulator = 0
index = 0
executed = []

while index not in executed:
    executed.append(index)
    line = puzzle_input[index]
    action, num = re.match(pattern,line).groups()
    num = int(num)
    if action == "nop":
        index += 1
    if action == "acc":
        accumulator += num
        index += 1
    if action == "jmp":
        index += num

print(accumulator)