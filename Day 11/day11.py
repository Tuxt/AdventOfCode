import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = np.array(f.read().split('\n')[:-1])
    data = np.array( [ list(line) for line in data ] )



def step(data, x, y):
    point = data[x,y]
    around = data[max(x-1, 0): x+2, max(y-1, 0): y+2]

    # No seat
    if point == '.':
        return '.'

    # All empty: Occupy the seat
    if not np.any(around == '#'):
        return '#'

    # 4 occupied around the chair: seat becomes empty
    if point == '#' and np.sum(around == '#') > 4:
        return 'L'

    return point



new_data = np.array( [ [ step(data, i, j) for j in range(data.shape[1]) ] for i in range(data.shape[0]) ] )

while not np.all(new_data == data):
    data = new_data
    new_data = np.array( [ [ step(data, i, j) for j in range(data.shape[1]) ] for i in range(data.shape[0]) ] )

print('[DAY 11]: Part 1')
print('Occupied seats: {}'.format( np.sum(data == '#') ))




