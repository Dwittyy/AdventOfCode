puzzle_input = open("Day 7/puzzleinput.txt").read().splitlines()

def parse_bagulation(line):
    splitter = line.split(' contain ')
    key = splitter[0].replace(' bags','')
    values = splitter[1].replace(' bags','').replace(' bag','').replace('.','').split(', ')
    dictlist = []
    for value in values:
        if value == "no other":
            dictlist = 0
            continue
        temp_list = value.split(' ')
        colour = temp_list[1] + " " + temp_list[2]
        amount = int(temp_list[0])
        newdict = {"colour": colour, "amount": amount}
        dictlist.append(newdict)
    return (key,dictlist)

bagulations = {}

for line in puzzle_input:
    key, dictlist = parse_bagulation(line)
    bagulations[key] = dictlist

def containees(colour,num):
    containees = bagulations[colour]
    for bag in containees:
        bag["amount"] *= num
    return containees

colour = "shiny gold"

allbags = dict()
to_search = [{colour: 1}]
searched = dict()

while to_search:
    for bag in to_search:
        c = list(bag.keys())[0]
        n = bag[c]
        print(bagulations[c])
        containees = bagulations[c]
        if containees == 0:
            print("empty bag!")
            to_search.remove(bag)
            continue
        for inner in containees:
            innerc = inner["colour"]
            innern = inner["amount"] * n
            if innerc in allbags:
                allbags[innerc] += innern
            else:
                allbags[innerc] = innern
            to_search.append({innerc: innern})
        to_search.remove(bag)

print(sum(allbags.values()))
print(allbags)


