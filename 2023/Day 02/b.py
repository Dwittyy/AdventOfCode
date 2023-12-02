import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run
from math import prod

def parse_game(line):
    # cba for regex
    game, raw_draws = line.split(': ')
    game = int(game.split(' ')[1])
    draws = []
    for draw in raw_draws.split('; '):
        colours = dict()
        for colour in draw.split(', '):
            colour = colour.split(' ')
            colours[colour[1]] = int(colour[0])
        draws.append(colours)
    return (game, draws)

@run
def solve():
    sum_of_powers = 0
    for line in read_lines():
        game, draws = parse_game(line)
        minimums = {'red': 0, 'green': 0, 'blue': 0}
        for draw in draws:
            for colour in draw.keys():
                minimums[colour] = max(draw[colour], minimums[colour])
        sum_of_powers += prod(minimums.values())
    return sum_of_powers

solve()