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


def clean_vector(vector):
    return vector[vector != '.']

def step(data, x, y):
    point = data[x,y]

    # No seat
    if point == '.':
        return '.'


    around = []
    # Horizontal line
    around += clean_vector( data[x, :y] )[-1:].tolist()                                         # Left
    around += clean_vector( data[x, y+1:] )[0:1].tolist()                                       # Right

    # Vertical line
    around += clean_vector( data[:x, y] )[-1:].tolist()                                         # Up
    around += clean_vector( data[x:, y] )[1:2].tolist()                                         # Down

    # Main diag
    diag_index = y-x
    diag = np.diag(data, diag_index)
    around += clean_vector( diag[:min(x,y)] )[-1:].tolist()                                     # Left-Up
    around += clean_vector( diag[min(x,y):] )[1:2].tolist()                                  # Right-Down

    # Secondary diag
    diag_index = data.shape[1] - (x+y) - 1
    diag = np.diag(np.fliplr(data),  diag_index)
    around += clean_vector( diag[:min(data.shape[1] - 1 - y, x)] )[-1:].tolist()               # Right-Up
    around += clean_vector( diag[min(data.shape[1] - 1 - y, x):] )[1:2].tolist()              # Left-Down

    around = np.array(around)

    # All empty: Occupy the seat
    if not np.any(around == '#'):
        return '#'

    # 4 occupied around the chair: seat becomes empty
    if point == '#' and np.sum(around == '#') > 4:
        return 'L'

    return point

# Restore data
with open(input_file, 'r') as f:
    data = np.array(f.read().split('\n')[:-1])
    data = np.array( [ list(line) for line in data ] )


new_data = np.array( [ [ step(data, i, j) for j in range(data.shape[1]) ] for i in range(data.shape[0]) ] )

while not np.all(new_data == data):
    data = new_data
    new_data = np.array( [ [ step(data, i, j) for j in range(data.shape[1]) ] for i in range(data.shape[0]) ] )


print('\n[DAY 11]: Part 2')
print('Occupied seats: {}'.format( np.sum(data == '#') ))