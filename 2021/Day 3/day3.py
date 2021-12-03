import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read()

data = data.split('\n')[:-1]
data = [ list(e) for e in data ]
data = np.array(data, dtype=int)

def common_bit(data, type):     # type = 'most' : Most common bit | type = 'least' : Least common bit
    ones = np.sum(data, axis=0) # Count 1's for each column: How many rows have 1's for each column
    num_rows = data.shape[0]    # Count number of rows
    if type == 'most':
        return ((ones/num_rows) >= 0.5).astype(int)
    elif type== 'least':
        return ((ones/num_rows) < 0.5).astype(int)
    else:
        raise ValueError('type must be "most" or "least": got {}'.format(type))

# Calculate gamma (most common bit) and epsilon (least common bit): True = 1, False = 0
gamma = common_bit(data, 'most')
epsilon = common_bit(data, 'least')

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


def filter_data(data, pos, type):   # type = 'most' : For oxygen rating | type = 'least' : For CO2 rating
    current_common_bits = common_bit(data, type)
    filter_bit = current_common_bits[pos]
    filter_data = data[data[:, pos] == filter_bit]
    return filter_data

def get_rating(data, type): # type = 'most' : For oxygen rating | type = 'least' : For CO2 rating
    i = 0
    while len(data) > 1:
        data = filter_data(data, i, type)
        i += 1
    return data

oxygen_generator_rating = bool_to_int( get_rating(data, 'most')[0] )
co2_scrubber_rating = bool_to_int( get_rating(data, 'least')[0] )

print('\n[DAY 3]: Part 2')
print('Oxygen Generator Rating: {} = {}'.format(format(oxygen_generator_rating, '#014b'), oxygen_generator_rating))
print('CO2 Scrubber Rating:     {} = {}'.format(format(co2_scrubber_rating, '#014b'), co2_scrubber_rating))

print('Solution: {} * {} = {}'.format(oxygen_generator_rating, co2_scrubber_rating, oxygen_generator_rating*co2_scrubber_rating))
