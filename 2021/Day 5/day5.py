import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read()

# Data preparation
data = data.split('\n')[:-1]                                                        # Split lines
data = np.stack(np.char.split(data, sep=' -> '))                                    # Split points
data = np.array([np.stack(e) for e in np.char.split(data, sep=',')]).astype(int)    # Split coords of each point

# Hydrothermal vents map
vents_map = np.zeros(shape=(np.max(data)+1, np.max(data)+1)).astype(int)

# Keep lines if horizontal or vertical (not diag)
is_hv = lambda point: np.any(point[0] == point[1])
hv_data = data[list(map(is_hv, data))]

# Draw lines in the map
def draw_line(vent_map, coords):
    x_min, x_max = np.min(coords[:, 0]), np.max(coords[:, 0])
    y_min, y_max = np.min(coords[:, 1]), np.max(coords[:, 1])
    vent_map[x_min: x_max + 1, y_min: y_max + 1] += 1
[draw_line(vents_map, coords) for coords in hv_data]

print('[DAY 5]: Part 1')
print('Points with at least 2 line overlaps: {}'.format(np.sum(vents_map > 1)))


diag_data = data[np.logical_not(list(map(is_hv, data)))]

def draw_diag(vent_map, coords):
    x_idx = np.arange(coords[0, 0], coords[1, 0] + 1) if coords[0, 0] <= coords[1, 0] else \
            np.arange(coords[0, 0], coords[1, 0] - 1, -1)
    y_idx = np.arange(coords[0, 1], coords[1, 1] + 1) if coords[0, 1] <= coords[1, 1] else \
            np.arange(coords[0, 1], coords[1, 1] - 1, -1)

    vent_map[x_idx, y_idx] += 1

[draw_diag(vents_map, coords) for coords in diag_data]

print('\n[DAY 5]: Part 2')
print('Points with at least 2 line overlaps: {}'.format(np.sum(vents_map > 1)))
