import sys, os

sys.path.append(os.getcwd())
from util.read import *

entries = read_lines()

count = 0

for entry in entries:
    output_values = entry.split(" | ")[-1].split(" ")
    for value in output_values:
        if len(value) in [2,3,4,7]:
            count += 1

print(count)