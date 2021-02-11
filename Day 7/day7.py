import networkx as nx
from networkx.algorithms.simple_paths import all_simple_paths

input_file = 'input'
my_bag = 'shiny gold'

with open(input_file, 'r') as f:
    data = f.read().split('\n')[:-1]


G = nx.DiGraph()

for line in data:
    container, content = line.split(' contain ')

    # Container
    container = container[:-5]

    # Content
    for child in content.split(','):
        # Get rid off number
        _, child = child.strip().split(' ', 1)
        # Get rid off bag/bags
        child, _ = child.rsplit(' ', 1)

        G.add_edge(container, child)

roots = [ n for n,d in G.in_degree() if d==0 ]

paths_elements = [ e
                   for root in roots
                   for path in all_simple_paths(G, root, my_bag)
                   for e in path if e != my_bag]
bags = set( paths_elements )

print('[DAY 7]: Part 1')
print('Bags that can contain at least one {}: {}'.format( my_bag, len(bags) ))

