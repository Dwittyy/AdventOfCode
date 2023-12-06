import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

@run
def solve():
    almanac = read_sections()
    seeds = [int(x) for x in almanac.pop(0)[0].split(': ')[1].split(' ')]

    destination_list = list(seeds)
    for section in almanac:
        source_cat, _, destination_cat = section[0].replace(' map:','').split('-')
        source_list = list(destination_list)
        destination_list = []
        for val in source_list:
            new_val = val
            for numbers in section[1:]:
                destination_start, source_start, rang = [int(x) for x in numbers.split(' ')]
                if val in range(source_start,source_start + rang):
                    new_val = val - source_start + destination_start
            destination_list.append(new_val)

    return min(destination_list)

solve()