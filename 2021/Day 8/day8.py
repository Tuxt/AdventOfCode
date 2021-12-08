import pandas as pd

input_file = 'input'

data = pd.read_csv(input_file, sep='|', header=None).rename({0: 'signal', 1:'output'}, axis=1)
data = data.apply(lambda col: col.str.strip())

signal, output = data['signal'].str.split(' ', expand=True), data['output'].str.split(' ', expand=True)
len2digits = {2: 1, 3: 7, 4: 4, 7: 8}
decoded_output = output.applymap(lambda e: len2digits[len(e)] if len(e) in len2digits.keys() else e)

print('[DAY 8]: Part 1')
print('Times the digits 1, 4, 7 and 8 appear in output: {}'.format(decoded_output.isin(len2digits.values()).sum().sum()))



