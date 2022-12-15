import networkx as nx
import numpy as np

FILENAME = 'input'

with open(FILENAME) as f:
    data = [list(line) for line in f.read().splitlines()]
    data = np.array(data)

DIM_i, DIM_j = data.shape
G = nx.MultiDiGraph()

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


start = np.argwhere(data == 'S')[0]
end = np.argwhere(data == 'E')[0]

[add_edges(data, G, i, j) for i in range(DIM_i) for j in range(DIM_j)]
path = nx.shortest_path(G, '{}-{}'.format(*start), '{}-{}'.format(*end))

print('[DAY 12]: Part 1')
print('Steps required: {}'.format(len(path) - 1))
