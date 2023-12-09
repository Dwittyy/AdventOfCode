import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

def subsequence(sequence):
    subsequence = []
    for i in range(1,len(sequence)):
        subsequence.append(sequence[i] - sequence[i-1])
    return subsequence

def extrapolate(sequence, ends):
    ends.append(sequence[-1])
    if all(x == 0 for x in sequence):
        return ends
    return extrapolate(subsequence(sequence),ends)

@run
def solve():
    report = read_lines()
    total_sum = 0
    for history in report:
        history = [int(x) for x in history.split()]
        ends = extrapolate(history,[])
        total_sum += sum(ends)
    return total_sum

solve()