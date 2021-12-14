import numpy as np
from collections import Counter

input_file = 'input'

with open(input_file) as f:
    template = f.readline().strip('\n')
rules = dict(np.genfromtxt(input_file, dtype=str, delimiter=' -> ', usecols=[0, 1], skip_header=1))


def step(template, rules):
    template = list(template)
    [template.insert(i+1, rules[''.join(template[i:i+2])]) for i in range(len(template)-2, -1, -1)]
    return ''.join(template)


STEPS = 10
for _ in range(STEPS):
    template = step(template, rules)

c = Counter(template)
most_common, least_common = c.most_common(1)[0][1], c.most_common()[-1][1]
print('[DAY 14]: Part 1')
print('After {} steps: Most common element ({}) - Least common element ({}) = {}'.format(STEPS,
                                                                                         most_common,
                                                                                         least_common,
                                                                                         most_common-least_common))




