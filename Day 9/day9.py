import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read().split('\n')[:-1]

def check_sequence(data, idx):
    elements = np.array(data[idx: idx+25], dtype=np.int64)
    target = int(data[idx+25])

    sums = np.add.outer(elements, elements)
    coords = np.where(sums == target)[0]

    return len(coords) != 0

idx = 0
while check_sequence(data, idx):
    idx += 1

print('[DAY 9]: Part 1')
print('First number without the property: {}'.format( data[idx+25] ))