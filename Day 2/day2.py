from collections import Counter
import re

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read()

data = data.split('\n')[:-1]

data = [ e.split(': ') for e in data ]

def check_password1(policy, password):
    # FORMAT: "low-high char"
    policy, char = policy.split(' ')
    low, high  = policy.split('-')
    low, high = int(low), int(high)

    return low <= Counter(password)[char] <= high

result1 = sum([ check_password1(e[0], e[1]) for e in data ])

print('[DAY 2]: Part 1')
print('Total valid passwords: {}'.format(result1))



def check_password2(policy, password):
    # FORMAT: "low-high char"
    policy, char = policy.split(' ')
    pos1, pos2 = policy.split('-')
    pos1, pos2 = int(pos1), int(pos2)

    occurrences = [ match.start()+1 for match in re.finditer(char, password) ]

    return (pos1 in occurrences) ^ (pos2 in occurrences)

result2 = sum([ check_password2(e[0], e[1]) for e in data ])

print('[DAY 2]: Part 2')
print('Total valid passwords: {}'.format(result2))

