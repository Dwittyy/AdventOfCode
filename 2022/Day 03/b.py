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
    for i in range(0,len(rucksacks),3):
        group = rucksacks[i:i+3]
        shared = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        total_priorities += get_priority(list(shared)[0])
    return total_priorities

solve()