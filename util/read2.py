import aocd, os, re, __main__

def read_file(test=False):
    current_dir = os.path.dirname(__main__.__file__)
    input_file  = os.path.join(current_dir, "input.txt")
    test_file   = os.path.join(current_dir, "test.txt")

    if test:
        with open(test_file) as f:
            return f.read()
    
    if not os.path.isfile(input_file):
        year, day = re.search(r"(\d{4})[\\/]Day (\d{2})", current_dir).groups()
        with open(input_file, "w") as f:
            f.write(aocd.get_data(day=int(day), year=int(year)))

    with open(input_file) as f:
        return f.read()

def read_lines(test=False):
    return read_file(test).splitlines()

def read_nums(test=False):
    return [int(x) for x in read_lines(test)]

def read_sections(test=False):
    return [x.splitlines() for x in read_file(test).split("\n\n")]