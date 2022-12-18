import numpy as np

FILENAME = 'input'
ORIGIN = [500, 0]


class SandSimulation:
    def __init__(self, rock_lines, sand_source, floor=False):
        self.sand_source = sand_source
        self.sand_position = self.sand_source[:]

        max_x = max([pair[0] for line in rock_lines for pair in line])
        max_y = max([pair[1] for line in rock_lines for pair in line])

        # Create layout with rock blocks (1s, 0s = air)
        self.layout = np.zeros((max_x + 1, max_y + 1)) if not floor else np.zeros((self.sand_source[0] + max_y + 3, max_y + 3))
        for line in data:
            for i in range(1, len(line)):
                origin, dest = line[i-1], line[i]
                self.layout[min(origin[0], dest[0]): max(origin[0], dest[0]) + 1, min(origin[1], dest[1]): max(origin[1], dest[1]) + 1] = 1
        if floor:
            self.layout[:, max_y + 2] = 1

    def sand(self):
        self.sand_position = self.sand_source[:]
        return self._simulate()

    # Simulation of sand: Return True if ends (sand stop at some point) | False if not (sand flows indefinitely)
    def _simulate(self):
        x, y = self.sand_position

        # Check if the current position already has something
        if self.layout[x, y] > 0:
            return False

        if y + 1 == self.layout.shape[1]:
            return False

        if self.layout[x, y + 1] == 0:                                          # Goes down
            self.sand_position = [x, y + 1]
            return self._simulate()
        elif x - 1 > 0 and self.layout[x - 1, y + 1] == 0:                      # Goes down-left
            self.sand_position = [x - 1, y + 1]
            return self._simulate()
        elif x + 1 < self.layout.shape[0] and self.layout[x + 1, y + 1] == 0:   # Goes down-right
            self.sand_position = [x + 1, y + 1]
            return self._simulate()
        elif x - 1 == 0 or x + 1 == self.layout.shape[0]:                       # Goes out of the layout
            return False
        else:                                                                   # Sand stop flowing
            self.layout[self.sand_position[0], self.sand_position[1]] = 2
            return True


if __name__ == '__main__':
    with open(FILENAME) as f:
        data = f.read().splitlines()
        data = [[list(map(int, pair.split(','))) for pair in line.split(' -> ')] for line in data]

    simulation = SandSimulation(data, ORIGIN)
    while simulation.sand():
        continue

    print('[DAY 14]: Part 1')
    print('Number of units of sand: {}'.format(np.sum(simulation.layout == 2)))

    simulation = SandSimulation(data, ORIGIN, floor=True)
    while simulation.sand():
        continue

    print('\n[DAY 14]: Part 2')
    print('Number of units of sand: {}'.format(np.sum(simulation.layout == 2)))
