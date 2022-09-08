class LinkedList:
    def __init__(self, values=None):
        self.head = None  # node with a pointer(next) to the next node
        self._length = 0

        if values == None:
            self.head = None
        else:
            for value in values:
                self.head = Node(value, self.head)
                self._length += 1

    def push(self, value):
        """
        will insert value at the self.head of the list
        """
        self.head = Node(value, self.head)
        self._length += 1

    def pop(self):
        """
        will pop the first value off the head of the list and return it. Raises an exception with an appropriate message if there are no values to return.
        """
        try:
            value = self.head.value
        except AttributeError:
            raise ValueError("There are no values to return")
        self.head = self.head.next
        self._length -= 1
        return value

    def size(self):
        """
        size() will return the length of the list
        """
        # this is another way to check the length if i didnt have the _length method
        # count = 0
        # current = self.head
        # while current:
        #     count += 1
        #     current = current.next
        # return count
        return self._length

    def search(self, value):
        """
        will return the node containing ‘val’ in the list, if present, else None
        """
        current = self.head
        while current:
            if value == current.value:
                return current
            else:
                current = current.next
        return None

    def remove(self, node):
        """
        will remove the given node from the list, wherever it might be
        (node must be an item in the list). If the node is not in the list,
        it should raise an exception with an appropriate message.
        """
        previous = None
        current = self.head
        while current:
            if current is node:
                if current is self.head:
                    self.head = self.head.next
                    return
                previous.next = current.next
                return
            previous = current
            current = current.next
            self._length -= 1
        raise ValueError("Node not present")

    def display(self):
        """
        will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”
        """
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next

        values = tuple(values)
        return str(values)

    def __len__(self):
        return self._length

    def __str__(self):
        return self.display()


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __eq__(self, other):
        return self.value == other.value
