from collections import Counter

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read().split('\n')[:-1]

executed_idx = set()

idx = 0
acc = 0

while idx not in executed_idx:
    executed_idx.add(idx)
    ins = data[idx]
    ins, inc = ins.split(' ')

    if ins == 'nop':
        idx += 1
    elif ins == 'acc':
        acc += int(inc)
        idx += 1
    elif ins == 'jmp':
        idx += int(inc)

print('[DAY 8]: Part 1')
print('Accumulator is: {}'.format( acc ))



