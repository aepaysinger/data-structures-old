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

    def del_node(self, value):
        if value in self.storage:
            del self.storage[value]
        else:
            raise ValueError("Node does not exist")

    def del_edge(self, value1, value2):
        if value1 in self.storage:
            if value2 in self.storage[value1]:
                self.storage[value1].remove(value2)
            else:
                raise ValueError("Edge does not exist")
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
