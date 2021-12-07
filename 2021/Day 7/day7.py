import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = np.array(f.read()[:-1].split(',')).astype(int)

cost = lambda data, target: np.sum(target - data[data < target]) + np.sum(data[data > target] - target)

best_cost = np.min([cost(data, i) for i in range(data.shape[0])])

print('[DAY 7]: Part 1')
print('Cheapest cost to align: {}'.format(best_cost))

