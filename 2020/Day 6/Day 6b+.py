puzzle_input = open("Day 6/puzzleinput.txt").read().splitlines()

groups = []
temp_group = []

for response in puzzle_input:
    if response != '':
        temp_group.append(response)
    else: 
        groups.append(temp_group)
        temp_group = []

count = 0

for group in groups:
    group_yes = {c for c in group[0]}
    for line in group:
        group_yes = group_yes.intersection(line)
    count += len(group_yes)

print(count)

