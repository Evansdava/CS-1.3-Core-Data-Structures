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

    def test_init_5_integers(self):
        """Test init with 5 integer items"""
        tree_set = TreeSet([1, 2, 3, 4, 5])
        assert repr(tree_set) == "(1), (2), (3), (4), (5)"
        assert tree_set.tree.root.data == 1
        assert tree_set.tree.root.right.data == 2
        assert tree_set.tree.root.right.right.data == 3
        assert tree_set.size == 5

    def test_init_5_strings(self):
        """Test init with 5 strings"""
        tree_set = TreeSet(['C', 'B', 'A', 'E', 'D'])
        assert repr(tree_set) == "('A'), ('B'), ('C'), ('D'), ('E')"
        assert tree_set.tree.root.data == 'C'
        assert tree_set.tree.root.right.data == 'E'
        assert tree_set.tree.root.left.data == 'B'
        assert tree_set.size == 5

    def test_init_mixed(self):
        """Test init with mixed types"""
        try:
            TreeSet(['C', 4, 'A', 5, 'E'])
            assert False
        except TypeError:
            assert True

    def test_contains_item_in_set(self):
        """Test contains method with items in the set"""
        tree_set = TreeSet([1, 2, 3, 4, 5])
        assert tree_set.contains(1)
        assert tree_set.contains(2)
        assert tree_set.contains(3)
        assert tree_set.contains(4)
        assert tree_set.contains(5)

    def test_contains_item_not_in_set(self):
        """Test contains with items outside of set"""
        tree_set = TreeSet([1, 2, 3, 4, 5])
        assert not tree_set.contains('A')
        assert not tree_set.contains(30)
        assert not tree_set.contains('T')
        assert not tree_set.contains(0)
        assert not tree_set.contains(7)

    def test_contains_with_ten_items(self):
        """Test contains with 10 items"""
        tree_set = TreeSet([5, 3, 2, 1, 4, 7, 6, 8, 9, 0])
        for num in range(10):
            assert tree_set.contains(num)

    def test_add_strings(self):
        """Test add method with strings"""
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

    def test_add_ints(self):
        """Test add method with ints"""
        tree_set = TreeSet()
        tree_set.add(5)
        assert tree_set.contains(5)
        assert tree_set.tree.root.data == 5
        tree_set.add(3)
        assert tree_set.contains(3)
        assert tree_set.tree.root.left.data == 3
        tree_set.add(7)
        assert tree_set.contains(7)
        assert tree_set.tree.root.right.data == 7
        tree_set.add(6)
        assert tree_set.contains(6)
        assert tree_set.tree.root.right.left.data == 6
        tree_set.add(1)
        assert tree_set.contains(1)
        assert tree_set.tree.root.left.left.data == 1

    def test_add_tuples(self):
        """Test add method with tuples"""
        tree_set = TreeSet()
        tree_set.add(('E', 5))
        assert tree_set.contains(('E', 5))
        assert tree_set.tree.root.data == ('E', 5)
        tree_set.add(('C', 3))
        assert tree_set.contains(('C', 3))
        assert tree_set.tree.root.left.data == ('C', 3)
        tree_set.add(('G', 7))
        assert tree_set.contains(('G', 7))
        assert tree_set.tree.root.right.data == ('G', 7)
        tree_set.add(('F', 6))
        assert tree_set.contains(('F', 6))
        assert tree_set.tree.root.right.left.data == ('F', 6)
        tree_set.add(('A', 1))
        assert tree_set.contains(('A', 1))
        assert tree_set.tree.root.left.left.data == ('A', 1)

    def test_remove_strings(self):
        """Test remove method with strings"""
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

    def test_remove_ints(self):
        """Test remove method with ints"""
        tree_set = TreeSet([3, 2, 1, 5, 4])
        assert tree_set.size == 5
        assert tree_set.contains(5)
        tree_set.remove(5)
        assert not tree_set.contains(5)
        assert tree_set.tree.root.data == 3
        assert tree_set.tree.root.right.data == 4
        assert tree_set.tree.root.left.data == 2
        assert tree_set.size == 4
        assert tree_set.contains(2)
        tree_set.remove(2)
        assert not tree_set.contains(2)
        assert tree_set.tree.root.data == 3
        assert tree_set.tree.root.right.data == 4
        assert tree_set.tree.root.left.data == 1
        assert tree_set.size == 3
        assert tree_set.contains(3)
        tree_set.remove(3)
        assert not tree_set.contains(3)
        assert tree_set.tree.root.data == 4
        assert tree_set.tree.root.right is None
        assert tree_set.tree.root.left.data == 1
        assert tree_set.size == 2
        assert tree_set.contains(4)
        tree_set.remove(4)
        assert not tree_set.contains(4)
        assert tree_set.tree.root.data == 1
        assert tree_set.tree.root.right is None
        assert tree_set.tree.root.left is None
        assert tree_set.size == 1
        assert tree_set.contains(1)
        tree_set.remove(1)
        assert not tree_set.contains(1)
        assert tree_set.tree.root is None
        assert tree_set.size == 0

    def test_remove_tuples(self):
        """Test remove method with tuples"""
        tree_set = TreeSet([('C', 3), ('B', 2), ('A', 1), ('E', 5), ('D', 4)])
        assert tree_set.size == 5
        assert tree_set.contains(('E', 5))
        tree_set.remove(('E', 5))
        assert not tree_set.contains(('E', 5))
        assert tree_set.tree.root.data == ('C', 3)
        assert tree_set.tree.root.right.data == ('D', 4)
        assert tree_set.tree.root.left.data == ('B', 2)
        assert tree_set.size == 4
        assert tree_set.contains(('B', 2))
        tree_set.remove(('B', 2))
        assert not tree_set.contains(('B', 2))
        assert tree_set.tree.root.data == ('C', 3)
        assert tree_set.tree.root.right.data == ('D', 4)
        assert tree_set.tree.root.left.data == ('A', 1)
        assert tree_set.size == 3
        assert tree_set.contains(('C', 3))
        tree_set.remove(('C', 3))
        assert not tree_set.contains(('C', 3))
        assert tree_set.tree.root.data == ('D', 4)
        assert tree_set.tree.root.right is None
        assert tree_set.tree.root.left.data == ('A', 1)
        assert tree_set.size == 2
        assert tree_set.contains(('D', 4))
        tree_set.remove(('D', 4))
        assert not tree_set.contains(('D', 4))
        assert tree_set.tree.root.data == ('A', 1)
        assert tree_set.tree.root.right is None
        assert tree_set.tree.root.left is None
        assert tree_set.size == 1
        assert tree_set.contains(('A', 1))
        tree_set.remove(('A', 1))
        assert not tree_set.contains(('A', 1))
        assert tree_set.tree.root is None
        assert tree_set.size == 0

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
