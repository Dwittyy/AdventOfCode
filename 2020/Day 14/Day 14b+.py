puzzle_input = open("AdventOfCode2020/Day 14/puzzleinput.txt").read().splitlines()

from itertools import product

def masked(address,mask):
    address = str(bin(address).replace("0b","")).zfill(len(str(mask)))
    output = ""
    for addressdigit,maskdigit in zip(list(address),list(mask)):
        if maskdigit == "0":
            output += addressdigit
        else:
            output += maskdigit
    
    if "X" not in output:
        return [int(output,base=2)]

    return floats(output)

def floats(string):
    combs = list(product(["0","1"],repeat=string.count("X")))
    outputlist = []
    for comb in combs:
        output = string
        i = 0
        while "X" in output:
            output = output.replace("X",comb[i],1)
            i += 1
        outputlist.append(int(output,base=2))
    return outputlist

def Part2(lines):
    memory = dict()

    for line in lines:
        if "mask" in line:
            mask = line[7:]
        if "mem" in line:
            key, value = [int(x) for x in line.replace("mem","").replace("[","").replace("]","").replace(" ","").split("=")]
            for num in masked(key,mask):
                memory[num] = value

    return sum(memory.values())

print(Part2(puzzle_input))


