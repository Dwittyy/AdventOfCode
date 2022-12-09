import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

directions = {"U": (0,1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}

def drag(dragger,dragee):
    diff = (dragger[0] - dragee[0],dragger[1] - dragee[1])

    if diff in [(0,2), (0,-2), (2,0), (-2,0)]:
        new_dragee = (dragee[0] + int(diff[0] / 2), dragee[1] + int(diff[1] / 2))

    elif diff in [(2,1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2), (2, 2), (2, -2), (-2, 2), (-2, -2)]:
        new_diff = [int(x/abs(x)) for x in diff]
        new_dragee = (dragee[0] + new_diff[0], dragee[1] + new_diff[1])

    else:
        new_dragee = dragee

    return new_dragee

@run
def solve():
    knots = {i: (0,0) for i in range(0,10)}
    tail_visited = set()
    for motion in read_lines():
        direction, amount = motion.split()
        direction = directions[direction]
        amount = int(amount)

        for _ in range(amount):
            knots[0] = (knots[0][0] + direction[0], knots[0][1] + direction[1])
            for k in range(1,10):
                knots[k] = drag(knots[k-1], knots[k])
            tail_visited.add(knots[9])
            
    return len(tail_visited)

solve()