class DoubleLinkedList:
    def __init__(self, values):
        self.head = None  
        self._length = 0
        

        for value in values[::-1]:
            self.head = Node(value, self.head, None)
            if self.head.next is not None:
                self.head.next.previous = self.head
            self._length += 1
            

    def push(self, value): 
        """
        will insert the value val at the head of the list
        """
        self.head = Node(value, self.head, None)
        if self.head.next is not None:
            self.head.next.previous = self.head
            self._length += 1


    def append(self, value): 
        """
        will append the value val at the tail of the list
        """
        current = self.head
        while True:
            if current.next is not None:
                current = current.next
            else:
                break

        current.next = Node(value, None, current)


    # def pop(self): 
    #     """
    #     will pop the first value off the head of the list and return it.
    #     Raises an exception with an appropriate message if there are no 
    #     values to return.
    #     """
    #     try:
    #         value = self.head.value
    #     except AttributeError:
    #         raise ValueError("There are no values to return")
    #     self.head = self.head.next
    #     self._length -= 1
    #     return value


    # def shift(self):[1,2,3]
    #     """ 
    #     will remove the last value from the tail of the list and return it. 
    #     Raises an exception with an appropriate message if there are no values to 
    #     return.
    #     """
    #     try:
    #         value = self.head.value
    #     except AttributeError:
    #         raise ValueError("There are no values to return")

        



class Node:
    def __init__(self, value, next, previous):
        self.value = value
        self.next = next
        self.previous = previous

    def __eq__(self, other):
        return self.value == other.value