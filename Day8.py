from typing import List
from pathlib import Path


def count_visible_trees(tree_height, list_of_tree_heights):
    count = 0
    for height in list_of_tree_heights:
        count += 1
        if height >= tree_height:
            return count
    return count


class Forest:
    def __init__(self, trees: List[List["Tree"]]):
        self.trees = trees

    @classmethod
    def read_trees_from_line(cls, line: str, is_first_or_last_line: bool) -> List["Tree"]:
        row_of_trees: List[Tree] = []
        for i in range(len(line)):
            tree = Tree(line[i])
            if is_first_or_last_line or i == 0 or i == len(line) - 1:
                tree.is_visible = True
            row_of_trees.append(tree)
        return row_of_trees

    @classmethod
    def read_from_file(cls, file: Path) -> "Forest":
        trees: List[List["Tree"]] = list()
        with file.open("r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                trees.append(cls.read_trees_from_line(lines[i].strip(), i == 0 or i == len(lines) - 1))
        return Forest(trees)

    def get_tree_data(self):
        for i in range(len(self.trees)):
            for j in range(len(self.trees[0])):
                curr_tree = self.trees[i][j]
                horizontal_trees = [tree.height for tree in self.trees[i]]
                left_trees = horizontal_trees[:j][::-1]
                right_trees = horizontal_trees[j + 1:]
                vertical_trees = [row[j].height for row in self.trees]
                up_trees = vertical_trees[:i][::-1]
                down_trees = vertical_trees[i + 1:]
                if left_trees and right_trees and up_trees and down_trees:
                    curr_tree.trees_visible = count_visible_trees(curr_tree.height, up_trees) \
                                              * count_visible_trees(curr_tree.height, down_trees) \
                                              * count_visible_trees(curr_tree.height, left_trees) \
                                              * count_visible_trees(curr_tree.height, right_trees)
                    if curr_tree.height > max(left_trees) or curr_tree.height > max(right_trees) \
                            or curr_tree.height > max(down_trees) or curr_tree.height > max(up_trees):
                        curr_tree.is_visible = True

    def visibility_count(self):
        self.get_tree_data()
        count = 0
        for row in self.trees:
            for tree in row:
                if tree.is_visible:
                    count += 1
        print(count)

    def visible_trees_count(self):
        self.get_tree_data()
        max_visible_trees = 0
        for row in self.trees:
            for tree in row:
                if tree.trees_visible > max_visible_trees:
                    max_visible_trees = tree.trees_visible
        print(max_visible_trees)


class Tree:
    def __init__(self, height):
        self.height = int(height)
        self.is_visible = False
        self.trees_visible = 0


def get_visibilities(file_name):
    forest = Forest.read_from_file(Path(file_name))
    forest.visibility_count()
    forest.visible_trees_count()


get_visibilities('day8.txt')
