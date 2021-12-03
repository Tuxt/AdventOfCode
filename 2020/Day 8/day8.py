from collections import Counter

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read().split('\n')[:-1]

# change = False for normal execution
# change = [int...] idxs already tried to change
# If change is list, execution changes only 1 instruction not changed before
def run_code(data, change = False):
    executed_idx = set()
    idx = 0
    acc = 0
    changed = False # False if no operation have been changed yet | Else, idx operation: check with changed is False!

    while idx not in executed_idx and 0 <= idx < len(data):
        executed_idx.add(idx)
        ins = data[idx]
        ins, inc = ins.split(' ')

        if ins == 'nop':
            if type(change) == list and idx not in change and changed is False:
                changed = idx
                idx += int(inc) # JMP
            else:
                idx += 1
        elif ins == 'acc':
            acc += int(inc)
            idx += 1
        elif ins == 'jmp':
            if type(change) == list and idx not in change and changed is False:
                changed = idx
                idx += 1 # NOP
            else:
                idx += int(inc)

    return idx>=len(data), acc, changed

_, acc, _ = run_code(data)
print('[DAY 8]: Part 1')
print('Accumulator is: {}'.format( acc ))


idx_tried = []
success, acc, last_idx_tried = run_code(data, idx_tried)

while not success:
    idx_tried.append(last_idx_tried)
    success, acc, last_idx_tried = run_code(data, idx_tried)

print('\n[DAY 8]: Part 2')
print('Successful run! Accumulator = {}'.format(acc))



