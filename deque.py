class Deque:
    def __init__(self, values=None):
        self.items = []
        if values:
            for value in values:
                self.items.append(value)               

    def append(self, value):
        self.items.append(value)

    def appendleft(self, value):
        self.items.insert(0, value)

    def pop(self):
        if len(self.items) == 0:
            raise ValueError("There are not items to pop.")
        else:
            return self.items.pop()

    def popleft(self):
        if len(self.items) == 0:
            raise ValueError("There are not items to popleft.")
        else:
            return self.items.pop(0)

    def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]

    def peekleft(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[0]        

    def size(self):
        return len(self.items)

