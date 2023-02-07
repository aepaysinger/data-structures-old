# _for private methods


class MinHeap:
    def __init__(self, max_num_elements, values=None):
        self.storage = []
        self.max_num_elements = max_num_elements
        if values:
            for value in values:
                self.storage.append(value)
            self.size = len(self.storage)
            self._heapify_up()

    def _find_parent_index(self, index):
        return (index - 1) // 2

    def _find_left_child_index(self, index):
        return (2 * index) + 1

    def _find_right_child_index(self, index):
        return (2 * index) + 2

    def _has_parent(self, index):
        return self._find_parent_index(index) >= 0

    def _has_left_child(self, index):
        return self._find_left_child_index(index) < len(self.storage)

    def _has_right_child(self, index):
        return self._find_right_child_index(index) < len(self.storage)

    def _parent_location(self, index):
        if index == 0:
            raise ValueError("Root Element")
        return self.storage[self._find_parent_index(index)]

    def _left_child_location(self, index):
        if self._find_left_child_index(index) <= len(self.storage) and index % 2 != 0:
            raise ValueError("Has no left child")
        return self.storage[self._find_left_child_index(index)]

    def _right_child_location(self, index):
        if self._find_right_child_index(index) >= len(self.storage):
            raise ValueError("Has no right child")
        return self.storage[self._find_right_child_index(index)]

    def _full_heap(self):
        return len(self.storage) == self.max_num_elements

    def _swap(self, index1, index2):
        spot_holder = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = spot_holder

    def push(self, value):
        if self._full_heap():
            raise ValueError("Full heap")
        else:
            self.storage.append(value)
            self._heapify_up()

    def _heapify_up(self):  # [15, 10]
        index = len(self.storage) - 1  # 1
        while (
            self._has_parent(index)
            and self._parent_location(index) > self.storage[index]
        ):
            self._swap(self._find_parent_index(index), index)
            index = self._find_parent_index(index)

    def pop(self):
        if self.storage == []:
            raise ValueError("Empty heap")
        else:
            self.storage[0] = self.storage[-1]
            self.storage = self.storage[0:-1]
            self._heapify_up()


# filled left to right
# parent node can have 2 or less children
# all levels must be filled before moving on
# parent key must be smaller that its children nodes (smallest to largest)
# root node is always the smallest

# PARENT INDEX: (index - 1)//2
# LEFT CHILD INDEX: 2 * index + 1
# RIGHT CHILD INDEX: 2 * index + 2
