FILENAME = 'input'

with open(FILENAME) as f:
    data = f.read().strip()

quads_pos = {i: data[i-4: i] for i in range(4, len(data))}
start_markers = [k for k, v in quads_pos.items() if len(set(v)) == 4]

print('[DAY 6]: Part 1')
print('First start marker: {}'.format(start_markers[0]))

