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

    def depth_first_traversal(self, start_val):
        path = [start_val]
        node_to_check = start_val
        while len(path) < len(self.storage):
            for node_to_check in self.storage:
                for edge in self.storage[node_to_check]:
                    if edge not in path:
                        path.append(edge)
                for edge in self.storage[node_to_check]:
                    for item in self.storage[edge]:
                        if item not in path:
                            node_to_check = item
        return path

    # def breadth_first_traversal(self, start_val):
    #     path = [start_val]
    #     next_to_check = start_val
    #     while len(path) < len(self.storage):
    #         for edge in self.storage[next_to_check]:
    #             path.append(edge)
            




#{4: [16, 8], 9: [81], 16: [4], 8: [4], 81: [9]}
graph = Graph()
graph.add_edge(4, 16)
graph.add_edge(4, 8)
graph.add_edge(9, 81)
print(graph.depth_first_traversal(4))      