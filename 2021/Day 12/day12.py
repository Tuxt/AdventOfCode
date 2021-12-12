import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read().splitlines()

paths = {}
visits = {}

for edge in data:
    node1, node2 = edge.split('-')
    paths[node1] = paths.get(node1, []) + [node2]
    paths[node2] = paths.get(node2, []) + [node1]
    visits[node1] = 1 if node1.islower() else np.inf
    visits[node2] = 1 if node2.islower() else np.inf
visits['end'] = np.inf  # End cave is stopped in a particular case


def search(node, current_visits, current_path=[], paths_found=[]):
    current_path.append(node)
    if node == 'end':
        paths_found.append(current_path.copy())
        return

    current_visits[node] -= 1
    for path in paths[node]:
        if current_visits[path] > 0:
            search(path, current_visits, current_path, paths_found)
    current_visits[node] += 1
    return paths_found


paths_found = search('start', visits)

print('[DAY 12]: Part 1')
print('Paths in which the small caves are visited 1 time at most: {}'.format(len(paths_found)))


