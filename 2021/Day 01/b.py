import sys, os

sys.path.append(os.getcwd())
from util.read import read_nums

measurements = read_nums(2021, 1)


def count_increases(nums):
    count = 0
    for i in range(1, len(nums)):
        count += nums[i - 1] < nums[i]
    return count


def count_window_increases(nums):
    count = 0
    window = 3
    for i in range(1, len(nums) - window + 1):
        count += sum(nums[i - 1 : i - 1 + window]) < sum(nums[i : i + window])
    return count


def count_increases_full(nums, window):
    count = 0
    step = window - 1
    for i in range(1, len(nums) - step):
        count += nums[i - 1] < nums[i + step]
    return count


print(count_increases_full(measurements, 3))