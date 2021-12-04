import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read()

# Process data
data = data.replace('  ', ' ')
random_numbers, *boards = data.split('\n\n')
random_numbers = np.array(random_numbers.split(','), dtype=int)

split_row = lambda row: row.strip().split(' ')
split_board = lambda board: np.array(list(map(split_row, board.strip().split('\n'))), dtype=int)

boards = np.array([split_board(board) for board in boards])

# BINGO LOGIC
# Masks for marked numbers on each board
board_masks = boards.copy().astype(bool)
board_masks[:, :] = False

# Functions to check bingo and mark numbers on masks
board_has_bingo = lambda mask: np.any(np.all(mask, axis=0)) or np.any(np.all(mask, axis=1))
has_bingo = lambda masks: np.any([board_has_bingo(mask) for mask in masks])
update_masks = lambda boards, masks, number: np.logical_or(masks, boards == number)

# Random numbers processing
current_number = None
while not has_bingo(board_masks):
    current_number, *random_numbers = random_numbers
    board_masks = update_masks(boards, board_masks, current_number)

# Get the winner board
winner_index_mask = [board_has_bingo(mask) for mask in board_masks]
winner_board = boards[winner_index_mask]
winner_mask = board_masks[winner_index_mask]
unmarked_elements = winner_board[np.logical_not(winner_mask)]

print('[DAY 4]: Part 1')
print('Winner Board:\n{}\n'.format(winner_board))
print('Winner Mask:\n{}\n'.format(winner_mask))
print('Unmarked_elements:\n{} = {}'.format(unmarked_elements, np.sum(unmarked_elements)))
print('Last random number called: {}'.format(current_number))
print('Solution: {} * {} = {}'.format(np.sum(unmarked_elements), current_number, np.sum(unmarked_elements)*current_number))



almost_all_has_bingo = lambda masks, remaining: np.sum([board_has_bingo(mask) for mask in masks]) == (len(masks)-remaining)

while not almost_all_has_bingo(board_masks, 1):
    current_number, *random_numbers = random_numbers
    board_masks = update_masks(boards, board_masks, current_number)

# Get the loser board
loser_index_mask = [not board_has_bingo(mask) for mask in board_masks]
# Keep playing until the loser board ends
while not almost_all_has_bingo(board_masks, 0):
    current_number, *random_numbers = random_numbers
    board_masks = update_masks(boards, board_masks, current_number)

loser_board = boards[loser_index_mask]
loser_mask = board_masks[loser_index_mask]
unmarked_elements = loser_board[np.logical_not(loser_mask)]

print('\n\n[DAY 4]: Part 2')
print('Loser Board:\n{}\n'.format(loser_board))
print('Loser Mask:\n{}\n'.format(loser_mask))
print('Unmarked_elements:\n{} = {}'.format(unmarked_elements, np.sum(unmarked_elements)))
print('Last random number called: {}'.format(current_number))
print('Solution: {} * {} = {}'.format(np.sum(unmarked_elements), current_number, np.sum(unmarked_elements)*current_number))