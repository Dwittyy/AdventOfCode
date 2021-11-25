puzzle_input = [1,20,8,12,0,14]

turns = list(enumerate(puzzle_input,start=1))

seen = {num:turn for turn,num in turns}

for i in range(7,2021):
    previousnum = turns[i-2][1]
    if previousnum not in seen:
        thisturn = (i,0)
    else:
        thisturn = (i,(i-1)-seen[previousnum])
    seen[previousnum] = i-1
    turns.append(thisturn)

print(turns[-1])