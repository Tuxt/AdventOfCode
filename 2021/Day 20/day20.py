import numpy as np

input_file = 'input'

current_padding_value = '0'

with open(input_file) as f:
    algorithm, img = f.read().replace('.', '0').replace('#', '1').split('\n\n')
    algorithm = np.array(list(algorithm))
    img = np.array([list(row) for row in img.strip().split('\n')])


def apply_algo_pix(img, i, j, algorithm, target_img):
    target_img[i, j] = algorithm[int(''.join(img[i-1:i+2, j-1:j+2].flatten()), 2)]


def step(img, algorithm):
    global current_padding_value

    # Add padding to the img
    if current_padding_value == '0':
        padded_img = np.zeros((img.shape[0] + 4, img.shape[1] + 4), dtype=int).astype(str)
    elif current_padding_value == '1':
        padded_img = np.ones((img.shape[0] + 4, img.shape[1] + 4), dtype=int).astype(str)
    padded_img[2:-2, 2:-2] = img

    # Create a target img and apply the algorithm
    target_img = padded_img.copy()
    [apply_algo_pix(padded_img, i, j, algorithm, target_img) for i in range(1, padded_img.shape[0] - 1) for j in range(1, padded_img.shape[1] - 1)]

    # Update padding value
    current_padding_value = algorithm[int(current_padding_value * 9, 2)]
    # Update borders of target_img, which have not been processed
    target_img[[0, -1]] = current_padding_value
    target_img[:, [0, -1]] = current_padding_value

    return target_img


STEPS1 = 2
for _ in range(STEPS1):
    img = step(img, algorithm)

print('[DAY 20]: Part 1')
print('Lit pixels after {} steps: {}'.format(STEPS1, np.sum(img == '1')))

STEPS2 = 50
for _ in range(STEPS2-STEPS1):
    img = step(img, algorithm)

print('\n[DAY 20]: Part 2')
print('Lit pixels after {} steps: {}'.format(STEPS2, np.sum(img == '1')))
