import numpy as np

FILENAME = 'input'
MOVEMENTS = {
    'U':  [ 0, +1],
    'D':  [ 0, -1],
    'L':  [-1,  0],
    'R':  [+1,  0]
}

with open(FILENAME) as f:
    data = f.read().splitlines()

# Initial state: 2 knots
visited_by_tail = {(0, 0): 1}
total_knots = 2
knots = [np.array([0, 0]) for _ in range(total_knots)]


def step(direction):
    global knots
    # Move head
    knots[0] += MOVEMENTS[direction]
    # Move next knots
    for i in range(1, len(knots)):
        distance = knots[i-1] - knots[i]
        if np.all(np.abs(distance) < 2):    # Touching: don't move Tail
            continue
        else:
            knots[i] = knots[i] + (distance > 0) - (distance < 0)
            continue
    visited_by_tail[tuple(knots[-1])] = visited_by_tail.get(tuple(knots[-1]), 0) + 1


[step(line.split()[0]) for line in data for _ in range(int(line.split()[1]))]


print('[DAY 9]: Part 1')
print('Positions visited by the tail: {}'.format(len(visited_by_tail)))

# Initial state: 10 knots
visited_by_tail = {(0, 0): 1}
total_knots = 10
knots = [np.array([0, 0]) for _ in range(total_knots)]

[step(line.split()[0]) for line in data for _ in range(int(line.split()[1]))]

print('\n[DAY 9]: Part 2')
print('Positions visited by the tail: {}'.format(len(visited_by_tail)))
