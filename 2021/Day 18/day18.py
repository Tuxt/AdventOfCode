import numpy as np
from binarytree import Node

input_file = 'input'

with open(input_file, 'r') as f:
    data = [eval(num) for num in f.read().splitlines()]


def build_tree(root, data):
    if type(data[0]) == int:
        root.left = Node(data[0])
        root.left.parent = root
    else:
        root.left = Node(0)
        root.left.parent = root
        build_tree(root.left, data[0])
    if type(data[1]) == int:
        root.right = Node(data[1])
        root.right.parent = root
    else:
        root.right = Node(0)
        root.right.parent = root
        build_tree(root.right, data[1])
    return root


def addition(num1, num2):
    if type(num1) is list:
        num1 = build_tree(Node(0), num1)
    if type(num2) is list:
        num2 = build_tree(Node(0), num2)

    root = Node(0)
    root.left = num1
    root.left.parent = root
    root.right = num2
    root.right.parent = root
    return root


def search_left(node):
    if not hasattr(node, 'parent'):     # root element: no left nodes
        return None

    result = node.parent.left
    if result == node:
        return search_left(node.parent)

    while result.right is not None:
        result = result.right
    return result


def search_right(node):
    if not hasattr(node, 'parent'):     # root element: no right nodes
        return None
    result = node.parent.right
    if result == node:
        return search_right(node.parent)

    while result.left is not None:
        result = result.left
    return result


def explode(root):
    if root.height < 5:
        return False
    node = root.levels[-1][0].parent    # Take the parent (the pair) of the first node on last level (must be level 5)
    left = search_left(node)
    right = search_right(node)
    if left is not None:
        left.value += node.left.value
    if right is not None:
        right.value += node.right.value
    node.left = None
    node.right = None
    return True


def get_split_nodes(root):
    return [node for node in root.inorder if node in root.leaves and node.val > 9]


def split(root):
    split_nodes = get_split_nodes(root)
    if len(split_nodes) == 0:
        return False

    node = split_nodes[0]
    node.left = Node(node.value // 2)
    node.left.parent = node
    node.right = Node(int(np.ceil(node.value/2)))
    node.right.parent = node
    node.value = 0
    return True


def reduction(root):
    while explode(root):
        pass
    if split(root):
        reduction(root)
    return root


def add_reduce(num1, num2):
    root = addition(num1, num2)
    return reduction(root)


def magnitude(node):
    if node.left is None and node.right is None:
        return node.value

    return 3 * magnitude(node.left) + 2 * magnitude(node.right)


root = Node(0)
build_tree(root, data[0])

for e in data[1:]:
    root = add_reduce(root, e)

print('[DAY 18]: Part 1')
print('Magnitude of the sum: {}'.format(magnitude(root)))
