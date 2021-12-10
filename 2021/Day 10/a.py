import sys, os

sys.path.append(os.getcwd())
from util.read import read, read_nums

subsystem = read(2021, 10)

def first_illegal_character(line):
    opened = []
    for char in line:
        if char in "([{<":
            opened.append(char)
        elif (opened[-1],char) in [("(",")"),("[","]"),("{","}"),("<",">")]:
            opened.pop()          
        else:
            return char
    return None

def syntax_error_score(lines):
    score = 0
    for line in lines:
        score += {")": 3, "]": 57, "}": 1197, ">": 25137, None: 0}[first_illegal_character(line)]
    return score

print(syntax_error_score(subsystem))