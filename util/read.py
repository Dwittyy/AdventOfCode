def read(year, day):
    return open(f"{year}\Day {str(day).zfill(2)}\input.txt").read().splitlines()

def read_nums(year, day):
    return [int(x) for x in read(year, day)]