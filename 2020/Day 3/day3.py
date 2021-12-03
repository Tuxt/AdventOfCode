import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read().split('\n')[:-1]

# Slope
right = 3
down = 1

def count_trees(map, slope):
    right, down = slope
    max_width = len(map[0])

    lines = np.arange(len(data), step=down)
    rows = np.arange(len(data)*right, step=right)

    return sum( [ data[i][j%max_width] == '#' for i,j in zip(lines, rows) ] )

print('[DAY 3]: Part 1')
print('Slope: (Right={}, Down={})'.format(right, down))
print('Total trees: {}'.format(count_trees(data, (right,down))))


slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

results = [ count_trees(data, slope) for slope in slopes ]

print('\n[DAY 3]: Part 2')
for (right, down), result in zip(slopes, results):
    print('Slope: (Right={}, Down={}) -> Trees: {:>4}'.format(right, down, result))
print('Product result: {}'.format(np.prod(results, dtype=np.int64)))
