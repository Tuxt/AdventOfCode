import numpy as np
from scipy import ndimage
import cv2

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read().splitlines()

data = np.array([list(e) for e in data]).astype(int)

# is_low = lambda arr: np.min(arr[1]) == arr[1, 1] and np.min(arr[:, 1]) == arr[1, 1]
is_low = lambda arr: np.min(arr[[1, 3, 4, 5, 7]]) == arr[4] != np.min(arr[[1, 3, 5, 7]])

low_values_mask = ndimage.generic_filter(data, is_low, size=(3, 3), mode='constant', cval=10).astype(bool)

print('[DAY 9]: Part 1')
print('Sum of the risk levels of all low points: {}'.format(np.sum(data[low_values_mask]+1)))

low_coords_x, low_coords_y = low_values_mask.nonzero()
limits = (data == 9).astype(int)

basin_size = lambda arr, x, y: cv2.floodFill(arr, None, (y, x), 2)[0]
basin_sizes = [basin_size(limits, x, y) for x, y in zip(low_coords_x, low_coords_y)]

print('\n[DAY 9]: Part 2')
print('Multiply together the sizes of the three largest basins: {}'.format(np.prod(sorted(basin_sizes)[-3:])))
