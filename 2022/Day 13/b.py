import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run
import ast
from functools import cmp_to_key
from math import prod

def int_to_list(x):
    if isinstance(x, int):
        return [x]
    return x

def in_order(left, right):
    if isinstance(left,int) and isinstance(right,int):
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    
    elif isinstance(left, list) and isinstance(right,list):
        left_len = len(left)
        right_len = len(right)
        for i in range(max(left_len,right_len)):
            if i < min(left_len,right_len):
                compare = in_order(left[i],right[i])
                if compare is not None:
                    return compare
            elif i >= right_len:
                return False
            elif i >= left_len:
                return True
        else:
            return None
    else:
        return in_order(*map(int_to_list,(left,right)))

@run
def solve():
    packets = [ast.literal_eval(i) for i in read_lines() if i]
    dividers = ([[[2]],[[6]]])
    packets.extend(dividers)
    packets.sort(key=cmp_to_key(lambda x,y: -1 if in_order(x,y) else 1))
    return prod([packets.index(i)+1 for i in dividers])

solve()