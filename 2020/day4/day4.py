VALID_KEYS = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
REQUIRED_KEYS = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

def part1(string: str):
    passports = parse_passports(string)
    valid_passports = [check_if_passport_is_valid(passport) for passport in passports]
    return sum(valid_passports)

def part2(string: str):
    passports = parse_passports(string)
    valid_passports = filter(check_if_passport_is_valid, passports)
    valid_passports = [check_if_fields_are_valid(passport) for passport in valid_passports]
    return sum(valid_passports)

def check_if_fields_are_valid(passport) -> bool:
    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return False 
    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return False 
    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return False 
    if not check_height(passport['hgt']):
        return False
    if not check_hair_color(passport['hcl']):
        return False
    if not check_eye_color(passport['ecl']):
        return False
    if not check_passport_id(passport['pid']):
        return False
    return True


def check_passport_id(pid) -> bool:
    if len(pid) != 9:
        return False
    for digit in pid:
        if digit not in '0123456789':
            return False
    return True

def check_eye_color(ecl) -> bool:
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def check_hair_color(hcl) -> bool:
    if len(hcl) != 7:
        return False
    if hcl[0] != "#":
        return False
    for character in hcl[1:]:
        if character not in '0123456789abcdef':
            return False
    return True

def check_height(height) -> bool:
    if len(height) < 3:
        return False
    prefix = int(height[:-2])
    suffix = height[-2:]
    if suffix == "cm":
        if prefix >= 150 and prefix <= 193:
            return True
    if suffix == "in":
        if prefix >= 59 and prefix <= 76:
            return True
    return False 

def parse_passports(string: str):
    passports_raw = string.split('\n\n')
    passports_raw = [passport.split() for passport in passports_raw]
    passports = []
    for passport_raw in passports_raw:
        passport = {}
        for field in passport_raw:
            key, value = field.split(':')
            passport[key] = value
        passports.append(passport)
    return passports

def check_if_passport_is_valid(passport) -> bool:
    present_keys = sorted([key for key in passport.keys()])
    if present_keys == VALID_KEYS:
        return True
    if present_keys == REQUIRED_KEYS:
        return True
    return False


def is_valid_passport(passport) -> bool:
    encountered = []
    for field in passport:
        key = field[0]
        if key not in VALID_KEYS:
            return False
        if key not in encountered:
            encountered.append(key)
        else:
            return False
    if sorted(encountered) == VALID_KEYS:
        return True
    else:
        if sorted(encountered) == REQUIRED_KEYS:
            return True
        else:
            return False

if __name__ == "__main__":
    with open("input.txt") as f:
        print(part1(f.read()))
        print(part2(f.read()))
