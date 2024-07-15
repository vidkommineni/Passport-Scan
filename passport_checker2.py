
# scanned_passports.txt
# functions to check every key depending on conditions
def byr_check(i):  # 4-digit, 1920 - 2005
    value = i.split(':')
    if value[0] == 'byr':
        if 1920 <= int(value[1]) <= 2005:
            return 1
        return 0
    return 0


def iyr_check(i):  # 4-digits, 2012 - 2022
    value = i.split(':')
    if value[0] == 'iyr':
        if 2012 <= int(value[1]) <= 2022:
            return 1
        return 0
    return 0


def eyr_check(i):  # 4-digits 2022 - 2032
    value = i.split(':')
    if value[0] == 'eyr':
        if 2022 <= int(value[1]) <= 2032:
            return 1
        return 0
    return 0


def hgt_check(i):  # cm, 150 - 193 | in, 59 - 76
    value = i.split(':')
    if value[0] == 'hgt':
        if 'cm' in value[1]:
            newVal = value[1].split('cm')
            if 150 <= int(newVal[0]) <= 193:
                return 1
        if 'in' in value[1]:
            newVal = value[1].split('in')
            if 59 <= int(newVal[0]) <= 76:
                return 1
        return 0
    return 0


def ecl_check(i):  # one of the following: amb, blu, brn, gry, grn, hzl, oth
    value = i.split(':')
    if value[0] == 'ecl':
        if (value[1] == 'amb' or value[1] == 'blu' or value[1] == 'brn' or value[1] == 'gry'
                or value[1] == 'grn' or value[1] == 'hzl' or value[1] == 'oth'):
            return 1
    return 0


def pid_check(i):  # 9-digits, including leading zeros
    value = i.split(':')
    if value[0] == 'pid':
        if len(value[1]) == 9:
            return 1
        return 0
    return 0


def cid_check(i):  # 3-digit number, NOT including leading zeroes
    value = i.split(':')
    if value[0] == 'cid':
        if len(str(int(value[1]))) == 3:
            return 1
        return 0
    return 0


def passportCheck(passport):
    count = 0
    line = []
    # made a list of the terms that we are checking for
    required_terms = ["byr", "iyr", "eyr", "hgt", "ecl", "pid", "cid"]

    for x in passport:
        line += x.split(' ')
    for i in line:
        # call check functions
        for j in required_terms:
            if i.find(j) >= 0:
                count += byr_check(i)
                count += iyr_check(i)
                count += eyr_check(i)
                count += hgt_check(i)
                count += ecl_check(i)
                count += pid_check(i)
                count += cid_check(i)
    if count == 7:
        return True
    return False


passed = 0
valid = []
filename = input('Enter the name of the file: ')
# scanned_passports.txt
with open(filename, "r") as file:
    lineList = file.read()
    lineList = lineList.split('\n\n')
    for i in lineList:
        if passportCheck(i.split('\n')):
            valid += [i]
            passed += 1

with open('valid_passports2.txt', 'w') as validPassports:
    for x in valid:
        validPassports.write(x + '\n\n')

print(f'There are {passed} valid passports')
