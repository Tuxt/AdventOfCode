import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read()

data = data.split('\n')[:-1]

data = np.array(data, dtype=int)

increments = np.sum((data[1:] - data[:-1]) > 0)

print('[DAY 1]: Part 1')
print('Number of times a deph measurement increases: {}'.format(increments))


