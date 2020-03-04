from binarytree import BinarySearchTree


class TreeSet(object):
    """Class for sets implemented with binary trees"""

    def __init__(self, items=None):
        """Initialize a new Set"""
        self.tree = BinarySearchTree(items)
        # self.size = self.tree.size

    def __repr__(self):
        """Return a string representation of this set"""
        items = ['({!r})'.format(item) for item in self.tree.items_in_order()]
        return ', '.join(items)

    def __iter__(self):
        """Allow the set to be iterated over (i.e. in for loops)"""
        return iter([value for value in self.tree.items_level_order()])

    @property
    def size(self):
        """Use tree size property"""
        return self.tree.size

    def contains(self, item):
        """Return a boolean indicating whether item is in this set
        Best case time complexity: O(1) if item is in the tree root
        Worst case: O(logn) if item is a leaf
        """
        return self.tree.search(item) is not None

    def add(self, item):
        """Add the item to the set if not present
        Best case time complexity: O(1) if tree is empty
        Worst case: O(n) if tree is poorly balanced
        """
        if not self.contains(item):
            self.tree.insert(item)

    def remove(self, item):
        """Remove element from this set, if present, or else raise KeyError
        Best case time complexity: O(1) if item is in the tree root
        Worst case: O(logn) if item isn't there
        """
        if not self.contains(item):
            raise KeyError("Item not found")
        else:
            self.tree.delete(item)

    def union(self, other_set):
        """Return a new set that is the union of this set and other_set
        Best and worst case time complexity: O(n+m), where n is the size of
        self, and m is the size of other_set, because every item has to
        be accounted for
        """
        new_set = TreeSet(self)
        for item in other_set:
            new_set.add(item)
        return new_set

    def intersection(self, other_set):
        """Return a new set that is the intersection of this and other_set
        Best and worst case time complexity: O(m) where m is the size of
        other_set, because it iterates over the other set.
        """
        new_set = TreeSet()
        for item in other_set:
            if self.contains(item):
                new_set.add(item)
        return new_set

    def difference(self, other_set):
        """Return a new set that is the difference of this set and other_set
        Best and worst case time complexity: O(n + logm) where n is the size of
        self, and m is the size of other_set, because it iterates over self and
        checks if other_set contains the items
        """
        new_set = TreeSet()
        for item in self:
            if not other_set.contains(item):
                new_set.add(item)
        return new_set

    def is_subset(self, other_set):
        """Return a boolean indicating if other_set is a subset of this
        Best case time complexity: O(1) if other_set is larger than self
        Worst case: O(m) where m is the size of other_set, as it has to
        iterate over each element of it
        """
        if other_set.size > self.size:
            return False

        for item in other_set:
            if not self.contains(item):
                return False

        return True


if __name__ == '__main__':
    set_a = TreeSet(['A', 'B', 'C'])
    set_b = TreeSet(['C', 'D', 'E'])
    print(set_a.union(set_b))
    print(set_a.intersection(set_b))
    print(set_a.difference(set_b))
    print(set_a.is_subset(set_b))
    assert repr(set_a.union(set_b)) == "('A'), ('B'), ('C'), ('D'), ('E')"
