def get_start_of_marker(filename: str, number_of_different_characters: int) -> int:
    with open(filename, 'r') as reader:
        for line in reader:
            for i in range(len(line)):
                if len(set(line[i:i + number_of_different_characters])) == number_of_different_characters:
                    return i + number_of_different_characters


print(get_start_of_marker('day6.txt', 4))
print(get_start_of_marker('day6.txt', 14))
