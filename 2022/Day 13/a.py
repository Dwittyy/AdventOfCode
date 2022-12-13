import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run
import ast

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
    packet_pairs = [list(map(ast.literal_eval,i)) for i in read_sections()]
    ordered_pairs = [i+1 for i,pair in enumerate(packet_pairs) if in_order(*pair)]

    return sum(ordered_pairs)

solve()