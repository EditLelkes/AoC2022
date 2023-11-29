def day10_1(file_name):
    x, cycle, sum_of_signals = 1, 0, 0
    with open(file_name) as file:
        for line in file:
            for item in line.strip().split():
                cycle += 1
                if cycle == 20 or (cycle - 20) % 40 == 0:
                    sum_of_signals += (cycle * x)
                try:
                    x += int(item)
                except ValueError:
                    pass

    print(sum_of_signals)


def day10_2(file_name):
    x = [0, 1, 2]
    cycle = 0
    with open(file_name) as file:
        for line in file:
            for item in line.strip().split():
                if cycle % 40 == 0:
                    print()
                if cycle % 40 in x:
                    print('#', end=' ')
                else:
                    print('.', end=' ')
                try:
                    x = [pos + int(item) for pos in x]
                except:
                    pass
                cycle += 1


day10_1('day10.txt')
day10_2('day10.txt')
