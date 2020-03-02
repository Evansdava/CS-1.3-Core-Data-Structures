from binarytree import BinarySearchTree


class TreeSet(object):
    """Class for sets implemented with binary trees"""

    def __init__(self, items=None):
        """Initialize a new Set"""
        self.tree = BinarySearchTree(items)
        self.size = self.tree.size

    def __repr__(self):
        """Return a string representation of this set"""
        items = ['({!r})'.format(item) for item in self.tree.items_in_order()]
        return ', '.join(items)

    def contains(self, item):
        """Return a boolean indicating whether item is in this set"""
        return self.tree.search(item) is not None

    def add(self, item):
        """Add the item to the set if not present"""
        if not self.contains(item):
            self.tree.insert(item)

    def remove(self, item):
        """Remove element from this set, if present, or else raise KeyError"""
        if not self.contains(item):
            raise KeyError("Item not found")
        else:
            self.tree.delete(item)

    def union(self, other_set):
        """Return a new set that is the union of this set and other_set"""
        new_set = TreeSet(self.tree.items_level_order())
        for item in other_set.tree.items_in_order():
            new_set.add(item)
        return new_set

    def intersection(self, other_set):
        """Return a new set that is the intersection of this and other_set"""
        new_set = TreeSet()
        for item in other_set.tree.items_in_order():
            if self.contains(item):
                new_set.add(item)
        return new_set

    def difference(self, other_set):
        """Return a new set that is the difference of this set and other_set"""
        new_set = TreeSet()
        for item in other_set.tree.items_in_order():
            if not self.contains(item):
                new_set.add(item)
        return new_set

    def is_subset(self, other_set):
        """Return a boolean indicating if other_set is a subset of this"""
        for item in other_set.tree.items_in_order():
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
