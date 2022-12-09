import numpy as np

FILENAME = 'input'

data = np.genfromtxt(FILENAME, dtype=int, delimiter=1)

vertical_visibility = np.array([
    np.all(data[i] > data[:i], axis=0) | np.all(data[i] > data[i + 1:], axis=0)
    for i in range(data.shape[0])
])
horizontal_visibility = np.array([
    np.all(data[:, i:i + 1] > data[:, :i], axis=1) | np.all(data[:, i:i + 1] > data[:, i + 1:], axis=1)
    for i in range(data.shape[1])
]).T

print('[DAY 8]: Part 1')
print('Visible trees from outside the grid: {}'.format(np.sum(vertical_visibility | horizontal_visibility)))


def scenic_line(value, line):
    if len(line) == 0:  # Edge: No trees to see
        return 0
    stop_position = np.argwhere(value <= line)
    if len(stop_position) == 0:  # No stop: can see all the trees
        return len(line)
    else:
        stop_position = stop_position[0][0]
        return len(line[:stop_position]) + 1


def scenic_score(arr, x, y):
    value = arr[x, y]
    return scenic_line(value, arr[x + 1:, y]) * \
           scenic_line(value, arr[x, y + 1:]) * \
           scenic_line(value, arr[:x, y][::-1]) * \
           scenic_line(value, arr[x, :y][::-1])

scenic_array = np.zeros(data.shape)
for x in range(data.shape[0]):
    for y in range(data.shape[1]):
        scenic_array[x, y] = scenic_score(data, x, y)

print('\n[DAY 8]: Part 2')
print('Highest scenic score: {}'.format(int(np.max(scenic_array))))
