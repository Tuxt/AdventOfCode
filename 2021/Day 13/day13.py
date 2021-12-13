import pandas as pd
import numpy as np

input_file = 'input'

data = pd.read_csv(input_file, header=None)
dots, folds = data[data[1].notna()].to_numpy(dtype=int), data[data[1].isna()].pop(0)
folds = np.array(folds.str.replace('fold along ', '').str.split('=').tolist())


def build_paper(coords):
    paper = np.zeros(np.max(coords, axis=0) + 1, dtype=bool)
    for x, y in coords:
        paper[x, y] += 1
    return paper


paper = build_paper(dots)


def fold_paper(paper, line):
    axis, index = line[0], int(line[1])

    if axis == 'y':
        paper = paper.T

    first, second = paper[:index], paper[index+1:]
    second = np.flipud(second)

    first[first.shape[0]-second.shape[0]:] = first[first.shape[0]-second.shape[0]:] + second

    return first.T if axis == 'y' else first


first_fold, *folds = folds
paper = fold_paper(paper, first_fold)

print('[DAY 13]: Part 1')
print('Visible dots after completing the first fold: {}'.format(np.sum(paper)))


