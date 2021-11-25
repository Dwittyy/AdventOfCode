puzzle_input = [int(i) for i in open("Day 9/puzzleinput.txt").read().splitlines()]

def TwoSum(nums,target):
    for num in nums:
        complement = target - num
        if complement in nums and complement != num: return True
    else: return False

def Part1(nums,l):
    return next((nums[i] for i in range(l,len(nums)) if not TwoSum(nums[i-l:i],nums[i])))

t = Part1(puzzle_input,25)

def MultiSum(nums,target,base):
    j = 1
    span = [nums[base]]
    while sum(span) <= target:
        span.append(nums[base+j])
        if sum(span) == target: return min(span) + max(span)
        j += 1
    return False

for i in range(len(puzzle_input)):
    result = MultiSum(puzzle_input,t,i)
    if result:
        print(result)
        break