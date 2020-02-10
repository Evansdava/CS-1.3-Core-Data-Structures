#!python


def linear_search(array, item):
    """Return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    """Best case runtime: O(1) if item is at index 0
    Worst case: O(n) if item is at last index
    """
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    """Best case runtime: O(1) if item is at index 0
    Worst case: O(n) if item is at last index
    """
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if array[index] == item:
        return index
    elif index < len(array) - 1:
        return linear_search_recursive(array, item, index + 1)
    else:
        return None


def binary_search(array, item):
    """Return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    """Best case runtime: O(1) if item is exactly in the middle
    Worst case: O(Log n) if item takes the maximum number
               of iterations to reach
    """
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    index = len(array) // 2
    left, right = None, None
    while array[index] != item:
        if left and right:
            index = (right + left) // 2
        elif left:
            index = (len(array) + left) // 2
        elif right:
            index = right // 2
        elif not (left or right):
            index = len(array) // 2

        if index == left or index == right:
            return None
        elif item < array[index]:
            right = index
        elif item > array[index]:
            left = index
    return index


def binary_search_recursive(array, item, left=None, right=None):
    """Best case runtime: O(1) if item is exactly in the middle
    Worst case: O(Log n) if item takes the maximum number
                of iterations to reach
    """
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    if left and right:
        index = (right + left) // 2
    elif left:
        index = (len(array) + left) // 2
    elif right:
        index = right // 2
    elif not (left or right):
        index = len(array) // 2

    if index == left or index == right:
        return None
    if array[index] == item:
        return index
    elif item < array[index]:
        return binary_search_recursive(array, item, left=left, right=index)
    elif item > array[index]:
        return binary_search_recursive(array, item, left=index, right=right)
