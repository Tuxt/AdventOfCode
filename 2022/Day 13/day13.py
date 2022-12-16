import numpy as np

FILENAME = 'input'

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
