from collections import Counter

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read().split('\n\n')

# One row per group. Each element is one person
data = [ e.replace('\n', ' ').strip().split() for e in data ]

# Questions answered yes by anyone in the group
answered_yes = [ len( set( ''.join(e) ) ) for e in data ]

print('[DAY 6]: Part 1')
print('Sum of counts: {}'.format( sum(answered_yes) ))


# Questions answered yes by everyone in the group

# For every group (e in data), count answers for every question and get how many
# was answered by all the group members (v == len(e))
counters = [ sum([ v == len(e) for v in Counter(''.join(e)).values() ])  for e in data ]

print('\n[DAY 6]: Part 2')
print('Sum of counts: {}'.format( sum(counters) ))



