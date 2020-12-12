puzzle_input = open("Day 12/puzzleinput.txt").read().splitlines()

directions = {"N": (0,1,0), "E": (1,0,0), "S": (0,-1,0), "W": (-1,0,0), "R": (0,0,1), "L": (0,0,-1)} # Dictionary reference

def Pivot(x,y,r): # (-1,10) -> (10,1) -> (1,-10) -> (-10,-1)
    r %= 360
    if r == 0: return x,y
    if r == 90: return y,-x
    if r == 180: return -x,-y
    if r == 270: return -y,x

def Solve(instructions,part):
    x,y = (0,0)
    if part == 1: wx,wy = (1,0) 
    if part == 2: wx,wy = (10,1)

    for line in instructions:
        action, value = (line[0], int(line[1:]))
        if action == "F":
            x,y = x + wx * value, y + wy * value
        else:
            dx, dy, dr = directions[action]
            wx, wy = Pivot(wx, wy, dr * value)
            if part == 1: # In Part 1, NESW moves the ship only.
                x,y = x + dx * value, y + dy * value
            if part == 2: # In Part 2, NESW moves the waypoint only.
                wx, wy = wx + dx * value, wy + dy * value

    return abs(x) + abs(y)

print(Solve(puzzle_input,1))
print(Solve(puzzle_input,2))