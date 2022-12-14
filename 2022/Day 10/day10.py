import os

FILENAME = 'input'


class Program:

    cycle = 0
    signal = [None]     # None for cycle 0
    register = 1        # Register X

    def __init__(self, program):
        if type(program) is str and os.path.isfile(program):
            with open(FILENAME) as f:
                self.instructions = f.read().splitlines()
        elif type(program) is list:
            self.instructions = program
        else:
            raise ValueError('Must be a list of instructions or filename')

    def reset(self):
        self.cycle = 0
        self.signal = [None]
        self.register = 1

    def _log_signal(self):
        self.signal.append(self.cycle * self.register)

    def _noop(self):
        self.cycle += 1
        self._log_signal()

    def _addx(self, inc):
        self._noop()            # Cycle 1/2 => Log signal strength
        self._noop()            # Cycle 2/2 => Log signal strength
        self.register += inc    # Increment after second cycle is finished

    def run_instruction(self, instruction):
        if instruction == 'noop':
            self._noop()
        elif instruction.startswith('addx'):
            inc = int(instruction.split()[1])
            self._addx(inc)

    def run(self):
        for instruction in self.instructions:
            self.run_instruction(instruction)


program = Program(FILENAME)
program.run()

print('[DAY 10]: Part 1')
print('Sum of the 6 signal strengths: {}'.format(sum([program.signal[i] for i in [20, 60, 100, 140, 180, 220]])))
