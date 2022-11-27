import os, __main__

def read_lines(test=False):
    filename = os.path.join(os.path.dirname(__main__.__file__),"test.txt" if test else "input.txt")
    return open(filename).read().splitlines()

def read_nums(test=False):
    return [int(x) for x in read_lines(test)]