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


# 3-sided dice + 3 turns: 27 possible combinations, 7 possible values
# Value +3    (x1 combination)
# Value +4    (x3 combination)
# Value +5    (x6 combination)
# Value +6    (x7 combination)
# Value +7    (x6 combination)
# Value +8    (x3 combination)
# Value +9    (x1 combination)
roll_dimension = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}

with open(INPUT_FILE) as f:
    player1_pos = int(f.readline().split(': ')[1])
    player2_pos = int(f.readline().split(': ')[1])
    pos = [player1_pos - 1, player2_pos - 1]

TARGET_DIRAC_SCORE = 21
score = [0, 0]
current_player = 0
won_games = [0, 0]      # Total games won by each player
games = 1               # Games/Dimensions with this rolled values

def dirac_game_turn(pos, score, current_player, won_games, games):
    for roll in roll_dimension.keys():
        new_pos = pos.copy()
        new_pos[current_player] = (new_pos[current_player] + roll) % 10
        new_score = score.copy()
        new_score[current_player] += (new_pos[current_player] + 1)
        new_player = (current_player + 1) % 2
        new_games = games * roll_dimension[roll]
        if new_score[current_player] < TARGET_DIRAC_SCORE:
            dirac_game_turn(new_pos, new_score, new_player, won_games, new_games)
        else:
            won_games[current_player] += new_games


dirac_game_turn(pos, score, current_player, won_games, games)

print('\n[DAY 21]: Part 2')
print('The player who wins in the most universes wins in {} universes'.format(max(won_games)))

