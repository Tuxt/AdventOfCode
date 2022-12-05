import copy

FILENAME = 'input'

with open(FILENAME) as f:
    data = f.read().splitlines()

# Split data
drawing, col_pos, commands = data[:8], data[8], data[10:]
num_columns = int(max(col_pos))

# Transform drawing to stacks
stacks = [list(map(lambda x, i: x[i], drawing, [col_pos.find(str(col))] * num_columns)) for col in range(1, num_columns + 1)]
stacks = [list(''.join(stack).strip()) for stack in stacks]     # Join to strip (spaces), and convert to list again
[stack.reverse() for stack in stacks]                           # Reverse lists: top at the end (inplace operation)
original_stacks = copy.deepcopy(stacks)

# Transform commands: [num_crates, origin, destination]
commands = [[int(val) for val in command.split() if val.isdigit()] for command in commands]

# Perform commands
[[stacks[dest-1].append(stacks[origin-1].pop()) for _ in range(num_crates)] for (num_crates, origin, dest) in commands]

# Get the top (last) element from each stack
top_stacks = list(map(lambda x: x[-1], stacks))

print('[DAY 5]: Part 1')
print('Crates at top: {}'.format(''.join(top_stacks)))

# Restore initial state
stacks = original_stacks

# Perform commands
[[stacks[dest-1].append(stacks[origin-1].pop(-i)) for i in range(num_crates, 0, -1)] for (num_crates, origin, dest) in commands]

# Get the top (last) element from each stack
top_stacks = list(map(lambda x: x[-1], stacks))


print('\n[DAY 5]: Part 2')
print('Crates at top: {}'.format(''.join(top_stacks)))