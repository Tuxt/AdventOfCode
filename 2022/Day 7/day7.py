from treelib import Tree

FILENAME = 'input'
with open(FILENAME) as f:
    data = f.read().splitlines()


# Create tree filesystem
def build_tree(data):
    tree = Tree()
    tree.create_node('/', '/', data={'type': 'dir'})    # Root node
    current_dir = []
    for line in data:
        if line.startswith('$'):                        # COMMAND
            if line.endswith('cd ..'):                  # Dir up
                current_dir.pop()
            elif 'cd' in line:                          # Dir down
                _, new_dir = line.split('cd ')
                current_dir.append(new_dir)
        else:                                           # NO COMMAND (ls lines)
            if line.startswith('dir'):                  # dir <dirname>
                _, dirname = line.split()
                tree.create_node(
                    dirname,
                    '/'.join(current_dir + [dirname])[1:],
                    parent='/'.join(current_dir)[1:] if len(current_dir) > 1 else '/',
                    data={'type': 'dir'}
                )
            else:                                       # size <filename>
                size, filename = line.split()
                tree.create_node(
                    filename,
                    '/'.join(current_dir + [filename])[1:],
                    parent='/'.join(current_dir)[1:] if len(current_dir) > 1 else '/',
                    data={'type': 'file', 'size': int(size)}
                )
    return tree


def calc_weight_node(tree, node):
    node.data['size'] = sum([
        child.data.get('size') if child.data.get('size') is not None else calc_weight_node(tree, child)
        for child in tree.children(node.identifier)
    ])
    return node.data['size']


tree = build_tree(data)
calc_weight_node(tree, tree.nodes.get('/'))


print('[DAY 7]: Part 1')
print('Sum of all directories with a size up to 100000: {}'.format(sum([
    node.data['size']
    for node in tree.all_nodes_itr()
    if node.data['type'] == 'dir' and node.data['size'] <= 100_000
])))

