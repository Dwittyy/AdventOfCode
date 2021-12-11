import sys, os

sys.path.append(os.getcwd())
from util.read import read, read_nums

def parse(levels):
    output = {}
    for r, row in enumerate(levels):
        for c in range(len(row)):
            output[(r,c)] = int(row[c])
    return output

energy_levels = parse(read(2021, 11))

def neighbours(levels,octopus):
    x,y = octopus
    return [test for test in [(x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y+1),(x-1,y),(x-1,y-1)] if test in levels.keys()]    

def simulate(levels,steps):
    flashes = 0
    for step in range(steps):
        for octopus in levels.keys():
            levels[octopus] += 1 * (levels[octopus] >= 0)
        while True:
            flashers = [octopus for octopus in levels.keys() if levels[octopus] > 9]
            if not flashers:
                for flashed in [octopus for octopus in levels.keys() if levels[octopus] == -1]:
                    levels[flashed] = 0
                break
            for octopus in flashers:
                flashes += 1
                levels[octopus] = -1
                for neighbour in neighbours(levels,octopus):
                    levels[neighbour] += 1 * (levels[neighbour] >= 0)
    return flashes

print(simulate(energy_levels,100))        