import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

directions = {"U": (0,1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}

def move(head, tail, direction):
    new_head = (head[0] + direction[0], head[1] + direction[1])
    diff = (new_head[0] - tail[0],new_head[1] - tail[1])

    if diff in [(0,2), (0,-2), (2,0), (-2,0)]:
        new_tail = (tail[0] + int(diff[0] / 2), tail[1] + int(diff[1] / 2))

    elif diff in [(2,1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]:
        new_diff = [int(x/abs(x)) for x in diff]
        new_tail = (tail[0] + new_diff[0], tail[1] + new_diff[1])

    else:
        new_tail = tail

    return new_head, new_tail

@run
def solve():
    head = tail = (0,0)
    tail_visited = set()
    for motion in read_lines():
        direction, amount = motion.split()
        direction = directions[direction]
        amount = int(amount)

        for _ in range(amount):
            head, tail = move(head,tail,direction)
            tail_visited.add(tail)
            
    return len(tail_visited)

solve()