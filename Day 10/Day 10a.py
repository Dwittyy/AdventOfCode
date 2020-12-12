puzzle_input = [int(i) for i in open("Day 10/puzzleinput.txt").read().splitlines()]

puzzle_input.append(max(puzzle_input) + 3)
puzzle_input.append(0)
puzzle_input.sort()

differences = [puzzle_input[x+1] - puzzle_input[x] for x in range(len(puzzle_input)-1)]

print(puzzle_input)
print(differences)
ones = differences.count(1)
threes = differences.count(3)
print(ones * threes)
