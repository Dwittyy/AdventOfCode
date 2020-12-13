puzzle_input = open("AdventOfCode2020/Day 13/puzzleinput.txt").read().splitlines()

from math import prod

start = int(puzzle_input[0])
buses = [int(i.replace("x","0")) for i in puzzle_input[1].split(",")]
constrained_buses = [(x,y) for x,y in list(enumerate(buses)) if y != 0]
mods = [((schedule - index) % schedule,schedule) for index,schedule in constrained_buses]


def Part1(starttime,buses):
    waittimes = [(bus - (starttime % bus)) for bus in buses if bus != 0]
    print(waittimes)
    index = waittimes.index(min(waittimes))
    print(index)
    return waittimes[index] * buses[index]

def validtimestamp(s,buses): # t is valid if t+(i) % (bus with index i) == 0 for x in constained_buses
    for i,bus in buses:
        if (s + i) % bus != 0 :
            return False
    else:
        return True

print(validtimestamp(556100168221141,constrained_buses)) # originally found using only calculator drcode.fr/chinese-remainder

def Part2():
    N = prod([n for a,n in mods])
    result = sum([a * (N // n) * pow(N // n,-1,n) for a,n in mods])
    return result % N

print(Part1(start,buses))
print(Part2())