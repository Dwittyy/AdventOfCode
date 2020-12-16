puzzle_input = open("AdventOfCode2020/Day 16/puzzleinput.txt").read().splitlines()

import math
import time
starttime = time.time()

def ParseField(line):
    line = line.split(':')

    field = line[0]

    line[1] = line[1].replace(' ','').split('or')
    spans = []
    for span in line[1]:
        newspan = span.split('-')
        spans.append((int(newspan[0]),int(newspan[1])))
    return field, spans

def IsValid(num,conditions):
    for spans in conditions.values():
        for span in spans:
            if span[0] <= num <= span[1]:
                return True
    return False

def ValidFields(num,conditions):
    validfields = []
    for field in conditions:
        spans = conditions[field]
        if IsValid(num,{field:spans}):
            validfields.append(field)
    return validfields

def IsTicketValid(ticket):
    for num in ticket:
        num = int(num)
        if not IsValid(num,fields):
            return False
    return True

def FindGimmes(dictionary):
    gimmes = []
    for key in list(dictionary.keys()):
        if len(dictionary[key]) == 1:
            gimmes.append((key,dictionary[key].pop()))
    return gimmes

def FindOptions(tickets,fields):
    alloptions = dict()

    for i in range(20):
        options = set(fields.keys())
        for ticket in tickets:
            for index,num in enumerate(ticket):
                if index != i:
                    continue
                num = int(num)
                vfields = set(ValidFields(num,fields))
                options = options.intersection(vfields)
        alloptions[i] = options
    return alloptions

def RemoveGimmes(dictionary,gimmes):
    for gimme in gimmes:
        gimmefield = gimme[1]
        for key in dictionary:
            if gimmefield in dictionary[key]:
                dictionary[key].remove(gimmefield)

def GimmeStep(options):
    gimmes = FindGimmes(options)
    RemoveGimmes(options,gimmes)
    finals.append(gimmes)
    #print(gimmes)
    #print(options)

fields = {key:value for key,value in [ParseField(x) for x in puzzle_input[:20]]}
tickets = [x.split(',') for x in puzzle_input[25:] if IsTicketValid(x.split(','))]

options = FindOptions(tickets,fields)

finals = []

while len(finals) < 20:
    GimmeStep(options)

print(finals)

departurefields = [x for x in finals if "departure" in x[0][1]]

myticket = puzzle_input[22].split(',')

result = 1

for field in departurefields:
    column = int(field[0][0])
    result *= int(myticket[column])

print(result)
print(round(time.time() - starttime,3))