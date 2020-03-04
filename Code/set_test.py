import unittest
from set import TreeSet


class TreeSetTest(unittest.TestCase):
    """Tests for Sets implemented with Binary Search Tree"""

    def test_init(self):
        """Test initialization"""
        # Empty tree
        tree_set = TreeSet()
        assert tree_set.size == 0
        assert tree_set.tree.root is None

        # 5 integers
        tree_set = TreeSet([1, 2, 3, 4, 5])
        assert repr(tree_set) == "(1), (2), (3), (4), (5)"
        assert tree_set.tree.root.data == 1
        assert tree_set.tree.root.right.data == 2
        assert tree_set.tree.root.right.right.data == 3
        assert tree_set.size == 5

        # 5 strings
        tree_set = TreeSet(['C', 'B', 'A', 'E', 'D'])
        assert repr(tree_set) == "('A'), ('B'), ('C'), ('D'), ('E')"
        assert tree_set.tree.root.data == 'C'
        assert tree_set.tree.root.right.data == 'E'
        assert tree_set.tree.root.left.data == 'B'
        assert tree_set.size == 5

    def test_contains(self):
        """Test contains method"""
        # Item in set
        tree_set = TreeSet([1, 2, 3, 4, 5])
        # First item in set
        assert tree_set.contains(1)
        # Last item in set
        assert tree_set.contains(5)
        # Item not in set
        assert not tree_set.contains(7)

    def test_add(self):
        """Test add method"""
        tree_set = TreeSet()
        tree_set.add('C')
        assert tree_set.contains('C')
        assert tree_set.tree.root.data == 'C'
        tree_set.add('B')
        assert tree_set.contains('B')
        assert tree_set.tree.root.left.data == 'B'
        tree_set.add('E')
        assert tree_set.contains('E')
        assert tree_set.tree.root.right.data == 'E'
        tree_set.add('D')
        assert tree_set.contains('D')
        assert tree_set.tree.root.right.left.data == 'D'
        tree_set.add('A')
        assert tree_set.contains('A')
        assert tree_set.tree.root.left.left.data == 'A'

    def test_remove(self):
        """Test remove method"""
        tree_set = TreeSet(['C', 'B', 'A', 'E', 'D'])
        assert tree_set.size == 5
        assert tree_set.contains('E')
        tree_set.remove('E')
        assert not tree_set.contains('E')
        assert tree_set.tree.root.data == 'C'
        assert tree_set.tree.root.right.data == 'D'
        assert tree_set.tree.root.left.data == 'B'
        assert tree_set.size == 4
        assert tree_set.contains('B')
        tree_set.remove('B')
        assert not tree_set.contains('B')
        assert tree_set.tree.root.data == 'C'
        assert tree_set.tree.root.right.data == 'D'
        assert tree_set.tree.root.left.data == 'A'
        assert tree_set.size == 3
        assert tree_set.contains('C')
        tree_set.remove('C')
        assert not tree_set.contains('C')
        assert tree_set.tree.root.data == 'D'
        assert tree_set.tree.root.right is None
        assert tree_set.tree.root.left.data == 'A'
        assert tree_set.size == 2
        assert tree_set.contains('D')
        tree_set.remove('D')
        assert not tree_set.contains('D')
        assert tree_set.tree.root.data == 'A'
        assert tree_set.tree.root.right is None
        assert tree_set.tree.root.left is None
        assert tree_set.size == 1
        assert tree_set.contains('A')
        tree_set.remove('A')
        assert not tree_set.contains('A')
        assert tree_set.tree.root is None
        assert tree_set.size == 0
        try:
            tree_set.remove('F')
            assert False
        except KeyError:
            assert True

    def test_union(self):
        """Testing the union method"""
        set_one = TreeSet(['C', 'B', 'A', 'E', 'D'])
        set_two = TreeSet(['G', 'F', 'E', 'I', 'H'])
        union = set_one.union(set_two)
        assert repr(union) == "('A'), ('B'), ('C'), ('D'), ('E'), \
('F'), ('G'), ('H'), ('I')"
        assert union.contains('A')
        assert union.contains('C')
        assert union.contains('E')
        assert union.contains('G')
        assert union.contains('I')
        assert union.size == 9

    def test_intersection(self):
        """Testing the intersection method"""
        set_one = TreeSet(['C', 'B', 'A', 'E', 'D'])
        set_two = TreeSet(['G', 'F', 'E', 'I', 'H'])
        intersection = set_one.intersection(set_two)
        assert not intersection.contains('A')
        assert not intersection.contains('C')
        assert intersection.contains('E')
        assert not intersection.contains('G')
        assert not intersection.contains('I')
        assert intersection.size == 1

    def test_difference(self):
        """Testing the difference method"""
        set_one = TreeSet(['C', 'B', 'A', 'E', 'D'])
        set_two = TreeSet(['G', 'F', 'E', 'I', 'H'])
        difference = set_one.difference(set_two)
        assert repr(difference) == "('A'), ('B'), ('C'), ('D')"
        assert difference.contains('A')
        assert difference.contains('C')
        assert not difference.contains('E')
        assert not difference.contains('G')
        assert not difference.contains('I')
        assert difference.size == 4

    def test_is_subset(self):
        """Testing the is_subset method"""
        set_one = TreeSet(['C', 'B', 'A', 'E', 'D'])
        set_two = TreeSet(['A', 'B', 'C', 'I', 'H'])
        set_three = TreeSet(['A', 'B', 'C'])
        assert not set_one.is_subset(set_two)
        assert not set_two.is_subset(set_one)
        assert set_one.is_subset(set_three)
        assert set_two.is_subset(set_three)
        assert not set_three.is_subset(set_one)
        assert not set_three.is_subset(set_two)
