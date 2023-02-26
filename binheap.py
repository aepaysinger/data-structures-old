class BinHeap:
    def __init__(self, max_num_elements, heap_type, values=None):
        self.storage = []
        self.max_num_elements = max_num_elements
        self.heap_type = heap_type
        if values:
            for value in values:
                self.storage.append(value)
                if heap_type == "min":
                    self._heapify_up()
                elif heap_type == "max":
                    self._heapify_down()

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

        return self.storage[self._find_parent_index(index)]

    def _left_child_location(self, index):

        return self.storage[self._find_left_child_index(index)]

    def _right_child_location(self, index):

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
            if self.heap_type == "min":
                self._heapify_up()
            else:
                self._heapify_down()

    def _heapify_up(self):
        index = len(self.storage) - 1
        while (
            self._has_parent(index)
            and self._parent_location(index) > self.storage[index]
        ):
            self._swap(self._find_parent_index(index), index)
            index = self._find_parent_index(index)

    def _heapify_down(self):
        index = len(self.storage) - 1
        while (
            self._has_parent(index)
            and self._parent_location(index) < self.storage[index]
        ):
            self._swap(self._find_parent_index(index), index)
            index = self._find_parent_index(index)

    def pop(self):
        if self.storage == []:
            raise ValueError("Empty heap")
        else:
            self.storage[0] = self.storage[-1]
            del self.storage[-1]
            if self.heap_type == "min":
                self._heapify_up()
            else:
                self._heapify_down()
