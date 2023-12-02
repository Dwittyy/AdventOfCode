import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

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
    maximums = {'red': 12, 'green': 13, 'blue': 14}
    sum_of_possible_games = 0
    for line in read_lines():
        game, draws = parse_game(line)
        possible = True
        for draw in draws:
            for colour in draw.keys():
                if draw[colour] > maximums[colour]:
                    possible = False
        if possible:
            sum_of_possible_games += game
    return sum_of_possible_games

solve()