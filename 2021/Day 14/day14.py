import numpy as np
from collections import Counter

input_file = 'input'

with open(input_file) as f:
    template = f.readline().strip('\n')
rules = dict(np.genfromtxt(input_file, dtype=str, delimiter=' -> ', usecols=[0, 1], skip_header=1))
FIRST_CHAR = template[0]
LAST_CHAR = template[-1]


def _steps(template, rules, steps=1):
    '''
        Manual generation of steps for the given template and rules
    '''
    template = list(template)
    for _ in range(steps):
        [template.insert(i+1, rules[''.join(template[i:i+2])]) for i in range(len(template)-2, -1, -1)]
    return ''.join(template)


def count_pairs_for_n_steps(n):
    '''
        Take n steps over each possible pair of values. For each pair, it counts the pairs of the generated
        sequence and produces a dictionary with the relation (initial pair) -> (generated pairs).
    '''
    # Generate n steps for each possible pair
    n_steps = {k: _steps(k, rules, n) for k in rules.keys()}
    # Count pairs generated for every pair in n steps
    return {k: Counter(''.join(pair) for pair in np.array([list(v[:-1]), list(v[1:])]).T) for k, v in n_steps.items()}


STEPS = 10
COUNTS = count_pairs_for_n_steps(STEPS)

# Transform template to pairs and count them
template = np.array([list(template[:-1]), list(template[1:])]).T
template_counter = Counter([''.join(pair) for pair in template])


def simulate_steps(current_counter, simulation_counter):
    '''
        For the given 'current_counter', advance the process applying the 'simulation_counter'.
        This is equivalent to run N steps over the 'current_counter'. Where N is the number of
        steps used to produce the 'simulation_counter'.
    '''
    # For each current pair, get the pairs generated after N steps (with simulation_counter)
    pair_counter = Counter()

    for key, value in current_counter.items():
        pair_counter += Counter({k: v * value for k, v in simulation_counter[key].items()})

    return pair_counter


def count_chars(current_counter):
    '''
        Count the number of times each symbol appears in the given counter/diccionary.
    '''
    char_counter = Counter()

    # Sum the number of times a letter appears in each pair
    for k, v in current_counter.items():
        char_counter[k[0]] += v
        char_counter[k[1]] += v

    # Divide the sum of each element by two
    # Since each element appears twice (in the pair with the previous element and with the next one)
    # Except for the first and last elements
    char_counter[FIRST_CHAR] -= 1
    char_counter[LAST_CHAR] -= 1
    char_counter = Counter({k: int(v / 2) for k, v in char_counter.items()})
    char_counter[FIRST_CHAR] += 1
    char_counter[LAST_CHAR] += 1
    return char_counter


template_counter = simulate_steps(template_counter, COUNTS)
chars_10steps = count_chars(template_counter)
most_common, least_common = chars_10steps.most_common(1)[0][1], chars_10steps.most_common()[-1][1]
print('[DAY 14]: Part 1')
print('After {} steps: Most common element ({}) - Least common element ({}) = {}'.format(STEPS,
                                                                                         most_common,
                                                                                         least_common,
                                                                                         most_common-least_common))

STEPS2 = 40     # Total steps for the second part
for _ in range(int((STEPS2 - STEPS) / STEPS)):
    template_counter = simulate_steps(template_counter, COUNTS)
chars_40steps = count_chars(template_counter)
most_common, least_common = chars_40steps.most_common(1)[0][1], chars_40steps.most_common()[-1][1]
print('\n[DAY 14]: Part 2')
print('After {} steps: Most common element ({}) - Least common element ({}) = {}'.format(STEPS2,
                                                                                         most_common,
                                                                                         least_common,
                                                                                         most_common-least_common))
