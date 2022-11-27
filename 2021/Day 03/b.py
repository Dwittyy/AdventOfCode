import sys, os

sys.path.append(os.getcwd())
from util.read import *

diagnostic_report = read_lines()


def frequent_bit(bits, extreme):
    if extreme == "most":
        result = "1" if bits.count("1") >= bits.count("0") else "0"
    else:
        result = "0" if bits.count("1") >= bits.count("0") else "1"
    return result


def find_rating(nums, extreme):
    options = nums.copy()
    for i in range(0, len(nums[0])):
        frequent = frequent_bit([option[i] for option in options], extreme)
        options = [bits for bits in options if bits[i] == frequent]
        if len(options) == 1:
            break
    return int(options[0], 2)


life_support_rating = find_rating(diagnostic_report, "most") * find_rating(
    diagnostic_report, "least"
)

print(life_support_rating)
