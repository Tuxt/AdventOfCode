import pandas as pd
import difflib

input_file = 'input'

data = pd.read_csv(input_file, sep='|', header=None).rename({0: 'signal', 1:'output'}, axis=1)
data = data.apply(lambda col: col.str.strip())

signal, output = data['signal'].str.split(' ', expand=True), data['output'].str.split(' ', expand=True)
len2digits = {2: 1, 3: 7, 4: 4, 7: 8}
decoded_output = output.applymap(lambda e: len2digits[len(e)] if len(e) in len2digits.keys() else e)

print('[DAY 8]: Part 1')
print('Times the digits 1, 4, 7 and 8 appear in output: {}'.format(decoded_output.isin(len2digits.values()).sum().sum()))


def decode_5len(item, one, four):
    if sum(map(lambda e: e.startswith(' '), list(difflib.ndiff(one, item)))) == 2:
        return 3
    elif sum(map(lambda e: e.startswith(' '), list(difflib.ndiff(four, item)))) == 2:
        return 2
    else:
        return 5

def decode_6len(item, one, four):
    if sum(map(lambda e: e.startswith(' '), list(difflib.ndiff(four, item)))) == 4:
        return 9
    elif sum(map(lambda e: e.startswith(' '), list(difflib.ndiff(one, item)))) == 2:
        return 0
    else:
        return 6

def decode(signal, output):
    try:
        items_to_decode = output.where(output.str.isalpha()).dropna().apply(sorted)
    except:
        return

    one, _, four, *_ = sorted(signal.apply(sorted), key=len)

    for item in set(items_to_decode.str.join('')):
        if len(item) == 5:
            decoded_item = decode_5len(list(item), one, four)
        elif len(item) == 6:
            decoded_item = decode_6len(list(item), one, four)

        items_to_decode[items_to_decode.str.join('') == item] = decoded_item

        output[items_to_decode.index] = items_to_decode

[ decode(signal.loc[i], decoded_output.loc[i]) for i in range(len(decoded_output)) ]

decoded_output[0] *= 1000
decoded_output[1] *= 100
decoded_output[2] *= 10

print('\n[DAY 8]: Part 2')
print('Sum of all decoded values: {}'.format(decoded_output.sum().sum()))
