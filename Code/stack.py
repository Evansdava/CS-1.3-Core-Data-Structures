#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        if self.list.length() == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) prepending to a LL is constant
        """
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty.
        """
        if self.list.head is None:
            return None
        return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) deleting from the head of a LL is constant
        """
        if self.is_empty():
            raise ValueError("Stack is empty")
        data = self.list.head.data
        self.list.delete(self.peek())
        return data


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        if len(self.list) == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) appending to a list is constant
        """
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty.
        """
        if not self.is_empty():
            return self.list[-1]
        return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) popping from the end of a list is constant
        """
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.list.pop(-1)


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
