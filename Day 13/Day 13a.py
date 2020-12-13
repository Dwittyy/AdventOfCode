puzzle_input = open("AdventOfCode2020/Day 13/puzzleinput.txt").read().splitlines()

start = int(puzzle_input[0])
buses = [int(i) for i in puzzle_input[1].split(",") if i != "x"]
print(buses)

remainders = [(bus - (start % bus)) for bus in buses]

index = remainders.index(min(remainders))

print(remainders[index] * buses[index])

print(index)
print(remainders)