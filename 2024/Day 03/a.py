import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run
import re
from math import prod

@run
def solve():
    memory = read_file(test=False)
    instructions = re.findall(r"mul\(\d+,\d+\)",memory)
    result = 0
    for instruction in instructions:
        product = prod([int(x) for x in re.findall(r"\d+",instruction)])
        result += product
    return result

solve()