import numpy as np
from collections import Counter

input_file = 'input'

with open(input_file, 'r') as f:
    data = np.array(f.read().split('\n')[:-1], dtype=int)

# By definition, the maximum difference must be 3 since otherwise, they could not all be connected in a row. But...
# Checking differences
data = np.append(data, [0,data.max()+3]) # Add 0 for the charging outlet, max()+3 for the built-in joltage adapter
data.sort()
data_diff = data[1:] - data[:-1]
if data_diff.min() < 1 or data_diff.max() > 3:
    print('⊂(⊙д⊙)つ')
    exit(1)

counter_diff = Counter(data_diff)
diff_1 = counter_diff[1]
diff_3 = counter_diff[3]

print('[DAY 10]: Part 1')
print('1-jolt differences: {}'.format(diff_1))
print('3-jolt differences: {}'.format(diff_3))
print('{} * {} = {}'.format(diff_1, diff_3, diff_1 * diff_3))
