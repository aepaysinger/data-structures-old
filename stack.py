class Stack:
    def __init__(self, values=None):
        self.head = None
        self._length = 0

        for value in values[::-1]:
            self.head = Node(value, self.head)
            self._length += 1


    def push(self, value):
        """
        Adds a value to the stack. The parameter is the value to be added 
        to the stack.
        """
        self.head = Node(value, self.head)
        self._length += 1
    
    def pop(self):
        """
        Removes a value from the stack and returns that value. 
        If the stack is empty, attempts to call pop should raise an 
        appropriate Python exception with message.
        """
        
        try:
            value = self.head.value
        except AttributeError:
            raise ValueError("There are no values to remove")
        self.head = self.head.next
        self._length -= 1
        return value


        


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
    def __eq__(self, other):
       return self.value == other.value