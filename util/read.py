import sys, os


def read(year, day):
    with open(f"{year}\Day {day}\input.txt") as f:
        return f.read().splitlines()


def read_nums(year, day):
    with open(f"{year}\Day {day}\input.txt") as f:
        return [int(x) for x in f.read().splitlines()]