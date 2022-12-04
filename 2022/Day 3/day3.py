import string

FILENAME = 'input'
with open(FILENAME) as f:
    data = f.read().splitlines()

items_in_both_compartments = [set(line[:len(line)//2]).intersection(set(line[len(line)//2:])).pop() for line in data]
priorities = map(lambda x: string.ascii_letters.find(x) + 1, items_in_both_compartments)

print('[DAY 3]: Part 1')
print('Sum of priorities: {}'.format(sum(priorities)))


iter_group = iter(data)
group_badges = [set(a).intersection(set(b)).intersection(set(c)).pop() for a, b, c in zip(*[iter_group]*3)]
badges_priorities = map(lambda x: string.ascii_letters.find(x) + 1, group_badges)

print('\n[DAY 3]: Part 2')
print('Sum of badges priorities: {}'.format(sum(badges_priorities)))