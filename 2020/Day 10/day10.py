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


# Get the out grades for each node (possible connections for each adapter)
grades = []
for i in range(len(data)):
    chunk = data[i + 1:i + 4]
    diffs = chunk - data[i]
    grades.append( (diffs <= 3).sum() )

# Group sequences of grades greater than 1:
# - Join grades as string and split on '1' elements: [3,2,1,1,1,3,1,1,2,2,1,3,1,0] -> [3,2] [3] [2,2] [3]
# - Sum groups: [3,2] [3] [2,2] [3] -> [5, 3, 4, 3]
branches = []
grades = ' '.join( list( map(str, grades) ) )

for group in grades.split('1'):
    group = group.strip()
    if group == '' or group == '0':
        continue
    branches.append(sum(list(map(int, group.split(' ')))))

# Decrease 1 on multiple branches in a row (3,3...; 2,2..; 3,3,2...), not isolated branches (1,2,1...; 1,3,1...)
# [3,2] [3] [2,2] [3] -> [5, 3, 4, 3] -> [4, 3, 3, 3]
branches = np.array(branches, dtype=np.int64)
branches -= (branches > 3)
result = branches.prod()

print('\n[DAY 10]: Part 2')
print('Total arranges: {}'.format(result))