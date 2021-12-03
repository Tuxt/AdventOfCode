import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read()

data = data.split('\n')[:-1]

data = np.array(data, dtype=int)

sums = np.add.outer(data, data)

index = np.where(sums == 2020)[0]
elems = data[index]

print('[DAY 1]: Part 1')
print('Element {}: {}'.format(index[0], elems[0]))
print('Element {}: {}'.format(index[1], elems[1]))

print('{} + {} = {}'.format( elems[0], elems[1], elems[0] + elems[1] ))

print('Solution: {} * {} = {}'.format(elems[0], elems[1], elems[0] * elems[1]))

sums3 = np.add.outer(data, sums)

index3 = np.where(sums3 == 2020)[0]
index3 = np.unique(index3)

elems3 = data[index3]

print('\n[DAY 1]: Part 2')
print('Element {}: {}'.format(index3[0], elems3[0]))
print('Element {}: {}'.format(index3[1], elems3[1]))
print('Element {}: {}'.format(index3[2], elems3[2]))

print('{} + {} + {}= {}'.format( elems3[0], elems3[1], elems3[2], elems3[0] + elems3[1] + elems3[2]))

print('Solution: {} * {} * {}= {}'.format(elems3[0], elems3[1], elems3[2], elems3[0] * elems3[1] * elems3[2]))