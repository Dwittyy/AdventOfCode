import sys, os

sys.path.append(os.getcwd())
from util.read import read
import networkx as nx

G = nx.Graph()
for line in read(2021,12):
    G.add_edge(line.split("-")[0],line.split("-")[1])

def paths(G,x,y,used,result_paths):
    if x == y:
        result_paths.add(str(used + [y]))
    else:
        neighbours = [n for n in G.neighbors(x) if n not in used or n.isupper()]
        for n in neighbours:
            paths(G,n,y,used + [n],result_paths)
                  
results = set()
paths(G,"start","end",["start"],results)
print(len(results))