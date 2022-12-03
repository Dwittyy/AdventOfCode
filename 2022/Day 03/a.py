import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

def get_priority(letter):
    return ord(letter.lower()) - 96 + (letter.isupper() * 26)

@run
def solve():
    rucksacks = read_lines()
    total_priorities = 0
    for rucksack in rucksacks:
        half = int(len(rucksack) / 2)
        shared = set(rucksack[:half]).intersection(set(rucksack[half:]))
        total_priorities += get_priority(list(shared)[0])
    return total_priorities

solve()