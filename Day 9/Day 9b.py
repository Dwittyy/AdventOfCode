puzzle_input = open("Day 9/puzzleinput.txt").read().splitlines()

for i in range(len(puzzle_input)):
    puzzle_input[i] = int(puzzle_input[i])

def TwoSum(nums,target):
    for num in nums:
        complement = target - num
        if complement in nums and complement != num:
            return True
    else:
        return False

def FindFirst(nums,span):
    for i in range(span,len(nums)):
        if not TwoSum(nums[i-span:i],int(nums[i])):
            return nums[i]

def MultiSum(nums,target,base):
    j = 1
    while nums[j]:
        span = [nums[x] for x in range(base,j+1)]
        if sum(span) > target:
            return False
        if sum(span) == target:
            return min(span) + max(span)
        if sum(span) < target:
            j += 1
    return False


t = FindFirst(puzzle_input,25)

for i in range(len(puzzle_input)):
    if not MultiSum(puzzle_input,t,i):
        continue
    else:
        print(MultiSum(puzzle_input,t,i))
        break
