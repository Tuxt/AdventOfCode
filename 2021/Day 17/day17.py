import numpy as np

input_file = 'input'

with open(input_file, 'r') as f:
    target_x, target_y = [[int(val) for val in coord.split('=')[1].split('..')]for coord in f.read()[:-1].split(', ')]


def simulation_step(probe_x, probe_y, speed_x, speed_y):
    probe_x += speed_x
    probe_y += speed_y
    speed_x = (speed_x - 1 if speed_x > 0 else speed_x + 1) if speed_x != 0 else 0
    speed_y -= 1
    return (probe_x, probe_y), (speed_x, speed_y)


def simulate_throw(start_speed_x, start_speed_y, target_x, target_y):
    probe = (0, 0)
    speed = (start_speed_x, start_speed_y)

    trace = []
    while (probe[0] < target_x[0] or probe[1] > target_y[0]) and (probe[0] < target_x[1] and probe[1] > target_y[1]):
        probe, speed = simulation_step(*probe, *speed)
        trace.append(probe)
    return target_x[0] <= probe[0] <= target_x[1] and target_y[0] <= probe[1] <= target_y[1], trace


# If x is a low value, it will take more steps to reach the target,
# so y will be able to go higher and have time to go down.
# However, too low x values will not reach the target.
# The values that y can take will depend on the steps that x needs
# to reach the target.

# FUNCTIONS TO NARROW THE TARGETS

# Determines min value of X. Max value of X will be the x max limit of the target zone
def get_min_x(min_target_x):
    dec = 0
    while min_target_x > 0:
        min_target_x -= dec
        dec += 1
    return dec - 1


# Get the x steps needed to reach the target zone
def get_x_steps_until_target(x, min_target_x):
    steps = 0
    while min_target_x > 0 and x > 0:
        min_target_x -= x
        x -= 1
        steps += 1
    return steps if x > 0 else np.inf


# For a given y value, the negative values it gets are: -(y+1), -(y+1 + y+2), -(y+1 + y+2 + y+3), ...
# So, the max value that y can take will be target_y[0] + 1
highest_y = 0
min_x = get_min_x(target_x[0])
max_x = target_x[1] + 1
min_y, max_y = 1, abs(target_y[0] + 1) + 1

for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        success, trace = simulate_throw(x, y, target_x, target_y)
        if success:
            highest_y = max([highest_y, np.array(trace)[:, 1].max()])

print('[DAY 17]: Part 1')
print('Highest y value that can be reach: {}'.format(highest_y))

