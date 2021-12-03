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
        num, child = child.strip().split(' ', 1)
        # Get rid off bag/bags
        child, _ = child.rsplit(' ', 1)

        try:
            G.add_edge(container, child, weight=int(num))
        except ValueError:
            # No bags inside
            pass

roots = [ n for n,d in G.in_degree() if d==0 ]

paths_elements = [ e
                   for root in roots
                   for path in all_simple_paths(G, root, my_bag)
                   for e in path if e != my_bag]
bags = set( paths_elements )

print('[DAY 7]: Part 1')
print('Bags that can contain at least one {}: {}'.format( my_bag, len(bags) ))


def count_bag(G, bag):
    contained_bags = 0
    for edge in G.edges(bag):
        contained_bags += count_edge(G, edge)
    return contained_bags

def count_edge(G, edge):
    weight = int(G.edges[edge]['weight'])
    return weight + weight * count_bag(G, edge[1])

total_bags_inside = count_bag(G, my_bag)

print('\n[DAY 7]: Part 2')
print('Total bags contained in {}: {}'.format(my_bag, total_bags_inside))