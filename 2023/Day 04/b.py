import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

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
    copies = dict()
    for line in read_lines():
        card, (winning, held) = parse_card(line)
        matches = len(winning & held)
        if card not in copies:
            copies[card] = 1
        for i in range(card, card + matches):
            copies[i + 1] = copies.get(i + 1, 1) + copies.get(card, 1)

    return sum(copies.values())

solve()