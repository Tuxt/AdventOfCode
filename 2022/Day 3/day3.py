import string

FILENAME = 'input'
with open(FILENAME) as f:
    data = f.read().splitlines()

items_in_both_compartments = [set(line[:len(line)//2]).intersection(set(line[len(line)//2:])).pop() for line in data]
priorities = map(lambda x: string.ascii_letters.find(x) + 1, items_in_both_compartments)

print('[DAY 3]: Part 1')
print('Sum of priorities: {}'.format(sum(priorities)))

