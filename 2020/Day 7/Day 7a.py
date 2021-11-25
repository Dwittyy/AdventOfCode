puzzle_input = open("Day 7/puzzleinput.txt").read().splitlines()

def parse_bagulation(line):
    splitter = line.split(' contain ')
    key = splitter[0].replace(' bags','')
    value = splitter[1].replace(' bags','').replace(' bag','').replace('.','')
    output = {key:value}
    return output

bagulations = [parse_bagulation(b) for b in puzzle_input]

colour = "shiny gold"

def find_containers(colour,bagulations):
    containers = set()
    for bagulation in bagulations:
        bag = list(bagulation.keys())[0]
        if colour in bagulation[bag]:
            containers.add(bag)
    return containers

to_search = {colour}
containers = set()
searched = set()

while to_search:
    for container in to_search:
        containers.update(find_containers(container,bagulations))
        searched.add(container)
    to_search = {c for c in containers if c not in searched}

print(containers)
print(to_search)
print(searched.difference(containers))
print(len(containers))