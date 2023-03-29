class PriorityQueueB:
    def __init__(self):
        self.storage = []
        
    def pop(self):
        return self.storage.pop(0)

    def peek(self):
        return self.storage[0]
    
    def insert(self, value, priority=0, left=0, right=None):
        if self.storage == []:
            self.storage.append((priority, value))
        else:
            if priority:
                left = 0
                right = len(self.storage) - 1
                mid = (left + right) // 2

                if priority > self.storage[-1][0]:
                    self.storage.append((priority, value))
                elif priority < self.storage[0][0]:
                    self.storage.insert(0, (priority, value))
                elif self.storage[mid][0] == priority:
                    for i in range(mid, len(self.storage)):
                        if self.storage[i+1] > priority:
                            self.storage.insert(i +1, (priority, value))
                elif self.storage[mid][0] < priority and self.storage[mid + 1][0] > priority:
                    self.storage.insert(mid + 1, (priority, value))
                elif priority > mid:
                    self.insert(self, priority, left, mid)
                elif priority < mid:
                    self.insert(self, priority, mid, right)
            else:
                self.storage.append((self.storage[-1][0], value))