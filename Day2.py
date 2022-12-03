def get_my_score(filename: str):
    my_score = 0
    with open(filename, 'r') as reader:
        for line in reader:
            choices = line.split(' ')
            my_score += rps_game(choices[0], choices[1].strip())

    return my_score


def rps_game(elf_choice: str, my_choice: str):
    elf_choice = decode_choice(elf_choice)
    my_choice = decode_my_choice(elf_choice, my_choice)
    if elf_choice == my_choice:
        return 3 + get_selection_score(my_choice)
    elif (my_choice == 'R' and elf_choice == 'S') or \
            (my_choice == 'P' and elf_choice == 'R') or \
            (my_choice == 'S' and elf_choice == 'P'):
        return 6 + get_selection_score(my_choice)
    else:
        return get_selection_score(my_choice)


def get_selection_score(choice: str):
    if choice == 'R':
        return 1
    elif choice == 'P':
        return 2
    elif choice == 'S':
        return 3


def decode_choice(choice: str):
    if choice == 'A' or choice == 'X':
        return 'R'
    elif choice == 'B' or choice == 'Y':
        return 'P'
    elif choice == 'C' or choice == 'Z':
        return 'S'


def decode_my_choice(elf_choice: str, is_win: str):
    if is_win == 'Y':
        return elf_choice
    if elf_choice == 'R':
        if is_win == 'X':
            return 'S'
        else:
            return 'P'
    if elf_choice == 'P':
        if is_win == 'X':
            return 'R'
        else:
            return 'S'
    if elf_choice == 'S':
        if is_win == 'X':
            return 'P'
        else:
            return 'R'


print(get_my_score('day2.txt'))
