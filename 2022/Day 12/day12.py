import networkx as nx
import numpy as np

FILENAME = 'input'

with open(FILENAME) as f:
    data = [list(line) for line in f.read().splitlines()]
    data = np.array(data)

DIM_i, DIM_j = data.shape

def calc_elevation(char_1, char_2):
    char_1 = 'a' if char_1 == 'S' else char_1
    char_2 = 'a' if char_2 == 'S' else char_2
    char_1 = 'z' if char_1 == 'E' else char_1
    char_2 = 'z' if char_2 == 'E' else char_2
    return ord(char_2) - ord(char_1)


def add_edges(data, G, i, j):
    if i > 0 and calc_elevation(data[i, j], data[i - 1, j]) <= 1:
            G.add_edge('{}-{}'.format(i, j), '{}-{}'.format(i - 1, j))
    if j > 0 and calc_elevation(data[i, j], data[i, j - 1]) <= 1:
        G.add_edge('{}-{}'.format(i, j), '{}-{}'.format(i, j - 1))
    if i < DIM_i - 1 and calc_elevation(data[i, j], data[i + 1, j]) <= 1:
        G.add_edge('{}-{}'.format(i, j), '{}-{}'.format(i + 1, j))
    if j < DIM_j - 1 and calc_elevation(data[i, j], data[i, j + 1]) <= 1:
        G.add_edge('{}-{}'.format(i, j), '{}-{}'.format(i, j + 1))


def calc_path(G, start, end):
    try:
        path = nx.shortest_path(G, '{}-{}'.format(*start), '{}-{}'.format(*end))
        return path
    except nx.exception.NetworkXNoPath:
        return None


G = nx.MultiDiGraph()
[add_edges(data, G, i, j) for i in range(DIM_i) for j in range(DIM_j)]

start = np.argwhere(data == 'S')[0]
end = np.argwhere(data == 'E')[0]
path = calc_path(G, start, end)

print('[DAY 12]: Part 1')
print('Steps required: {}'.format(len(path) - 1))

steps = [calc_path(G, start, end) for start in np.argwhere(data == 'a')]

print('\n[DAY 12]: Part 2')
print('Steps required: {}'.format(min([len(step) - 1 for step in steps if step is not None])))

