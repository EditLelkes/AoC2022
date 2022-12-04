from typing import List


def get_the_bags(filename: str):
    fully_overlapping_num = 0
    all_overlapping_num = 0
    with open(filename, 'r') as reader:
        for line in reader:
            first_elf = [int(i) for i in line.strip().split(',')[0].split('-')]
            second_elf = [int(i) for i in line.strip().split(',')[1].split('-')]
            fully_overlapping_num += is_fully_overlapping(first_elf, second_elf)
            all_overlapping_num += is_overlapping(first_elf, second_elf)
    return fully_overlapping_num, all_overlapping_num


def is_fully_overlapping(first_elf: List, second_elf: List):
    if first_elf[0] <= second_elf[0] and first_elf[1] >= second_elf[1]:
        return 1
    elif second_elf[0] <= first_elf[0] and second_elf[1] >= first_elf[1]:
        return 1
    return 0


def is_overlapping(first_elf: List, second_elf: List):
    if second_elf[0] <= first_elf[0] <= second_elf[1]:
        return 1
    elif first_elf[0] <= second_elf[0] <= first_elf[1]:
        return 1
    return 0


print(get_the_bags('day4.txt'))
