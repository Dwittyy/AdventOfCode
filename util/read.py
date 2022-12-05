import os, __main__

def read_file(test=False):
    return open(os.path.join(os.path.dirname(__main__.__file__),"test.txt" if test else "input.txt")).read()

def read_lines(test=False):
    return read_file(test).splitlines()

def read_nums(test=False):
    return [int(x) for x in read_lines(test)]

def read_sections(test=False):
    return [x.splitlines() for x in read_file(test).split("\n\n")]