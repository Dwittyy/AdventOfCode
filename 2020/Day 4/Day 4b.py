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

def formatpassport(passport):
    passport_dict = {}
    list_of_values = passport.rsplit()
    for pair in list_of_values:
        field = pair[0:3]
        value = pair[4:]
        passport_dict[field] = value
    return passport_dict

def byr_valid(passport):
    return (1920 <= int(passport["byr"]) <= 2002)

def iyr_valid(passport):
    return (2010 <= int(passport["iyr"]) <= 2020)

def eyr_valid(passport):
    return (2020 <= int(passport["eyr"]) <= 2030)

def hgt_valid(passport):
    hgt = passport["hgt"]
    unit = hgt[-2:]
    if unit == "cm" and (150 <= int(hgt[0:-2]) <= 193):
        return True
    elif unit == "in" and (59 <= int(hgt[0:-2]) <= 76):
        return True
    else:
        return False

def hcl_valid(passport):
    hcl = passport["hcl"]
    if hcl[0] != "#":
        return False
    if len(hcl[1:]) != 6:
        return False
    for digit in hcl[1:]:
        if not digit.isnumeric() and digit not in ["a","b","c","d","e","f"]:
            return False
    return True

def ecl_valid(passport):
    return (passport["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"])

def pid_valid(passport):
    return (passport["pid"].isnumeric() and len(passport["pid"]) == 9)


passports = formatinput(puzzle_input)
fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
count = 0

for passport in passports:
    passport = formatpassport(passport)
    valid = True
    for field in fields:
        if field not in passport:
            valid = False
            break
    if valid == False:
        continue

    count += byr_valid(passport) * eyr_valid(passport) * iyr_valid(passport) * hgt_valid(passport) * hcl_valid(passport) * ecl_valid(passport) * pid_valid(passport)

print(count)
print(formatpassport(passports[0]))

    