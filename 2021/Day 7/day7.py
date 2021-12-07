import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = np.array(f.read()[:-1].split(',')).astype(int)

cost = lambda data, target: np.sum(target - data[data < target]) + np.sum(data[data > target] - target)

best_cost = np.min([cost(data, i) for i in range(data.shape[0])])

print('[DAY 7]: Part 1')
print('Cheapest cost to align: {}'.format(best_cost))

cost = lambda data, target: np.sum([np.sum(np.arange(np.abs(e - target) + 1)) for e in data])

best_cost = np.min([cost(data, i) for i in range(data.shape[0])])

print('\n[DAY 7]: Part 2')
print('Cheapest cost to align: {}'.format(best_cost))
