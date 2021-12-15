import numpy as np
import networkx as nx

input_file = 'input'

with open(input_file) as f:
    data = np.array([[int(char) for char in list(line[:-1])] for line in f.readlines()])


def add_edge(G, data, i, j):
    if i > 0:
        G.add_edge('{:03}{:03}'.format(i, j), '{:03}{:03}'.format(i - 1, j), weight=data[i - 1][j])
    if i < len(data) - 1:
        G.add_edge('{:03}{:03}'.format(i, j), '{:03}{:03}'.format(i + 1, j), weight=data[i + 1][j])
    if j > 0:
        G.add_edge('{:03}{:03}'.format(i, j), '{:03}{:03}'.format(i, j - 1), weight=data[i][j - 1])
    if j < len(data) - 1:
        G.add_edge('{:03}{:03}'.format(i, j), '{:03}{:03}'.format(i, j + 1), weight=data[i][j + 1])


G = nx.MultiDiGraph()
[add_edge(G, data, i, j) for i in range(len(data)) for j in range(len(data[i]))]
weight, path = nx.algorithms.shortest_paths.weighted.single_source_dijkstra(G, '000000', '099099')

print('[DAY 15]: Part 1')
print('Total risk of the path: {}'.format(weight))


data1 = np.concatenate((data, data+1, data+2, data+3, data+4), axis=0)
data2 = np.concatenate((data+1, data+2, data+3, data+4, data+5), axis=0)
data3 = np.concatenate((data+2, data+3, data+4, data+5, data+6), axis=0)
data4 = np.concatenate((data+3, data+4, data+5, data+6, data+7), axis=0)
data5 = np.concatenate((data+4, data+5, data+6, data+7, data+8), axis=0)
data = np.concatenate((data1, data2, data3, data4, data5), axis=1)

data[data > 9] = data[data > 9] % 10 + 1

G = nx.MultiDiGraph()
[add_edge(G, data, i, j) for i in range(len(data)) for j in range(len(data[i]))]
weight, path = nx.algorithms.shortest_paths.weighted.single_source_dijkstra(G, '000000', '499499')

print('\n[DAY 15]: Part 2')
print('Total risk of the path: {}'.format(weight))
