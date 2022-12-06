def get_containers(file_name):
    with open(file_name) as file:
        containers = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
        for line in file.readlines():
            l = line.strip().replace("    ", "-").replace('[', '').replace(']', '').replace(' ', '')
            if l == '123456789':
                return containers
            else:
                for i in range(len(l)):
                    if l[i] != '-':
                        containers[i + 1] += l[i]


def get_moves(file_name):
    with open(file_name) as file:
        moves = []
        for line in file.readlines():
            l = line.strip().split()
            if 'move' in l:
                moves.append([int(l[1]), int(l[3]), int(l[5])])
        return moves


def get_first_containers(containers):
    for container in containers.values():
        print(container[0], end='')
    print()


def machine9000(containers, moves):
    for move in moves:
        for i in range(move[0]):
            box = containers[move[1]][0]
            containers[move[1]] = containers[move[1]][1:]
            containers[move[2]] = box + containers[move[2]]
    get_first_containers(containers)


def machine9001(containers, moves):
    for move in moves:
        box = ''
        for i in range(move[0]):
            box += containers[move[1]][0]
            containers[move[1]] = containers[move[1]][1:]
        containers[move[2]] = box + containers[move[2]]
    get_first_containers(containers)


machine9000(get_containers('input.txt'), get_moves('input.txt'))
machine9001(get_containers('input.txt'), get_moves('input.txt'))
