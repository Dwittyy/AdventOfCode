import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

def neighbours(cube):
    x, y, z = cube
    return [(x + dx,y + dy,z + dz) for dx,dy,dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]

def outsiders(cubes,corners):
    to_check = [corners[0]]
    outsiders = set()
    while to_check:
        checkee = to_check.pop()
        outsiders.add(checkee)
        for neighbour in neighbours(checkee):
            if neighbour in cubes or neighbour in outsiders:
                continue
            if not all(corners[0][i] <= neighbour[i] <= corners[1][i] for i in range(3)):
                continue
            to_check.append(neighbour)
    return outsiders

@run
def solve():
    cubes = {tuple(map(int,x.split(","))) for x in read_lines()}

    min_x = min(cube[0] for cube in cubes) - 1
    min_y = min(cube[1] for cube in cubes) - 1
    min_z = min(cube[2] for cube in cubes) - 1
    max_x = max(cube[0] for cube in cubes) + 1
    max_y = max(cube[1] for cube in cubes) + 1
    max_z = max(cube[2] for cube in cubes) + 1
    corners = [(min_x,min_y,min_z),(max_x,max_y,max_z)]

    outside_faces = 0
    for outsider in outsiders(cubes,corners):
        outside_faces += len([neighbour for neighbour in neighbours(outsider) if neighbour in cubes])

    return outside_faces

solve()