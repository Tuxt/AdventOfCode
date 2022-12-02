import pandas as pd

FILENAME = 'input'

data = pd.read_csv(FILENAME, sep=' ', header=None)
data = data.rename(columns={0: 'Elf', 1: 'Me'})

# Outcome points
data['Outcome'] = 0
data.loc[((data.Elf == 'A') & (data.Me == 'Y')) | ((data.Elf == 'B') & (data.Me == 'Z')) | ((data.Elf == 'C') & (data.Me == 'X')), 'Outcome'] = 6
data.loc[((data.Elf == 'A') & (data.Me == 'X')) | ((data.Elf == 'B') & (data.Me == 'Y')) | ((data.Elf == 'C') & (data.Me == 'Z')), 'Outcome'] = 3

# Shape points
data.loc[data.Me == 'X', 'Shape'] = 1
data.loc[data.Me == 'Y', 'Shape'] = 2
data.loc[data.Me == 'Z', 'Shape'] = 3

# Total round points
data['Round'] = data['Outcome'] + data['Shape']

print('[DAY 2]: Part 1')
print('Score according to the strategy guide: {:.0f}'.format(data.sum()['Round']))
