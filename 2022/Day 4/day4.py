
FILENAME = 'input'

with open(FILENAME) as f:
    data = f.read().splitlines()

data = [
    [
        range(int(e.split('-')[0]), int(e.split('-')[1])+1)
        for e in line.split(',')
    ]
    for line in data
]

ranges_contained_in_other = [ set(pair[0]).issubset(set(pair[1])) or set(pair[1]).issubset(set(pair[0])) for pair in data]

print('[DAY 4]: Part 1')
print('Pairs with ranges fully contained: {}'.format(sum(ranges_contained_in_other)))

