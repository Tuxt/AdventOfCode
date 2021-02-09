input_file = 'input'

with open(input_file, 'r') as f:
    data = f.read().split('\n')[:-1]

def seat_to_id(seat):
    seat = seat.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    row = int(seat[:7], 2)
    col = int(seat[7:], 2)

    return row * 8 + col

seat_ids = [ seat_to_id(seat) for seat in data ]

print('[DAY 5]: Part 1')
print('Highest seat ID: {}'.format(max(seat_ids)))


