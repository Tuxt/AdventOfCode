import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read()

data = data.split('\n')[:-1]

data = np.array(data, dtype=int)

sums = np.add.outer(data, data)

index = np.where(sums == 2020)[0]
elems = data[index]

print('Element {}: {}'.format(index[0], elems[0]))
print('Element {}: {}'.format(index[1], elems[1]))

print('{} + {} = {}'.format( elems[0], elems[1], elems[0] + elems[1] ))

print('Solution: {} * {} = {}'.format(elems[0], elems[1], elems[0] * elems[1]))
