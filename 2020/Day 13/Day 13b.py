puzzle_input = open("AdventOfCode2020/Day 13/puzzleinput.txt").read().splitlines()

from math import prod

buses = [int(i.replace("x","0")) for i in puzzle_input[1].split(",")]
constrained_buses = [(x,y) for x,y in list(enumerate(buses)) if y != 0]

def waittime(bus,t):
    return bus - (t % bus)

# t is valid if t+(i) % (bus with index i) == 0 for x in constained_buses

print(constrained_buses)

t = 100000000000000

def validtimestamp(s,buses):
    for i,bus in buses:
        if (s + i) % bus != 0 :
            return False
    else:
        return True

for x,y in constrained_buses:
    print((y - x) % y, "mod", y)

print(validtimestamp(556100168221141,constrained_buses)) # found using only calculator drcode.fr/chinese-remainder