import numpy as np

input_file = 'input'
data = np.genfromtxt(input_file, dtype=int, delimiter=[1]*10)


def step(data, highlighted_items=None, highlights=0):
    if highlighted_items is None:
        data += 1
        highlighted_items = np.zeros(data.shape).astype(bool)
    items_to_highlight = (data > 9) ^ highlighted_items

    if not np.any(items_to_highlight):
        data[data > 9] = 0
        return highlights

    highlights += np.sum(items_to_highlight)

    for x, y in zip(*np.where(items_to_highlight)):
        data[np.max([x-1, 0]):x+2, np.max([y-1, 0]): y+2] += 1

    return step(data, items_to_highlight | highlighted_items, highlights)


STEPS = 100
print('[DAY 11]: Part 1')
print('Flashes in {} steps: {}'.format(STEPS, np.sum([step(data) for _ in range(STEPS)])))

data = np.genfromtxt(input_file, dtype=int, delimiter=[1] * 10)
steps = 0
while step(data) != 100: steps += 1

print('\n[DAY 11]: Part 2')
print('All flashes synchronized in step: {}'.format(steps + 1))
