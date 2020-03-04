from itertools import permutations
from binarytree import BinarySearchTree


class JumbleSolver():
    """Class for solving word jumbles"""

    def __init__(self, items):
        """Initializes items for solving"""
        self.tree = self.make_word_tree('/usr/share/dict/words')

    def make_word_tree(self, file):
        """Creates a binary search tree of the words in given file"""
        with open(file) as f:
            words = f.readlines()
            tree = BinarySearchTree(words)
        return tree

    def solve_word(self, word):
        """Solves a single word"""
        solved_list = permutations(word)
        for solved in solved_list:
            if self.tree.contains(solved):
                return solved
