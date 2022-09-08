class DoubleLinkedList:
    def __init__(self, values):
        self.head = None
        self._length = 0

        for value in values:
            self.head = Node(value, next, previous)
            
        

            

    def push(self, value): 
        """
        will insert the value val at the head of the list
        """
      


    def append(self, value): 
        """
        will append the value val at the tail of the list
        """
     


    # def pop(self): 
    #     """
    #     will pop the first value off the head of the list and return it.
    #     Raises an exception with an appropriate message if there are no 
    #     values to return.
    #     """
    #     


    # def shift(self):[1,2,3]
    #     """ 
    #     will remove the last value from the tail of the list and return it. 
    #     Raises an exception with an appropriate message if there are no values to 
    #     return.
    #     """
  

        



class Node:
    def __init__(self, value, next, previous):
        self.value = value
        self.next = next
        self.previous = previous




  