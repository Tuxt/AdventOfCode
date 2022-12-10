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

visited_by_tail = {(0, 0): 1}
head = np.array([0, 0])                 # Current coords for head
tail = np.array([0, 0])                 # Current coords for tail


def step(direction):
    global head
    global tail
    # Move head
    head += MOVEMENTS[direction]
    # Move tail
    distance = head - tail
    if np.all(np.abs(distance) < 2):    # Touching: don't move Tail
        return
    else:
        tail = tail + (distance > 0) - (distance < 0)
        visited_by_tail[tuple(tail)] = visited_by_tail.get(tuple(tail), 0) + 1
        return


[step(line.split()[0]) for line in data for _ in range(int(line.split()[1]))]


print('[DAY 9]: Part 1')
print('Positions visited by the tail: {}'.format(len(visited_by_tail)))
