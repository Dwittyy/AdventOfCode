import sys, os

sys.path.append(os.getcwd())
from util.read import read, read_nums

initial_fish = [int(x) for x in read(2021, 6)[0].split(",")]

counts = [initial_fish.count(x) for x in range(0,7)] + [0,0]

def fish_growth(counts,days):
    for i in range(1,days+1):
        growth = counts.pop(0)
        counts.append(growth)
        counts[6] += growth
    return counts

print(sum(fish_growth(counts,80)))