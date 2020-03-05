from itertools import permutations
from binarytree import BinarySearchTree
from random import shuffle
from utility import time_it


class JumbleSolver():
    """Class for solving word jumbles"""

    @time_it
    def __init__(self, items):
        """Initializes items for solving"""
        self.tree = self.make_word_tree('/usr/share/dict/words')
        self.solutions = [self.solve_word(item) for item in items]

    def __str__(self):
        """Print out the solutions of the given words"""
        result = ""
        for words in self.solutions:
            for word in words:
                result += word + " "
            result += "\n"
        return result

    @time_it
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
        results = []
        for solved in solved_list:
            if self.tree.contains(solved) and solved not in results:
                results.append(solved)
        return tuple(results)

    @time_it
    def new_words(self, words):
        """Replace the set of scrambled words and solve them"""
        self.solutions = [self.solve_word(word) for word in words]


if __name__ == '__main__':
    solver = JumbleSolver(['gyrint', 'drivet', 'snamea',
                           'ceedit', 'sowdah', 'elchek'])
    print(solver.solutions)
    print(solver)
    solver.new_words(['mbipl', 'hoves', 'funsie', 'nioide'])
    print(solver.solutions)
    print(solver)
    solver.new_words(['shast', 'doore', 'ditnic', 'catili'])
    print(solver.solutions)
    print(solver)
    solver.new_words(['banic', 'ogame', 'tanedt', 'tadrsn'])
    print(solver.solutions)
    print(solver)
    solver.new_words(['pryat', 'sogeo', 'rothex', 'areeta'])
    print(solver.solutions)
    print(solver)
