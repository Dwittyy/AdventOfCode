import sys, os

sys.path.append(os.getcwd())
from util.read import read
from collections import Counter

# Parse
puzzle_input = read(2021, 14)
template = puzzle_input[0]
rules = {rule.split(" -> ")[0] : rule.split(" -> ")[1] for rule in puzzle_input[2:]}

def insertion_step(polymer,rules):
    new_polymer = polymer[0]
    for index in range(len(polymer)-1):
        new_polymer += rules[polymer[index:index+2]] + polymer[index+1]
    return new_polymer

def insertion_process(template,rules,steps):
    polymer = template
    for _ in range(steps):
        polymer = insertion_step(polymer,rules)
    counts = Counter(polymer).most_common()
    return counts[0][1] - counts[-1][1]

print(insertion_process(template,rules,10))
