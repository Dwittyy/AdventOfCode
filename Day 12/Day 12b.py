puzzle_input = open("Day 12/puzzleinput.txt").read().splitlines()

newdict = {"N": (1,0,0), "E": (0,1,0), "S": (-1,0,0), "W": (0,-1,0), "R": (0,0,1), "L": (0,0,-1),}
newdict2 = {0: (1,0), 90: (0,1), 180: (-1,0), 270: (0,-1)}

up, right, rotate = newdict["E"]
print(right)


# (-1,10) -> (10,1) -> (1,-10) -> (-10,-1)

def Pivot(x,y,r):
    r %= 360
    if r == 0: return x,y
    if r == 90: return y,-x
    if r == 180: return -x,-y
    if r == 270: return -y,x

x = 0
y = 0

wx = 10
wy = 1

for line in puzzle_input:
    action = line[0]
    value = int(line[1:])
    if action != "F":
        dy, dx, dr = newdict[action]
        wy += dy * value
        wx += dx * value
        dr *= value
        wx, wy = Pivot(wx,wy,dr) 
    if action == "F":
        x += wx * value
        y += wy * value

print(abs(x) + abs(y))