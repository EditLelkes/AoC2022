class Directory:
    def __init__(self, parent_dir):
        self.parent_dir = parent_dir
        self.size = 0

    def add_size_to_self_and_all_parents(self, size):
        current_directory = self
        while current_directory is not None:
            current_directory.size += size
            current_directory = current_directory.parent_dir


def get_directories(file_name):
    with open(file_name) as file:
        current_directory = None
        directory_list = []
        for line in file.readlines():
            line = line.strip().split()
            if line[0] == '$' and line[1] == 'cd':
                if line[2] == '..':
                    current_directory = current_directory.parent_dir
                else:
                    current_directory = Directory(current_directory)
                    if current_directory not in directory_list:
                        directory_list.append(current_directory)
            elif line[0] != '$' and line[0] != 'dir':
                current_directory.add_size_to_self_and_all_parents(int(line[0]))

    return sorted([directory.size for directory in directory_list], reverse=True)


sorted_list_of_dir_sizes = get_directories('day7.txt')

print(min([size for size in sorted_list_of_dir_sizes if size >= (30000000 - (70000000 - sorted_list_of_dir_sizes[0]))]))
print(sum([size for size in sorted_list_of_dir_sizes if size <= 100000]))
