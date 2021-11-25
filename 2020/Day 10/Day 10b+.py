puzzle_input = [int(i) for i in open("Day 10/puzzleinput.txt").read().splitlines()]

from math import prod

puzzle_input.sort()
joltages = [0] + puzzle_input + [puzzle_input[-1] + 3]

def Part1(adapters):
    differences = [adapters[x+1] - adapters[x] for x in range(len(adapters)-1)]
    return differences.count(1) * differences.count(3)

#print(Part1(puzzle_input))

def Groups(adapters):
    groups = []
    sub = []
    for i in range(1,len(adapters)-1):
        if adapters[i] == adapters[i+1] - 3 or adapters[i] == adapters[i-1] + 3:
            if sub: 
                groups.append(sub)
                sub = []
        elif adapters[i] == adapters[i-1] + 1:
            sub.append(adapters[i])
        else:
            groups.append(sub)
            sub = [adapters[i]]
    return groups

def Combs(split):
    if len(split) == 1: return 2
    if len(split) == 2: return 4
    if len(split) == 3: return 7

print(Groups(joltages))
print(prod([Combs(x) for x in Groups(joltages)]))