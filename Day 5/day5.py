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


seat_ids = sorted(seat_ids)
min_id = min(seat_ids)

high_idx = len(seat_ids)
low_idx = 0

found = False
while not found:
    mid_idx = low_idx + (high_idx - low_idx)//2

    if (high_idx - low_idx) < 2:
        found = True

    if seat_ids[mid_idx] == mid_idx + min_id:
        low_idx = mid_idx
    else:
        high_idx = mid_idx

current_id = int(seat_ids[mid_idx])
above_id = int(seat_ids[mid_idx + 1])

found_id = current_id + 1 if (above_id - current_id) == 2 else current_id - 1

print('\n[DAY 5]: Part 2')
print('My seat ID: {}'.format(found_id))
