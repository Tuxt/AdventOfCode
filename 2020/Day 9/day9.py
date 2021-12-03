import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = np.array(f.read().split('\n')[:-1], dtype=np.int64)

def check_sequence(data, idx):
    elements = data[idx: idx+25]
    target = data[idx+25]

    sums = np.add.outer(elements, elements)
    coords = np.where(sums == target)[0]

    return len(coords) != 0

idx = 0
while check_sequence(data, idx):
    idx += 1

invalid_number = data[idx+25]
print('[DAY 9]: Part 1')
print('First number without the property: {}'.format( invalid_number ))

# Search contiguous numbers that sums `invalid_number` in a range from `idx`
def search_range(data, range_size, invalid_number):
    window = np.ones(range_size).astype(np.int64)
    convs = np.convolve(data, window)[len(window)-1:-len(window)+1]
    results = np.where(convs == invalid_number)[0]

    if len(results) != 0:
        return results[0]
    return False

for range_size in range(2, len(data)):
    idx = search_range(data, range_size, invalid_number)
    if idx:
        break

sequence = data[idx: idx+range_size]

print('\n[DAY 9]: Part 2')
print('Contiguous set found!')
print('Sequence: {}'.format(sequence))
print('Sum of sequence: {}'.format(sequence.sum()))
print('Max: {}\tMin: {}\tResult: {}'.format(sequence.max(), sequence.min(), sequence.max()+sequence.min()))