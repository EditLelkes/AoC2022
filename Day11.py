class Monkey:
    def __init__(self, name):
        self.name = name
        self.operation = ''
        self.operation_nr = 0
        self.test_division_nr = 0
        self.passing_test_monkey_to_throw = 0
        self.failing_test_monkey_to_throw = 0
        self.nr_of_inspected_items = 0

    def get_through_items(self, items, worry_reduction, lcm):
        for item in items[self.name]:
            self.nr_of_inspected_items += 1
            item = self.worry_level_operation(item)
            if worry_reduction:
                item = item // 3
            item = item % lcm
            if item % self.test_division_nr == 0:
                items[self.passing_test_monkey_to_throw].append(item)
            else:
                items[self.failing_test_monkey_to_throw].append(item)
        items[self.name] = []

    def worry_level_operation(self, item):
        if self.operation == '*':
            return item * self.operation_nr
        elif self.operation == '+':
            return item + self.operation_nr
        elif self.operation == '**':
            return item * item


def create_monkeys(file_name):
    monkeys = {}
    items = {}
    lowest_common_multiple = 1
    with open(file_name) as file:
        for line in file:
            line = line.strip().split()
            if 'Monkey' in line:
                curr_monkey = line[1][0]
                monkeys[curr_monkey] = Monkey(line[1][0])
                items[curr_monkey] = []
            elif 'Starting' in line:
                items[curr_monkey] = [int(i) for i in ''.join(line[2:]).split(',')]
            elif 'Operation:' in line:
                if line[5] == 'old':
                    monkeys[curr_monkey].operation = '**'
                else:
                    monkeys[curr_monkey].operation = line[4]
                    monkeys[curr_monkey].operation_nr = int(line[5])
            elif 'Test:' in line:
                monkeys[curr_monkey].test_division_nr = int(line[3])
                lowest_common_multiple *= int(line[3])
            elif 'true:' in line:
                monkeys[curr_monkey].passing_test_monkey_to_throw = line[5]
            elif 'false:' in line:
                monkeys[curr_monkey].failing_test_monkey_to_throw = line[5]
    return monkeys, items, lowest_common_multiple


def get_monkey_business(filename, is_worry_reduction, rounds):
    monkeys, items, lcm = create_monkeys(filename)
    for i in range(rounds):
        for monkey in monkeys.values():
            monkey.get_through_items(items, is_worry_reduction, lcm)
    item_manipulations = sorted([monkey.nr_of_inspected_items for monkey in monkeys.values()], reverse=True)
    print(item_manipulations[0] * item_manipulations[1])


get_monkey_business('day11.txt', True, 20)
get_monkey_business('day11.txt', False, 10000)
