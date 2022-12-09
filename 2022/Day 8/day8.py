import numpy as np

FILENAME = 'input'

data = np.genfromtxt(FILENAME, dtype=int, delimiter=1)

vertical_visibility = np.array([
    np.all(data[i] > data[:i], axis=0) | np.all(data[i] > data[i+1:], axis=0)
    for i in range(data.shape[0])
])
horizontal_visibility = np.array([
    np.all(data[:, i:i+1] > data[:, :i], axis=1) | np.all(data[:, i:i+1] > data[:, i+1:], axis=1)
    for i in range(data.shape[1])
]).T

print('[DAY 8]: Part 1')
print('Visible trees from outside the grid: {}'.format(np.sum(vertical_visibility | horizontal_visibility)))


