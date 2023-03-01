class PriorityQueue:
    def __init__(self):
        self.storage = []

    def insert(self, value, priority=0):
        if self.storage == []:
            self.storage.append((priority, value))
        else:
            if priority:
                for i in range(len(self.storage) + 1):
                    print(i, self.storage[i])
                    if priority < self.storage[i][0]:
                        self.storage.insert(i, (priority, value))
                        break
                    elif i == len(self.storage) - 1:
                        self.storage.append((priority, value))
                        break
                    elif (
                        priority > self.storage[i][0]
                        and priority < self.storage[i + 1][0]
                    ):
                        self.storage.insert(i + 1, (priority, value))
                        break
            else:
                self.storage.append((self.storage[-1][0], value))

    def pop(self):
        return self.storage.pop(0)

    def peek(self):
        return self.storage[0]
