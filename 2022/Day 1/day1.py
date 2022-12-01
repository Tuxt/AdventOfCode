
FILENAME = 'input'

with open(FILENAME) as f:
    data = f.read()

elves = [[int(e) for e in line.strip().split('\n')] for line in data.split('\n\n')]
max_elves = [sum(elf) for elf in elves]

print('[DAY 1]: Part 1')
print('Total calories carried by the Elf with more calories: {}'.format(max(max_elves)))
