class DoubleLinkedList:
    def __init__(self, values=None):
        self.head = None
        self._length = 0
        if values:
            for value in values:
                self.head = Node(value, self.head, None)
                if self.head.next:
                    self.head.next.previous = self.head
                self._length += 1

    def push(self, value):
        """
        will insert the value val at the head of the list
        """

        self.head = Node(value, self.head, None)
        if self.head.next:
            self.head.next.previous = self.head
        self._length += 1

    def append(self, value):
        """
        will append the value val at the tail of the list
        """

        node = self.head
        if not node:
            self.head = Node(value, self.head, None)
            self._length += 1
            return
        while node.next:
            node = node.next

        node.next = Node(value, None, node)
        self._length += 1

    def pop(self):
        """
        will pop the first value off the head of the list and return it.
        Raises an exception with an appropriate message if there are no
        values to return.
        """

        if self.head:
            old_head = self.head
            self.head = self.head.next
            self.head.previous = None
            self._length -= 1

            return old_head.value
        else:
            raise ValueError("empty list")

    def shift(self):
        """
        will remove the last value from the tail of the list and return it.
        Raises an exception with an appropriate message if there are no values to
        return.
        """

        node = self.head
        if not node:
            raise ValueError("empty list")
        while node.next:
            node = node.next
        node.previous.next = None
        self._length -= 1
        return node.value

    def __len__(self):
        return self._length

    def remove(self, value):
        """
        will remove the first instance of val found in the list, starting from the head.
        If val is not present, it will raise an appropriate Python exception.
        """

        node = self.head
        while node:
            if node.value == value:
                if node == self.head:
                    if self.head.next == None:
                        self.head = None
                    else:
                        self.head.next.previous = None
                        self.head = self.head.next
                elif node.next is None:
                    node.previous.next = None
                else:
                    node.previous.next = node.next
                    node.next.previous = node.previous

                self._length -= 1
                return

            else:
                node = node.next

        raise ValueError("number not in list")


class Node:
    def __init__(self, value, next, previous):
        self.value = value
        self.next = next
        self.previous = previous
