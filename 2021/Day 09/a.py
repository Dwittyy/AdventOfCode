import sys, os

sys.path.append(os.getcwd())
from util.read import *

height_map = read_lines()

def parse_map(height_map):
    output = {}
    for r, row in enumerate(height_map):
        for c in range(len(row)):
            output[(r,c)] = int(row[c])
    return output

def is_low_point(coordinates,height_map):
    x,y = coordinates
    base_value = height_map[(x,y)]
    for test in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if test in height_map.keys() and height_map[test] <= base_value:
            return False
    return True

def find_low_points(height_map):
    height_map = parse_map(height_map)
    low_points = [point for point in height_map if is_low_point(point,height_map)]
    risk_levels = [1 + height_map[point] for point in low_points]
    return sum(risk_levels)



print(find_low_points(height_map))
