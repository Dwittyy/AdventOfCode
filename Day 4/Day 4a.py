puzzle_input = open("Day 4/puzzleinput.txt").read().splitlines()

def formatinput(puzzle_input):
    passports = []
    temp_passport = ""

    for i in range(len(puzzle_input)):
        if puzzle_input[i] != '':
            temp_passport += puzzle_input[i] + " "
        else:
            passports.append(temp_passport)
            temp_passport = ""
    return passports

passports = formatinput(puzzle_input)
 
count = 0

for passport in passports:
    if "byr" in passport:
        if "iyr" in passport:
            if "eyr" in passport:
                if "hgt" in passport:
                    if "hcl" in passport:
                        if "ecl" in passport:
                            if "pid" in passport:
                                count += 1

print(count)