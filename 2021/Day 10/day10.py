import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read().splitlines()

ERROR_SCORE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    None: 0
}


def remove_pairs(line):
    line_length = len(line)
    line = line.replace('{}', '').replace('()', '').replace('[]', '').replace('<>', '')
    if line_length != len(line):
        return remove_pairs(line)
    return line


def find_error(line):
    line = remove_pairs(line)
    line = line.replace('(', '').replace('{', '').replace('[', '').replace('<', '')
    return line[0] if len(line) > 0 else None


error_scores = [ERROR_SCORE[find_error(line)] for line in data]


print('[DAY 10]: Part 1')
print('Total syntax error score: {}'.format(sum(error_scores)))


incomplete = np.array(data)[np.array(error_scores) == 0]

COMPLETION_SCORE = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}


def completion_score(line, score=0):
    *line, current = line
    score = score * 5 + COMPLETION_SCORE[current]
    return score if len(line) == 0 else completion_score(line, score)


completion_scores = [completion_score(remove_pairs(line)) for line in incomplete]

print('\n[DAY 10]: Part 2')
print('Middle score: {}'.format(np.median(completion_scores).astype(np.int64)))
