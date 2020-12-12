puzzle_input = open("Day 12/puzzleinput.txt").read().splitlines()

newdict = {"N": (1,0,0), "E": (0,1,0), "S": (-1,0,0), "W": (0,-1,0), "R": (0,0,1), "L": (0,0,-1),}
newdict2 = {0: (1,0), 90: (0,1), 180: (-1,0), 270: (0,-1)}

up, right, rotate = newdict["E"]
print(right)

x = 0
y = 0
r = 90

for line in puzzle_input:
    action = line[0]
    value = int(line[1:])
    if action != "F":
        dy, dx, dr = newdict[action]
        y += dy * value
        x += dx * value
        r = (r + dr * value) % 360
    if action == "F":
        dy, dx = newdict2[r]
        y += dy * value
        x += dx * value

print(x,y,r)
print(abs(x) + abs(y))
