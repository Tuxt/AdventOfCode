FILENAME = 'input'

with open(FILENAME) as f:
    data = f.read().strip()

def find_markers(data, num_chars):
    positions = {i: data[i-num_chars: i] for i in range(num_chars, len(data))}
    start_markers = [k for k, v in positions.items() if len(set(v)) == num_chars]
    return start_markers

print('[DAY 6]: Part 1')
print('First start-of-packet marker: {}'.format(find_markers(data, 4)[0]))

print('\n[DAY 6]: Part 2')
print('First start-of-message marker: {}'.format(find_markers(data, 14)[0]))
