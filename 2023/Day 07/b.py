import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

def card_strength(card):
    return "J23456789TQKA".index(str(card))

def hand_strength(hand):
    counts = {}
    for char in hand:
        counts[char] = counts.get(char,0) + 1
    if "J" in counts.keys():
        jokers = counts.pop("J")
        if not counts.keys(): return 6
        counts[max(counts,key=counts.get)] += jokers
    if 5 in counts.values(): return 6
    if 4 in counts.values(): return 5
    if 3 in counts.values():
        if 2 in counts.values(): return 4
        return 3
    if list(counts.values()).count(2) == 2: return 2
    if list(counts.values()).count(2) == 1: return 1
    return 0

@run
def solve():
    hands = []
    for line in read_lines():
        hand, bid = line.split(' ')
        strengths = [hand_strength(hand)]
        for char in hand:
            strengths.append(card_strength(char))
        hands.append(strengths + [int(bid)])
        # Each hand is represented by a list of length 7 - hand strength, each card's strength, then bid
    hands.sort()
    total_winnings = 0
    for i, hand in enumerate(hands):
        total_winnings += hand[-1] * (i + 1)
    return total_winnings

solve()