import bisect
import math


class PriorityQueue:
    def __init__(self):
        self.storage = []
        
    def insert(self, value, priority=-math.inf):
        if self.storage == []:
            self.storage.append((priority, value))
            return
        for i in range(len(self.storage) + 1):
            bisect.insort_left(self.storage, (priority, value), key=lambda t: t[0])
            break

    def pop(self):
        return self.storage.pop()

    def peek(self):
        return self.storage[-1]
