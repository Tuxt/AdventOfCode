import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read()

data = data.split('\n')[:-1]
data = [ list(e) for e in data ]
data = np.array(data, dtype=int)

ones = np.sum(data, axis=0) # Count 1's for each column: How many rows have 1's for each column
num_rows = data.shape[0]    # Count number of rows

# Calculate gamma (most common bit) and epsilon (least common bit): True = 1, False = 0
gamma = ((ones/num_rows) > 0.5).astype(int)
epsilon = ((ones/num_rows) < 0.5).astype(int)

# Transform Bool/Binary array to Integer
def bool_to_int(bool_data):
    data = bool_data.astype(int).astype(str)
    data  = ''.join(data)
    return int(data, 2)

gamma = bool_to_int(gamma)
epsilon = bool_to_int(epsilon)

print('[DAY 3]: Part 1')
print('Gamma:   {} = {}'.format(format(gamma, '#014b'), gamma))
print('Epsilon: {} = {}'.format(format(epsilon, '#014b'), epsilon))

print('Solution: {} * {} = {}'.format(gamma, epsilon, gamma*epsilon))


