class SnakePart:
    def __init__(self):
        self.visited_positions = [[0, 0]]
        self.coord = [0, 0]

    def move_head(self, instruction):
        if instruction == 'U':
            self.coord[0] += 1
        elif instruction == 'D':
            self.coord[0] -= 1
        elif instruction == 'L':
            self.coord[1] -= 1
        elif instruction == 'R':
            self.coord[1] += 1

    def move_tail(self, head_coord):
        horizontal = head_coord[1] - self.coord[1]
        vertical = head_coord[0] - self.coord[0]
        if (abs(horizontal) > 0 and abs(vertical) > 1) or (abs(horizontal) > 1 and abs(vertical) > 0):
            self.coord[1] += horizontal // abs(horizontal)
            self.coord[0] += vertical // abs(vertical)
        elif abs(horizontal) > 1:
            self.coord[1] += horizontal // abs(horizontal)
        elif abs(vertical) > 1:
            self.coord[0] += vertical // abs(vertical)

    def add_position_to_visited(self):
        if [self.coord[0], self.coord[1]] not in self.visited_positions:
            self.visited_positions.append([self.coord[0], self.coord[1]])


class Snake:
    def __init__(self, number_of_parts):
        self.number_of_parts = number_of_parts
        self.body = number_of_parts * [SnakePart()]

    def move(self, instructions):
        for j in range(int(instructions[1])):
            self.body[0].move_head(instructions[0])
            for i in range(1, self.number_of_parts):
                self.body[i].move_tail(self.body[i - 1].coord)
                if i == self.number_of_parts - 1:
                    self.body[i].add_position_to_visited()

    def print_num_of_positions_for_last_part(self):
        print(len(self.body[self.number_of_parts - 1].visited_positions))

    def move_snake_with_instructions(self, file_name):
        with open(file_name) as file:
            for line in file:
                self.move(line.strip().split())


SNAKE_LENGTH = 10
INSTRUCTIONS_FILEPATH = 'day9.txt'

snake = Snake(SNAKE_LENGTH)
snake.move_snake_with_instructions(INSTRUCTIONS_FILEPATH)
snake.print_num_of_positions_for_last_part()
