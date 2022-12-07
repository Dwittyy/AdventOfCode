import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

def add_file(size,path,dirs):
    dirs[tuple(path)] += size
    path = path[:-1]
    if not path:
        return
    add_file(size,path,dirs)

@run
def solve():
    dirs = {tuple("/",): 0}
    current_dir = []
    for line in read_lines():
        split = line.split()
        if split[0] == "$":
            if split[1] == "cd":
                if split[2] == "..":
                    current_dir.pop()
                else:
                    current_dir.append(split[2])
        else:
            if split[0] == "dir":
                dirs[tuple(current_dir + [split[1]])] = 0
            else:
                add_file(int(split[0]),current_dir, dirs)
    unused_space = 70000000 - dirs[tuple("/",)]
    return min(size for size in dirs.values() if size >= 30000000 - unused_space)

solve()