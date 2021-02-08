

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read().split('\n')[:-1]

# Slope
right = 3
down = 1

def count_trees(map, slope):
    right, down = slope

    j = 0
    max_width = len(map[0])
    total_trees = 0
    for i in range(0, len(map), down):
        total_trees += (map[i][j] == '#')
        j = (j + right) % max_width

    return total_trees

print('[DAY 3]: Part 1')
print('Slope: (Right={}, Down={})'.format(right, down))
print('Total trees: {}'.format(count_trees(data, (right,down))))

