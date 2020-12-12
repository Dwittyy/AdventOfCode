puzzle_input = open("Day 9/puzzleinput.txt").read().splitlines()

for i in range(len(puzzle_input)):
    puzzle_input[i] = int(puzzle_input[i])

def TwoSum(nums,target):
    for num in nums:
        num = int(num)
        complement = target - num
        if complement in nums and complement != num:
            return True
    else:
        return False

l = 25

for i in range(l,len(puzzle_input)):
    if not TwoSum(puzzle_input[i-l:i],int(puzzle_input[i])):
        print(puzzle_input[i])
        break