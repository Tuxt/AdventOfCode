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
    visits[node1] = 0
    visits[node2] = 0


def search(node, current_visits, paths_found=0, max_visits=1, max_small_caves=np.inf):
    if node == 'end':
        paths_found += 1
        return paths_found

    current_visits[node] += 1
    for path in paths[node]:
        if path == 'start':
            continue
        if np.sum(np.array([v for k, v in visits.items() if k.islower()]) == max_visits) > max_small_caves:
            break
        if path.isupper() or current_visits[path] < max_visits:
            paths_found = search(path, current_visits, paths_found, max_visits=max_visits, max_small_caves=max_small_caves)
    current_visits[node] -= 1
    return paths_found


paths_found = search('start', visits)

print('[DAY 12]: Part 1')
print('Paths in which the small caves are visited 1 time at most: {}'.format(paths_found))

paths_found = search('start', visits, max_visits=2, max_small_caves=1)
print('\n[DAY 12]: Part 2')
print('Paths in which one small cave are visited 2 times: {}'.format(paths_found))

