from linked_list import LinkedList


class Que_():
    def __init__(self, values=None):
        self.linked_list = LinkedList(values)


    def enqueue(self, value):
        self.linked_list.push(value)

    
    def dequeue(self):
        self.linked_list.pop()

    
    def peek(self):
        if len(self.linked_list) >= 2:
            return self.linked_list.head.next.value
        else:
            return None

    
    def size(self):
        return len(self.linked_list)

