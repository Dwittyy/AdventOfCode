puzzle_input = [1,20,8,12,0,14]

def ElfGame(firstnums,n):
    seen = {num:turn for turn,num in list(enumerate(firstnums,start=1))[:-1]} # A dictionary that stores the turn (value) that each number (key) was last seen.
    previousnum = firstnums[-1]

    for i in range(len(firstnums)+1,n+1):
        thisturnnum = 0 if previousnum not in seen else (i - 1 - seen[previousnum])
        seen[previousnum] = i - 1
        previousnum = thisturnnum

    return thisturnnum

print(ElfGame(puzzle_input,2020))