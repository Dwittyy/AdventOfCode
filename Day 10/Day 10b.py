puzzle_input = [int(i) for i in open("Day 10/testpuzzleinput.txt").read().splitlines()]

puzzle_input.append(max(puzzle_input) + 3)
puzzle_input.append(0)
puzzle_input.sort()

def Part1(adapters):
    differences = [adapters[x+1] - adapters[x] for x in range(len(adapters)-1)]
    return differences.count(1) * differences.count(3)

print(Part1(puzzle_input))

def FindNecessary(adapters):
    adapters.sort()
    necessary = [adapters[0],adapters[-1]]
    for i in range(1,len(adapters)-1):
        if adapters[i] == adapters[i+1] - 3:
            necessary.append(adapters[i])
            continue
        if adapters[i] == adapters[i-1] + 3:
            necessary.append(adapters[i])
            continue
    necessary.sort()
    return necessary

def SplitSubs(nums):
    splits = []
    running = [nums[0]]
    for i in range(1,len(nums)):
        if nums[i-1] == nums[i] - 1:
            running.append(nums[i])
            continue
        else:
            splits.append(running)
            running = [nums[i]]
    splits.append(running)
    return splits

def CountCombinations(split):
    if len(split) == 1: return 2
    if len(split) == 2: return 4
    if len(split) == 3: return 7

def Product(nums):
    product = 1
    for x in nums:
        product *= x
    return product

remains = [x for x in puzzle_input if x not in FindNecessary(puzzle_input)]

print("a: ", puzzle_input)
print("n: ", FindNecessary(puzzle_input))
print("r: ",SplitSubs(remains))

print(Product([CountCombinations(x) for x in SplitSubs(remains)]))

