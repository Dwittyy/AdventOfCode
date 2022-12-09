import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

dirs = {"U": (0,1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}

def move(p, d):
    return (p[0] + d[0], p[1] + d[1])

def drag(dragger,dragee):
    diff = (dragger[0] - dragee[0], dragger[1] - dragee[1])

    if abs(diff[0]) <= 1 and abs(diff[1]) <= 1:
        return dragee
        
    direction = [(int(x/abs(x) if x != 0 else 0)) for x in diff]
    return move(dragee, direction)

@run
def solve():
    head = tail = (0,0)
    tail_visited = set()
    for motion in read_lines():
        char, num = motion.split()
        direction = dirs[char]
        amount = int(num)

        for _ in range(amount):
            head = move(head, direction)
            tail = drag(head, tail)
            tail_visited.add(tail)

    return len(tail_visited)

solve()