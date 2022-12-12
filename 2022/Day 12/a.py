import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run
import networkx as nx

def elevation(char):
    return ord(char.replace("S","a").replace("E","z"))

@run
def solve():
    heightmap = read_lines()
    g = nx.DiGraph()
    width = len(heightmap[0])
    height = len(heightmap)
    ends = dict()
    for r in range(height):
        for c in range(width):
            if heightmap[r][c] in ("S","E"):
                ends[heightmap[r][c]] = (r,c)
                
            for nr, nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if (nr in range(height)) and (nc in range(width)) and (elevation(heightmap[nr][nc]) <= elevation(heightmap[r][c]) + 1):
                    g.add_edge((r,c),(nr,nc))

    return nx.shortest_path_length(g,source=ends["S"],target=ends["E"])

solve()