class DoubleLinkedList:
    def __init__(self, values):
        self.head = None  
        self.previous = None
        self._length = 0

        for value in values[::-1]:
            self.head = Node(value, self.head, self.previous)
            self._length += 1



    def push(self, value): 
        """
        will insert the value val at the head of the list
        """
        self.head = Node(value, self.head, self.previous)
        self._length += 1


    def append(self, value): #[1, 2, 3]4
        """
        will append the value val at the tail of the list
        """
        if self.next.value == None:
            self.previous = self.next
            self.next = self.next.next


class Node:
    def __init__(self, value, next, previous):
        self.value = value
        self.next = next
        self.previous = previous

    def __eq__(self, other):
        return self.value == other.value