import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run

def get_digit(line,backwards=False):
    word_digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    l = len(line)
    for i in range(l):
        if backwards:
            i = -i-1
        if line[i].isdigit():
            return line[i]
        for word in word_digits.keys():
            if line.startswith(word,i):
                return word_digits[word]

@run
def solve():
    document = read_lines()
    total_calibration = 0
    for line in document:
        total_calibration += int(str(get_digit(line)) + str(get_digit(line,backwards=True)))
    return total_calibration

solve()