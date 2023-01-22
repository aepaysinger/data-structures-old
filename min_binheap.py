class MinHeap:
    def __init__(self, max_num_elements):
        self.storage = []
        self.max_num_elements = max_num_elements 
        self.size = 0 

    def find_parent_index(self, index):
        return (index - 1) // 2

    def find_left_child_index(self, index):
        return (2 * index) + 1

    def find_right_child_index(self, index):
        return (2 * index) + 2

    def has_parent(self, index):
        return self.find_parent_index(index) >= 0 
    
    def has_left_child(self, index):
        return self.find_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.find_right_child_index(index) < self.size

    def parent_location(self, index):
        return self.storage[self.find_parent_index(index)]

    def left_child_location(self, index):
        return self.storage[self.find_left_child_index(index)]

    def right_child_location(self, index):
        return self.storage[self.find_right_child_index(index)]

    def full_heap(self):
        return self.size == self.max_num_elements
    
    def swap(self, index1, index2):
        spot_holder = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = spot_holder

    def push(self, value):
        if self.full_heap():
            raise ValueError("Full heap")
        else:
            self.storage[self.size] = value
            self.size += 1
            self.heapify_up()

    def heapify_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.parent_location(index) > self.storage[index]:
            self.swap(self.find_parent_index(index), index)
            index = self.find_parent_index(index)

    def pop(self):
        if self.storage == []:
            raise ValueError("Empty heap")
        else:
            self.storage[0] = self.storage[-1]
            self.size -= 1
            self.heapify_up()
        

# filled left to right
# parent node can have 2 or less children
# all levels must be filled before moving on 
# parent key must be smaller that its children nodes (smallest to largest)
# root node is always the smallest

# PARENT INDEX: (index - 1)//2
# LEFT CHILD INDEX: 2 * index + 1
# RIGHT CHILD INDEX: 2 * index + 2