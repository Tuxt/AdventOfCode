FILENAME = 'input'

with open(FILENAME) as f:
    data = f.read().split('\n\n')


class Monkey:

    @classmethod
    def build_monkey(cls, monkeys, monkey):
        monkey = monkey.strip().splitlines()
        items = [int(item.strip()) for item in monkey[1].strip().split(': ')[1].split(',')]
        operation = lambda old: eval(monkey[2].split(' = ')[1]) // 3
        test = lambda e: int(monkey[4].split()[-1]) if e % int(monkey[3].split()[-1]) == 0 else int(monkey[5].split()[-1])
        return Monkey(monkeys, items, operation, test)

    def __init__(self, monkeys, items, operation, test):
        self.monkeys = monkeys
        self.items = items
        self.operation = operation
        self.test = test
        self.inspected_items = 0

    def _inspect_item(self):
        self.items[0] = self.operation(self.items[0])
        self.inspected_items += 1

    def _throw_item(self):
        destination = self.test(self.items[0])
        self.monkeys[destination].items.append(self.items.pop(0))

    def process_item(self):
        self._inspect_item()
        self._throw_item()

    def process_all_items(self):
        while len(self.items) > 0:
            self.process_item()


# Instance monkeys
monkeys = []
[monkeys.append(Monkey.build_monkey(monkeys, monkey)) for monkey in data]

# Run 20 rounds
[monkey.process_all_items() for _ in range(20) for monkey in monkeys]

# Get the inspected items for each monkey (sorted)
inspected_items = sorted(map(lambda e: e.inspected_items, monkeys), reverse=True)

print('[DAY 11]: Part 1')
print('Monkey business: {}'.format(inspected_items[0] * inspected_items[1]))
