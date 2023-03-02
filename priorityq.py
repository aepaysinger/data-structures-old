import bisect

class PriorityQueue:
    def __init__(self):
        self.storage = []

    def insert(self, value, priority=0):
        if self.storage == []:
            self.storage.append((priority, value))
        elif priority:
            self.storage.reverse()
            bisect.insort_right(self.storage, (priority, value))
            self.storage.reverse()
        else:
            self.storage.insert(0, (self.storage[0][0], value))

    def pop(self):
        return self.storage.pop()

    def peek(self):
        return self.storage[-1]
