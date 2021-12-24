import numpy as np
from itertools import combinations
from collections import Counter
from treelib import Tree, Node

input_file = 'input'

with open(input_file, 'r') as f:
    data = [np.array(list(map(eval, scanner.strip().split('\n')[1:]))) for scanner in f.read().split('\n\n')]

# Scanner 0 as reference +x, +y +z
# Scanners 1 to 30 could be in any orientation:
# +x, +y, +z    -x, -z, -y
# +x, -z, +y    -x, +y, -z
# +x, -y, -z    -x, +z, +y
# +x, +z, -y    -x, -y, +z
#
# +y, +z, +x    -y, -x, -z
# +y, -x, +z    -y, +z, -x
# +y, -z, -x    -y, +x, +z
# +y, +x, -z    -y, -z, +x
#
# +z, +x, +y    -z, -y, -x
# +z, -y, +x    -z, +x, -y
# +z, -x, -y    -z, +y, +x
# +z, +y, -x    -z, -x, +y


# Beacons will be at the same distance, despite the axes are switched
def distance(e1, e2):
    return np.sqrt(np.square(e1 - e2).sum())


def has_12_common_beacons(scanner1, scanner2):
    distances1 = [distance(e1, e2) for e1, e2 in combinations(scanner1, 2)]
    distances2 = [distance(e1, e2) for e1, e2 in combinations(scanner2, 2)]
    distances = distances1 + distances2
    counts = np.array([[k, v] for k, v in Counter(distances).items() if v == 2])
    return len(counts) >= 12


def search_relations(tree=None, root=None):
    if tree is None:
        tree = Tree()
    if root is None:
        root = Node(0)
        tree.add_node(root)
    scanners_to_be_found = [i for i in range(len(data)) if  i not in [n.tag for n in tree.all_nodes()]]

    added = [tree.add_node(Node(scanner), parent=root) for scanner in scanners_to_be_found if has_12_common_beacons(data[root.tag], data[scanner])]

    scanners_to_be_found = [i for i in range(31) if i not in [n.tag for n in tree.all_nodes()]]

    if len(scanners_to_be_found) > 0 and len(added) > 0:
        for leave in tree.leaves():
            tree = search_relations(tree=tree, root=leave)

    return tree


def intersect(e1, e2):
    return np.array(eval(np.intersect1d([str(row) for row in e1.tolist()],
                                     [str(row) for row in e2.tolist()])[0]))


# Remove duplicate coords in a scanner
def del_dups(scanner):
    return np.array([eval(coords) for coords in set([str(row) for row in scanner.tolist()])])


# For the given scanners (scanner1 and scanner2), get beacon1 and beacon2 (beacon identified
# for each scanner) and beacon1_ref and beacon2_ref (the corresponding reference beacon)
# beacon1 and beacon1_ref are the same beacon as beacon2 and beacon2_ref, each one on its scanner
def get_beacons(scanner1, scanner2):
    # Get distances for each pair of beacons and save distances and corresponding pair of beacons
    # that both scanners have in common
    distances1 = {distance(e1, e2): [e1, e2] for e1, e2 in combinations(scanner1, 2)}
    distances2 = {distance(e1, e2): [e1, e2] for e1, e2 in combinations(scanner2, 2)}
    distances = list(distances1.keys()) + list(distances2.keys())
    common_distances = np.array([k for k, v in Counter(distances).items() if v == 2])
    distances1 = {k: v for k, v in distances1.items() if k in common_distances}
    distances2 = {k: v for k, v in distances2.items() if k in common_distances}

    # IDENTIFY A BEACON UNEQUIVOCALLY FOR EACH SCANNER
    # Find the 3 most repeated beacons in scanner1 and get distances between the first one and the other ones
    scanner1_values = np.array([v for v in distances1.values()]).reshape(-1, 3)
    (beacon1, _), (beacon1_ref, _), (other, _) = Counter([str(v) for v in scanner1_values.tolist()]).most_common(3)
    beacon1, beacon1_ref, other = np.array(eval(beacon1)), np.array(eval(beacon1_ref)), np.array(eval(other))

    # Get the distance between that elements and find the coords of that distances in scanner2
    # It's necessary to get 2 distances to find the common element and identify the beacon in scanner2 unequivocally
    dist1 = distance(beacon1, beacon1_ref)
    dist2 = distance(beacon1, other)
    scanner2_dist1 = np.array(distances2[dist1])
    scanner2_dist2 = np.array(distances2[dist2])
    beacon2 = intersect(scanner2_dist1, scanner2_dist2)
    beacon2_ref = scanner2_dist1[scanner2_dist1 != beacon2]

    return beacon1, beacon1_ref, beacon2, beacon2_ref


# Get the coords of scanner2 in the same referece as scanner1 (location and orientation)
def transform_coords(scanner1, scanner2):
    # Get the same beacon for each scanner to compare
    beacon1, beacon1_ref, beacon2, beacon2_ref = get_beacons(scanner1, scanner2)

    # Calc the difference to correct axis
    diff1 = beacon1 - beacon1_ref
    diff2 = beacon2 - beacon2_ref

    # Check how axis change position (no signs)
    axis_permutation = [int(np.argwhere(abs(diff2) == abs(diff1[0])).squeeze()),
                        int(np.argwhere(abs(diff2) == abs(diff1[1])).squeeze()),
                        int(np.argwhere(abs(diff2) == abs(diff1[2])).squeeze())]

    # Correct axis with the previous permutation
    scanner2 = scanner2[:, axis_permutation]
    diff2 = diff2[axis_permutation]
    beacon2 = beacon2[axis_permutation]

    # Correct signs (positive/negative)
    signs = (diff1 - diff2 != 0) * (-1) + (diff1 - diff2 == 0)
    scanner2 *= signs
    diff2 *= signs
    beacon2 *= signs

    # scanner2 orientation is fixed
    # Move coords of scanner2 from scanner2 reference to scanner1 reference
    correction = beacon1 - beacon2
    scanner2 += correction

    return scanner2


# Build the relations tree
def transform_coords_tree(tree):
    for leave in tree.leaves():
        parent = tree.parent(leave.identifier)
        child = leave

        new_child_data = transform_coords(data[parent.tag], data[child.tag])
        data[parent.tag] = del_dups(np.concatenate((data[parent.tag], new_child_data)))
        tree.remove_node(child.identifier)

    if sum([leave.tag for leave in tree.leaves()]) > 0:
        transform_coords_tree(tree)


tree = search_relations()       # Build the relations tree
transform_coords_tree(tree)     # Transform coords of each scanner to the reference (first scanner)

print('[DAY 19]: Part 1')
print('Total number of beacons: {}'.format(data[0].shape[0]))



