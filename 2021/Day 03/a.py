import sys, os

sys.path.append(os.getcwd())
from util.read import *

diagnostic_report = read_lines()


def most_frequent_bit(bits):
    if bits.count("1") > bits.count("0"):
        return "1"
    else:
        return "0"


def find_power_consumption(nums):
    l = len(nums[0])
    gamma = ""
    epsilon = ""
    for i in range(0, l):
        frequent = most_frequent_bit([num[i] for num in nums])
        gamma += frequent
        epsilon += "1" if frequent == "0" else "0"
    return int(gamma, 2) * int(epsilon, 2)


print(find_power_consumption(diagnostic_report))