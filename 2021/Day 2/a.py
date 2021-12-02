import sys, os

sys.path.append(os.getcwd())
from util.read import read, read_nums

instructions = read(2021, 2)


def parse_instruction(instruction):
    command, value = tuple(instruction.split(" "))
    value = int(value)
    return command, value


def move_sub(instructions):
    directions = {"forward": 0, "down": 0, "up": 0}
    for instruction in instructions:
        d, v = parse_instruction(instruction)
        directions[d] += v
    return directions


movement = move_sub(instructions)
total_movement = movement["forward"] * (movement["down"] - movement["up"])

print(total_movement)
