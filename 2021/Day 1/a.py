import sys, os

sys.path.append(os.getcwd())
from util.read import read_nums

measurements = read_nums(2021, 1)


def count_increases(nums):
    count = 0
    for i in range(1, len(nums)):
        count += nums[i - 1] < nums[i]
    return count


print(count_increases(measurements))