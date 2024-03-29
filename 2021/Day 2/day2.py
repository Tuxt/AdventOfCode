input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read()

data = data.split('\n')[:-1]

horizontal_pos = 0
depth = 0

def process_line(e):
    global horizontal_pos
    global depth

    if e.startswith('forward'):
        horizontal_pos += int(e[8:])
    elif e.startswith('up'):
        depth -= int(e[3:])
    elif e.startswith('down'):
        depth += int(e[5:])

[process_line(e) for e in data]

print('[DAY 2]: Part 1')
print('Horizontal position: {}'.format(horizontal_pos))
print('Depth: {}'.format(depth))

print('Solution: {} * {} = {}'.format(horizontal_pos, depth, horizontal_pos*depth))


horizontal_pos = 0
depth = 0
aim = 0

def process_line(e):
    global horizontal_pos
    global depth
    global aim

    if e.startswith('forward'):
        value = int(e[8:])
        horizontal_pos += value
        depth += (value * aim)
    elif e.startswith('up'):
        aim -= int(e[3:])
    elif e.startswith('down'):
        aim += int(e[5:])

[process_line(e) for e in data]

print('\n[DAY 2]: Part 2')
print('Horizontal position: {}'.format(horizontal_pos))
print('Depth: {}'.format(depth))

print('Solution: {} * {} = {}'.format(horizontal_pos, depth, horizontal_pos*depth))