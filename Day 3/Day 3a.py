base_field = open("Day 3/puzzleinput.txt").read().splitlines()

def extendfield(current_field):
    for row in range(len(current_field)):
        current_field[row] = current_field[row] + base_field[row]
    return current_field

current_field = base_field.copy()

trees = 0
r = 0
c = 0

while r < len(current_field):
    if c >= len(current_field[r]):
        current_field = extendfield(current_field)
    trees += (current_field[r][c] == "#")
    r += 1
    c += 3

print(trees)