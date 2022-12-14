class Que_:
    def __init__(self, values=None):
        self.items = []
        if values:
            for value in values:
                self.items.append(value)

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("Empty Stack")
        
    def peek(self):
        try:
            return self.items[0]
        except IndexError:
            return None

    def size(self):
        return len(self.items)

    def __len__(self):
        return len(self.items)