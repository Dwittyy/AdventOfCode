puzzle_input = open("AdventOfCode2020/Day 14/puzzleinput.txt").read().splitlines()

def masked(value,mask):
    value = str(bin(value).replace("0b","")).zfill(len(str(mask)))
    output = ""
    for valuedigit,maskdigit in zip(list(value),list(mask)):
        to_add = valuedigit if maskdigit == "X" else maskdigit
        output += to_add
    return int(output,base=2)

def Part1(lines):
    memory = dict()

    for line in lines:
        if "mask" in line:
            mask = line[7:]
        if "mem" in line:
            key, value = line.replace("mem","").replace("[","").replace("]","").replace(" ","").split("=")
            key, value = int(key), int(value)
            memory[key] = masked(value,mask)

    return sum(memory.values())

print(masked(4,"101X00"))
print(Part1(puzzle_input))