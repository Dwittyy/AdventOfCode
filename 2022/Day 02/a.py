import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

opponent_moves = {"A": "Rock", "B": "Paper", "C": "Scissors"}
my_moves = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
scores = {"Rock": 1, "Paper": 2, "Scissors": 3}
better = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}

@run
def solve():
    strategy_guide = read_lines()
    total_score = 0
    for match in strategy_guide:
        my_move = my_moves[match[2]]
        opponent_move = opponent_moves[match[0]]
        if my_move == better[opponent_move]:
            total_score += 6
        elif opponent_move == better[my_move]:
            total_score += 0
        else:
            total_score += 3
        total_score += scores[my_move]

    return total_score

solve()