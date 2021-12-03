import numpy as np
import re

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read().split('\n\n')
    data = np.vectorize( lambda x: x.replace('\n', ' ').strip() )(data).tolist()

passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # + 'cid

valid_passports = sum( [ all([ field in passport for field in passport_fields]) for passport in data ] )

print('[DAY 4]: Part 1')
print('Total valid passports: {}'.format(valid_passports))


def check_year(value, low, high):
    try:
        return (len(value) == 4) and (low <= int(value) <= high)
    except ValueError:
        return False

def check_height(value, units):
    try:
        if units == 'cm':
            return 150 <= int(value) <= 193
        elif units == 'in':
            return 59 <= int(value) <= 76
        else:
            return False
    except ValueError:
        return False

def validate_field(field):
    key, value = field.split(':')
    if key == 'byr':
        return check_year(value, 1920, 2002)
    elif key == 'iyr':
        return check_year(value, 2010, 2020)
    elif key == 'eyr':
        return check_year(value, 2020, 2030)
    elif key == 'hgt':
        return check_height(value[:-2], value[-2:])
    elif key == 'hcl':
        return re.match('^#[0-9a-f]{6}$', value) is not None
    elif key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        return (len(value) == 9) and value.isdecimal()
    elif key == 'cid':
        return True


def valid_passport(passport):
    # Check all required fields
    if not all([ field in passport for field in passport_fields ]):
        return False

    # Validate data
    passport = passport.split()
    return all([ validate_field(field) for field in passport ])


valid_passports = sum( [valid_passport(e) for e in data] )
print('\n[DAY 4]: Part 2')
print('Total valid passports: {}'.format(valid_passports))
