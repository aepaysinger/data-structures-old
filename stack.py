from linked_list import LinkedList


class Stack:
    def __init__(self, values=None):
        self.linked_list = LinkedList(values)


    def push(self, value):
        """
        Adds a value to the stack. The parameter is the value to be added 
        to the stack.
        """
        self.linked_list.push(value)
    
    def pop(self):
        """
        Removes a value from the stack and returns that value. 
        If the stack is empty, attempts to call pop should raise an 
        appropriate Python exception with message.
        """

        return self.linked_list.pop()

    def __len__(self):
        return self.linked_list.size()

