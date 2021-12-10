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


def process_line(line):     # Faster than using stack, same as recursive
    line_lenght = len(line)+1
    while len(line) != line_lenght:
        line_lenght = len(line)
        line = line.replace('{}', '').replace('()', '').replace('[]', '').replace('<>', '')
    line = line.replace('(', '').replace('{', '').replace('[', '').replace('<', '')
    return line[0] if len(line) > 0 else None


scores = [ERROR_SCORE[process_line(line)] for line in data]

print('[DAY 10]: Part 1')
print('Total syntax error score: {}'.format(sum(scores)))

