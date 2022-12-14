class Que_:
    def __init__(self, values=None):
        self.items = []
        if values:
            for value in values:
                self.items.append(value)

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if len(self.items) > 0:
            self.items.pop(0)
        else:
            raise ValueError("Empty List")

    def peek(self):
        if len(self.items) >= 2:
            return self.items[1]
        else:
            return None

    def size(self):
        return len(self.items)
