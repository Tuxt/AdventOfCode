import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = np.array(f.read()[:-1].split(',')).astype(int)

def step(data):
    new = np.sum(data==0)
    data -= 1
    data[data < 0] %= 7
    return np.concatenate([data, np.ones(new, dtype=int) * 8])

DAYS = 80

for _ in range(DAYS):
    data = step(data)

print('[DAY 6]: Part 1')
print('There are {} lanternfish after {} days'.format(data.shape[0], DAYS))
