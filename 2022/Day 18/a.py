import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

def count_neighbours(cube,cubes):
    neighbours = 0
    x, y, z = cube
    for dx,dy,dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        if (x + dx,y + dy,z + dz) in cubes:
            neighbours += 1
    return neighbours

@run
def solve():
    cubes = [tuple(map(int,x.split(","))) for x in read_lines()]
    counted_cubes = set()
    total_surface_area = 0
    for cube in cubes:
        total_surface_area += 6 - (2 * count_neighbours(cube,counted_cubes))
        counted_cubes.add(cube)
    return total_surface_area

solve()