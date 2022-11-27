import sys, os

sys.path.append(os.getcwd())
from util.read import *
from collections import Counter

# Parse
puzzle_input = read_lines()
template = puzzle_input[0]
rules = {rule.split(" -> ")[0] : rule.split(" -> ")[1] for rule in puzzle_input[2:]}

def insertion_step(pairs,rules):
    new_pairs = {}
    for pair in pairs.keys():
        for comb in (pair[0] + rules[pair],rules[pair] + pair[1]):
            new_pairs[comb] = new_pairs.get(comb,0) + pairs[pair]
    return new_pairs

def insertion_process(template,rules,steps):
    # Starting counts
    pairs = {}
    for pair in [template[i:i+2] for i in range(len(template)-1)]:
        pairs[pair] = pairs.get(pair,0) + 1

    # Step
    for _ in range(steps):
        pairs = insertion_step(pairs,rules)
    
    # Convert pair counts to letter counts
    letters = {template[-1]: 1}
    for pair in pairs:
        for letter in pair:
            letters[letter] = letters.get(letter,0) + pairs[pair]
    letters = {l : int(letters[l] / 2) for l in letters.keys()}

    return max(letters.values()) - min(letters.values())

print(insertion_process(template,rules,40))