import numpy as np
from functools import cmp_to_key
from copy import deepcopy

FILENAME = 'input'
DIVIDER_PACKETS = [
    [[2]],
    [[6]]
]

with open(FILENAME) as f:
    data = f.read().split('\n\n')
    data = [[eval(line) for line in pair.strip().splitlines()] for pair in data]


def compare_ints(left, right):
    return left < right if left != right else None


def compare_lists(left, right):
    while len(left) > 0 and len(right) > 0:
        left_e, right_e = left.pop(0), right.pop(0)
        cmp = compare(left_e, right_e)
        if cmp is not None:
            return cmp
    if len(left) == 0 and len(right) == 0:
        return None
    return len(left) < len(right)


def compare(left, right):
    if type(left) == int and type(right) == int:
        return compare_ints(left, right)
    elif type(left) == list and type(right) == list:
        return compare_lists(left, right)
    else:
        left = [left] if type(left) == int else left
        right = [right] if type(right) == int else right
        return compare(left, right)


pairs_in_the_right_order = [compare(*pair) for pair in data]

print('[DAY 13]: Part 1')
print('Sum of indices or right pairs: {}'.format((np.argwhere(pairs_in_the_right_order) + 1).sum()))


def comparator(left, right):
    cmp = compare(deepcopy(left), deepcopy(right))
    if cmp is None:
        return 0
    else:
        return -1 if cmp else 1


with open(FILENAME) as f:
    data = f.read().replace('\n\n', '\n').splitlines()
    data = [eval(line) for line in data]

data += DIVIDER_PACKETS

data = sorted(data, key=cmp_to_key(comparator))
divider_idx = [i + 1 for i, e in enumerate(data) if e in DIVIDER_PACKETS]

print('\n[DAY 13]: Part 2')
print('Decoder key: {}'.format(divider_idx[0] * divider_idx[1]))
