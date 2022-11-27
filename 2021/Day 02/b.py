import sys, os

sys.path.append(os.getcwd())
from util.read import *

instructions = read_lines()


def parse_instruction(instruction):
    command, value = tuple(instruction.split(" "))
    value = int(value)
    return command, value


def move_sub(instructions):
    aim_adjustments = {"forward": 0, "up": -1, "down": 1}
    directions = {"forward": 0, "depth": 0, "aim": 0}
    for instruction in instructions:
        d, v = parse_instruction(instruction)
        if d == "forward":
            directions["forward"] += v
            directions["depth"] += directions["aim"] * v
        else:
            directions["aim"] += aim_adjustments[d] * v
    return directions


movement = move_sub(instructions)
total_movement = movement["forward"] * movement["depth"]

print(total_movement)
