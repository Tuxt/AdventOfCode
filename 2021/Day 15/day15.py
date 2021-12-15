import numpy as np
import networkx as nx

input_file = 'input'

with open(input_file) as f:
    data = np.array([[int(char) for char in list(line[:-1])] for line in f.readlines()])


G = nx.MultiDiGraph()


def add_edge(G, data, i, j):
    if i > 0:
        G.add_edge('{:02}{:02}'.format(i, j), '{:02}{:02}'.format(i - 1, j), weight=data[i - 1][j])
    if i < len(data) - 1:
        G.add_edge('{:02}{:02}'.format(i, j), '{:02}{:02}'.format(i + 1, j), weight=data[i + 1][j])
    if j > 0:
        G.add_edge('{:02}{:02}'.format(i, j), '{:02}{:02}'.format(i, j - 1), weight=data[i][j - 1])
    if j < len(data) - 1:
        G.add_edge('{:02}{:02}'.format(i, j), '{:02}{:02}'.format(i, j + 1), weight=data[i][j + 1])


[add_edge(G, data, i, j) for i in range(len(data)) for j in range(len(data[i]))]
weight, path = nx.algorithms.shortest_paths.weighted.single_source_dijkstra(G, '0000', '9999')

print('[DAY 15]: Part 1')
print('Total risk of the path: {}'.format(weight))

