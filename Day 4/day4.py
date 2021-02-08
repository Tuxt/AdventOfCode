import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read().split('\n\n')
    data = np.vectorize( lambda x: x.replace('\n', ' ').strip() )(data).tolist()

passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # + 'cid

valid_passports = sum( [ all([ field in passport for field in passport_fields]) for passport in data ] )

print('[DAY 4]: Part 1')
print('Total valid passports: {}'.format(valid_passports))

