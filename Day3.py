from typing import List
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_my_score(filename: str):
    sum_of_priorities = 0
    with open(filename, 'r') as reader:
        for line in reader:
            sum_of_priorities += get_common_element_score(line)
    return sum_of_priorities


def get_common_element_score(line: str):
    half_length = len(line.strip()) // 2
    common_element = list(set(line[:half_length]).intersection(line[half_length:]))[0]
    return letters.index(common_element) + 1


print(get_my_score('day3.txt'))


# PART 2

def get_the_bags(filename: str):
    bags = []
    with open(filename, 'r') as reader:
        for line in reader:
            bags.append(line.strip())
    return bags


def get_badges_score(bags: List):
    sum_of_priorities = 0
    for i in range(0, len(bags), 3):
        common_element = list((set(bags[i]).intersection(bags[i + 1])).intersection(bags[i + 2]))[0]
        sum_of_priorities += letters.index(common_element) + 1
    return sum_of_priorities


print(get_badges_score(get_the_bags('day3.txt')))
