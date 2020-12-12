puzzle_input = open("Day 5/puzzleinput.txt").read().splitlines()

def seat_search(s,span,lower,higher):
    options = [i for i in range(span)]
    for char in s:
        l = int(len(options)/2)
        if char == lower:
            del options[l:]
        if char == higher:
            del options[:l]
    return options[0]

def decode_row(s):
    return seat_search(s[0:7],128,"F","B")

def decode_column(s):
    return seat_search(s[7:],8,"L","R")

def seat_id(s):
    return ((decode_row(s) * 8) + decode_column(s))

list_of_ids = [seat_id(seat) for seat in puzzle_input]

missing = [s for s in range(min(list_of_ids),max(list_of_ids)) if s not in list_of_ids]

print(max(list_of_ids))
print(missing)