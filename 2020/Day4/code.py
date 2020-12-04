import os

filename = "data.txt"

def OpenInput(filename, mode = "r"):
    return open(filename, mode)
    
def IsBirthYearValid(value):
    return value.isdigit() and int(value) >= 1920 and int(value) <= 2002

def IsIssueYearValid(value):
    return value.isdigit() and int(value) >= 2010 and int(value) <= 2020
    
def IsExpirationYearValid(value):
    return value.isdigit() and int(value) >= 2020 and int(value) <= 2030
    
def IsPassportIDValid(value):
    return len(value) == 9 and value.isdigit() and int(value) >= 000000000 and int(value) <= 999999999
    
def IsEyeColorValid(value):
    valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    is_valid = value in valid_eye_colors
    return is_valid
    
def IsHairColorValid(value):
    is_valid = False
    valid_values = "0123456789abcdef"
    if len(value) == 7 and value[0] == "#":
        is_valid = True
        for i in range(1, 7):
            is_valid = is_valid and value[i] in valid_values
    return is_valid
    
def IsHeightValid(value):
    is_valid = False
    index_cm = value.find("cm")
    index_in = value.find("in")
    if index_cm != -1:
        height = int(value[0:index_cm])
        is_valid = height >= 150 and height <= 193
    elif index_in != -1:
        height = int(value[0:index_in])
        is_valid = height >= 59 and height <= 76
    return is_valid
    
def IsPassportValid(value, required_fields, optional_fields):
    part_one_valid = False
    if len(value) == (len(required_fields) + len(optional_fields)):
        part_one_valid = True
    elif len(value) == len(required_fields) and not value.get(optional_fields[0]):
        part_one_valid = True
    
    part_two_valid = part_one_valid
    if part_two_valid:
        for field in value:
            if field in optional_fields:
                continue
            if not part_two_valid:
                break
            part_two_valid = part_two_valid and field in value and required_fields[field](value[field])
    
    return part_one_valid, part_two_valid

def CountValidPassports(filename):
    required_fields = {"byr":IsBirthYearValid, "iyr":IsIssueYearValid, "eyr":IsExpirationYearValid, "hgt":IsHeightValid, "hcl":IsHairColorValid, "ecl":IsEyeColorValid, "pid":IsPassportIDValid}
    optional_fields = ["cid"]
    
    passports = []
    passports.append({})
    passport_index = 0
    
    with OpenInput(filename) as in_file:
        for line in in_file.readlines():
            line = line.strip(os.linesep)
            if not line:
                passports.append({})
                passport_index += 1
            else:
                passports[passport_index].update(dict(subStr.split(":") for subStr in line.split(" ")))
        
    total = 0
    total_part_two = 0
    for elt in passports:
        part_one_valid, part_two_valid = IsPassportValid(elt, required_fields, optional_fields)
        if part_one_valid:
            total += 1
        if part_two_valid:
            total_part_two += 1
            
    print("Part one : {} valid passports".format(total))
    print("Part two : {} valid passports".format(total_part_two))
    
CountValidPassports(filename)