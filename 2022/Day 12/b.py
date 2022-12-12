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
    for row in range(height):
        for col in range(width):
            if heightmap[row][col] in ("S","E"):
                ends[heightmap[row][col]] = (row,col)
            for nr, nc in ((row-1,col),(row+1,col),(row,col-1),(row,col+1)):
                if (nr in range(height)) and (nc in range(width)) and (elevation(heightmap[nr][nc]) <= elevation(heightmap[row][col]) + 1):
                    g.add_edge((row,col),(nr,nc))
            else:
                g.add_node((row,col))

    shortest = 2 * width * height
    for n in g:
        if heightmap[n[0]][n[1]] == "a" and nx.has_path(g, n, ends["E"]):
            shortest = min(shortest,nx.shortest_path_length(g,source=n,target=ends["E"]))

    return shortest

solve()