import sys, os

sys.path.append(os.getcwd())
from util.read import *

def parse_map(height_map):
    output = {}
    for r, row in enumerate(height_map):
        for c in range(len(row)):
            output[(r,c)] = int(row[c])
    return output

actual_height_map = parse_map(read_lines())

def find_neighbours(coordinates,height_map):
    x,y = coordinates
    return [test for test in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] if test in height_map.keys()]

def is_low_point(coordinates,height_map):
    for neighbour in find_neighbours(coordinates,height_map):
        if height_map[neighbour] <= height_map[coordinates]:
            return False
    return True

def find_low_points(height_map):
    return [point for point in height_map if is_low_point(point,height_map)]

def find_basin(coordinates,height_map):
    basin = {coordinates}
    path_basin(coordinates,height_map,basin)
    return basin

def path_basin(coordinates,height_map,basin):
    for neighbour in find_neighbours(coordinates,height_map):
        if 9 > height_map[neighbour] > height_map[coordinates]:
            basin.add(neighbour)
            path_basin(neighbour,height_map,basin)
    return

def find_basins(height_map):
    return [find_basin(low_point,height_map) for low_point in find_low_points(height_map)]

def find_largest(basins):
    sizes = sorted([len(basin) for basin in basins])
    return sizes[-1] * sizes[-2] * sizes[-3]

print(find_largest(find_basins(actual_height_map)))
