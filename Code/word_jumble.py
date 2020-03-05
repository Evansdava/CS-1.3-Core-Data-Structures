from itertools import permutations
from binarytree import BinarySearchTree
from random import shuffle


class JumbleSolver():
    """Class for solving word jumbles"""

    def __init__(self, items):
        """Initializes items for solving"""
        self.tree = self.make_word_tree('/usr/share/dict/words')
        self.solutions = [self.solve_word(item) for item in items]

    def __str__(self):
        """Print out the solutions of the given words"""
        result = ""
        for word in self.solutions:
            result += word + "\n"

    def make_word_tree(self, file):
        """Creates a binary search tree of the words in given file"""
        with open(file) as f:
            words = [word.strip() for word in f.readlines()]
            shuffle(words)
            tree = BinarySearchTree(words)
        return tree

    def solve_word(self, word):
        """Solves a single word"""
        solved_list = [''.join(perm).lower() for perm in permutations(word)]
        for solved in solved_list:
            if self.tree.contains(solved):
                return solved


if __name__ == '__main__':
    solver = JumbleSolver(['gyrint', 'drivet', 'snamea',
                           'ceedit', 'sowdah', 'elchek'])
    print(solver.solutions)
