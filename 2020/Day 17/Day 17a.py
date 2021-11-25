puzzle_input = open("AdventOfCode2020/Day 17/puzzleinput.txt").read().splitlines()
test_input = open("AdventOfCode2020/Day 17/testinput.txt").read().splitlines()

from itertools import product

def FindAdjacent(coordinate,cubes):
    x,y,z = coordinate
    return [(x + dx,y + dy,z + dz) for dx,dy,dz in list(product([-1,0,1],repeat=3)) if (x + dx, y + dy, z + dz) in cubes and not (dx == dy == dz == 0)]

def CountAdjacent(coordinate,cubes,char):
    count = 0
    for c in FindAdjacent(coordinate,cubes):
        count += (cubes[c] == char)
    return count

def Step(cubes, coordinates, xspan):
    newcubes = cubes.copy()

    biggerbox = set(product([x for x in range(xspan[0],xspan[1] + 1)],repeat=3))
    newcoordinates = biggerbox.difference(coordinates)
    for cd in newcoordinates:
        newcubes[cd] = "."
    coordinates = biggerbox.copy()

    if (3,3,-1) in newcoordinates:
        print("I'm new!")
        print(sorted(newcoordinates))

    for coordinate in coordinates:
        if coordinate in newcoordinates:
            if CountAdjacent(coordinate,cubes,"#") == 3:
                newcubes[coordinate] = "#"
        elif cubes[coordinate] == "#":
            if CountAdjacent(coordinate,cubes,"#") in [2,3]:
                newcubes[coordinate] = "#"
            else:
                newcubes[coordinate] = "."
        else:
            if CountAdjacent(coordinate,cubes,"#") == 3:
                newcubes[coordinate] = "#"
            else:
                newcubes[coordinate] = "."
    return newcubes, coordinates

def Display(cubes):
    for z in range(z_span[0],z_span[1]+1):
        for y in range(y_span[0],y_span[1]+1):
            for x in range(x_span[0],x_span[1]+1):
                print(cubes[(x,y,z)],end='')
            print()
        print()

states = dict()

x_span = (0,7)
y_span = (0,7)
z_span = (0,0)

coordinates = set(product([x for x in range(x_span[0],x_span[1] + 1)],repeat=3))

for coordinate in coordinates:
    states[coordinate] = '.'

for i,row in enumerate(puzzle_input):
    for j,state in enumerate(row):
        states[(j,i,0)] = state

Display(states)

for i in range(6):
    x_span = (x_span[0] - 1, x_span[1] + 1)
    y_span = (y_span[0] - 1, y_span[1] + 1)
    z_span = (z_span[0] - 1, z_span[1] + 1)

    states, coordinates = Step(states, coordinates, x_span)
    print("Step:",i)
    #Display(states)
    print(i, list(states.values()).count("#"))

