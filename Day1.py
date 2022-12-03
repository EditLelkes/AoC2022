def create_list_of_calories(filename: str):
    current_elf_calories = 0
    elf_calorie_list = []
    with open(filename, 'r') as reader:
        for line in reader:
            if line != '\n':
                current_elf_calories += int(line)
            else:
                elf_calorie_list.append(current_elf_calories)
                current_elf_calories = 0
    return sorted(elf_calorie_list, reverse=True)


print(sum(create_list_of_calories('day1.txt')[:3]))
