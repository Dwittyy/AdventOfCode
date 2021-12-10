import sys, os

sys.path.append(os.getcwd())
from util.read import read, read_nums
from statistics import median

subsystem = read(2021, 10)

def autocomplete(line):
    opened = []
    for char in line:
        if char in "([{<":
            opened.append(char)
        elif (opened[-1],char) in [("(",")"),("[","]"),("{","}"),("<",">")]:
            opened.pop()          
        else:
            return False
    autocompletion = ""
    for char in opened[::-1]:
        autocompletion += {"(": ")", "[": "]", "{": "}", "<": ">"}[char]
    return autocompletion

def autocomplete_score(lines):
    scores = []
    for line in lines:
        autocompletion = autocomplete(line)
        if not autocompletion:
            continue
        line_score = 0
        for char in autocompletion:
            line_score = (line_score * 5) + {")": 1, "]": 2, "}": 3, ">": 4}[char]
        scores.append(line_score)
    return median(scores)

print(autocomplete_score(subsystem))