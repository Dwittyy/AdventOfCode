import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run
from collections import defaultdict

def parse_numbers(numbers):
    numbers = set([int(x) for x in numbers.split(' ') if x.isdigit()])
    return numbers

def parse_card(line):
    card, numbers = line.split(': ')
    card = int(card.split(' ')[-1])
    winning, held = numbers.split(' | ')
    return card, (parse_numbers(winning), parse_numbers(held))

@run
def solve():
    lines = read_lines()
    cards = dict()
    for line in lines:
        card, numbers = parse_card(line)
        cards[card] = numbers
    copies = defaultdict(lambda: 1)
    for card in cards:
        if card not in copies:
            copies[card] = 1
        winning, held = cards[card]
        matches = len(winning.intersection(held))
        for i in range(card, card + matches):
            copies[i + 1] += 1 * copies.get(card,1)

    return sum(copies.values())

solve()