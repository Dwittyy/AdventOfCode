puzzle_input = open("Day 6/puzzleinput.txt").read().splitlines()

groups = []
temp_group = []

for response in puzzle_input:
    if response != '':
        temp_group.append(response)
    else: 
        groups.append(temp_group)
        temp_group = []

print(groups[0])

count = 0

for group in groups:
    group_yes = []
    for line in group:
        person_yes = [char for char in "abcdefghijklmnopqrstuvwxyz" if char in line]
        group_yes += [char for char in person_yes if char not in group_yes]
    count += len(group_yes)

print(group)
print(person_yes)
print(group_yes)
print(count)
