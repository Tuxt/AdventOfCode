import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read()

data = data.split('\n')[:-1]

data = np.array(data, dtype=int)

increments = np.sum((data[1:] - data[:-1]) > 0)

print('[DAY 1]: Part 1')
print('Number of times a deph measurement increases: {}'.format(increments))


sliding_windows = np.lib.stride_tricks.sliding_window_view(data, 3)

sum_windows = np.sum(sliding_windows, axis=1)

increments = np.sum((sum_windows[1:] - sum_windows[:-1]) > 0)

print('[DAY 1]: Part 2')
print('Number of times the sum of measurements in this sliding window increases: {}'.format(increments))
