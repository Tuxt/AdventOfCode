import numpy as np

INPUT_FILE = 'input'
TARGET_SCORE = 1000
ROLLS_PER_TURN = 3
MAX_PLAYERS = 2

with open(INPUT_FILE) as f:
    player1_pos = int(f.readline().split(': ')[1])
    player2_pos = int(f.readline().split(': ')[1])
    pos = np.array([player1_pos - 1, player2_pos - 1])


def deterministic_dice():
    value = 0
    while True:
        yield value + 1
        value = (value + 1) % 100


dice = deterministic_dice()
score = np.array([0, 0])
times_rolled = 0
current_player = 0
remaining_turns = ROLLS_PER_TURN

while np.all(score < TARGET_SCORE):
    times_rolled += 1
    pos[current_player] = (pos[current_player] + next(dice)) % 10
    remaining_turns -= 1
    if remaining_turns == 0:
        score[current_player] += (pos[current_player] + 1)
        remaining_turns = ROLLS_PER_TURN
        current_player = (current_player + 1) % 2

print('[DAY 21]: Part 1')
print('Score of loser ({}) * Times rolled ({}) =  {}'.format(score[current_player], times_rolled, score[current_player]* times_rolled))



