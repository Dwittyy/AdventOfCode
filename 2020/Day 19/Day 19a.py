puzzle_input = open("AdventOfCode/2020/Day 19/puzzleinput.txt").read().splitlines()

def FormatInput(input):
    rules = dict()

    for line in input:
        if not line:
            break
        extracted = line.split(':')
        rules[int(extracted[0])] = extracted[1].lstrip().replace('"',"")
    return rules


def FindDecoded(rules):
    decodedrules = dict()
    for key in rules:
        value = rules[key]
        if not any(item in value for item in "0123456789"):
            rules[key] = value.replace(' ','')
        if rules[key].isalpha():
            decodedrules[key] = rules[key]
    return decodedrules

def Decode(rules,decoded):
    for k1 in decoded:
        for k2 in rules:
            rules[k2] = rules[k2].replace(str(k1),decoded[k1])
    return rules

rules = FormatInput(puzzle_input)

#while not rules[0].isalpha():
for i in range(2):
    decoded = FindDecoded(rules)
    print(decoded)
    rules = Decode(rules,decoded)
    print(rules)

