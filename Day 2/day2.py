from collections import Counter

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read()

data = data.split('\n')[:-1]

data = [ e.split(': ') for e in data ]

def check_password(policy, password):
    # FORMAT: "low-high char"
    policy, char = policy.split(' ')
    low, high  = policy.split('-')
    low, high = int(low), int(high)

    return low <= Counter(password)[char] <= high

result1 = sum([ check_password(e[0], e[1]) for e in data ])

print('[DAY 2]: Part 1')
print('Total valid passwords: {}'.format( result1 ))


