import sys, os
sys.path.append(os.getcwd())
from util.read import *
from util.run import run
from math import prod, lcm

class Monkey():
    def __init__(self, lines):
        self.num = lines[0][-2]
        self.items = [int(x) for x in lines[1].replace("Starting items: ","").split(", ")]
        self.op = lines[2].split()[-2]
        self.op_value = lines[2].split()[-1]
        self.test = int(lines[3].split()[-1])
        self.if_true = int(lines[4][-1])
        self.if_false =  int(lines[5][-1])
        self.inspections = 0
        return

    def inspect(self):
        item = self.items.pop(0)
        op_value = int(self.op_value.replace("old",str(item)))
        match self.op:
            case "+":
                item += op_value
            case "*":
                item *= op_value
        self.inspections += 1
        return item
    
    def turn(self, mod_lcm):
        throws = []
        while len(self.items) > 0:
            worry = self.inspect()
            worry = worry % mod_lcm
            passed = (worry % self.test == 0)
            receiver = (self.if_false, self.if_true)[passed]
            throws.append((worry, receiver))
        return throws
    
@run
def solve():
    monkeys = [Monkey(lines) for lines in read_sections()]
    mod_lcm = lcm(*[monkey.test for monkey in monkeys])
    for _ in range (10000):
        for monkey in monkeys:
            for throw in monkey.turn(mod_lcm):
                worry, receiver = throw
                monkeys[receiver].items.append(worry)
    return prod(sorted([m.inspections for m in monkeys],reverse=True)[:2])

solve()