class Graph:
    def __init__(self):
        self.storage = {}

    def nodes(self):
        return list(self.storage.keys())

    def edges(self):
        return list(self.storage.values())

    def add_node(self, value):
        self.storage[value] = []

    def add_edge(self, value1, value2):
        if value1 in self.storage:
            self.storage[value1].append(value2)
        else:
            self.storage[value1] = [value2]
        if value2 in self.storage:
            self.storage[value2].append(value1)
        else:
            self.storage[value2] = [value1]

    def del_node(self, value):
        if value in self.storage:
            for edge in self.storage[value]:
                self.storage[edge].remove(value)
            del self.storage[value]
        else:
            raise ValueError("Node does not exist")

    def del_edge(self, value1, value2):
        if value1 in self.storage and value2 in self.storage[value1]:
            self.storage[value1].remove(value2)
            self.storage[value2].remove(value1)
        else:
            raise ValueError("Edge does not exist")

    def has_node(self, value):
        return value in self.storage

    def neighbors(self, value):
        if value in self.storage:
            return self.storage[value]
        else:
            raise ValueError("Value does not exist")

    def adjcent(self, value1, value2):
        if value1 not in self.storage:
            raise ValueError("Value does not exist")
        elif value2 not in self.storage[value1]:
            raise ValueError("Value does not exist")
        else:
            return value2 in self.storage[value1]
