puzzle_input = open("AdventOfCode/2020/Day 16/puzzleinput.txt").read().splitlines()

def ParseField(line):
    output =[]
    line = line.split(':')
    output.append(line[0])

    line[1] = line[1].replace(' ','').split('or')
    for span in line[1]:
        newspan = span.split('-')
        output.append((int(newspan[0]),int(newspan[1])))
    return output

def IsValid(num,ranges):
    for span in ranges:
        if span[0] <= num <= span[1]:
            return True
    return False

fields = [y for x in puzzle_input[:20] for y in ParseField(x)[1:]]

tickets = [x.split(',') for x in puzzle_input[25:]]

invalid = []

for ticket in tickets:
    for num in ticket:
        num = int(num)
        if not IsValid(num,fields):
            invalid.append(num)

print(sum(invalid))