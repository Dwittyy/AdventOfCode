puzzle_input = open("AdventOfCode/2020/Day 14/puzzleinput.txt").read().splitlines()

from itertools import product

def masked(address,mask):
    address = str(bin(address).replace("0b","")).zfill(len(str(mask)))
    output = ""
    for addressdigit,maskdigit in zip(list(address),list(mask)):
        if maskdigit == "0":
            output += addressdigit
        if maskdigit == "1":
            output += "1"
        if maskdigit == "X":
            output += "F"
    
    if "F" not in output:
        return [int(output,base=2)]

    return floats(output)

def floats(string):
    count = string.count("F")
    combs = list(product(["0","1"],repeat=count))
    outputlist = []
    for comb in combs:
        output = str(string)
        i = 0
        while "F" in output:
            output = output.replace("F",comb[i],1)
            i += 1
        outputlist.append(int(output,base=2))
    return outputlist

def Part2(lines):
    memory = dict()

    for line in lines:
        if "mask" in line:
            mask = line[7:]
        if "mem" in line:
            key, value = line.replace("mem","").replace("[","").replace("]","").replace(" ","").split("=")
            key, value = int(key), int(value)
            for num in masked(key,mask):
                memory[num] = value

    return sum(memory.values())

print(Part2(puzzle_input))


