input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read().split('\n\n')

# One row per group. Each element is one person
data = [ e.replace('\n', ' ').strip().split() for e in data ]

# Questions answered yes by anyone in the group
answered_yes = [ len( set( ''.join(e) ) ) for e in data ]

print('[DAY 6]: Part 1')
print('Sum of counts: {}'.format( sum(answered_yes) ))

