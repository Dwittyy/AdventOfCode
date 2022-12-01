import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

@run
def solve():
    elf_calories = []
    elf_calorie = []
    for calorie in read_lines():
        if calorie != "":
            elf_calorie.append(int(calorie))
        else:
            elf_calories.append(elf_calorie)
            elf_calorie = []
    elf_calories.append(elf_calorie)

    totals = [sum(holding) for holding in elf_calories]

    return sum(sorted(totals,reverse=True)[:3])

solve()