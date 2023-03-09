# data-structures
## LinkedList
  * push(val): will insert the value ‘val’ at the head of the list
  * pop(): will pop the first value off the head of the list and return it. Raises an exception with an appropriate message if there are no values to return.
  * size(): will return the length of the list
  * search(val): will return the node containing ‘val’ in the list, if present, else None
  * remove(node): will remove the given node from the list, wherever it might be (node must be an item in the list). If the node is not in the list, it should raise an exception with an appropriate message.
  * display() will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”
  * len(the_list): returns the size of the list
  * 
  * print(the_list): returns what the display() method returns
  ## Stack
  * push(value) - Adds a value to the stack. The parameter is the value to be added to the stack.
  * pop() - Removes a value from the stack and returns that value. If the stack is empty, attempts to call pop should raise an appropriate Python exception with message.
  ## Doubly-Linked List
  * push(val) will insert the value val at the head of the list
  * append(val) will append the value val at the tail of the list
  * pop() will pop the first value off the head of the list and return it. Raises an exception with an appropriate message if there are no values to return.
  * shift() will remove the last value from the tail of the list and return it. Raises an exception with an appropriate message if there are no values to return.
  * remove(val) will remove the first instance of val found in the list, starting from the head. If val is not present, it will raise an appropriate Python exception.
  * len() will return the size of the list.
### Que_
  * enqueue(val): adds value to the queue
  * dequeue(): removes the correct item from the queue and returns its value (should raise an error if the queue is empty)
  * peek(): returns the next value in the queue without dequeueing it. If the queue is empty, returns None
  * size(): return the size of the queue. Should return 0 if the queue is empty.
### Binary Heap - min heap
  * push(val): puts a new value into the heap, maintaining the heap property.
  * pop(): removes the “top” value in the heap, maintaining the heap property.
## Deque
  * append(val): adds value to the end of the deque
  * appendleft(val): adds a value to the front of the deque
  * pop(): removes a value from the end of the deque and returns it (raises an exception if the deque is empty)
  * popleft(): removes a value from the front of the deque and returns it (raises an exception if the deque is empty)
  * peek(): returns the next value that would be returned by pop but leaves the value in the deque (returns None if the deque is empty)
  * peekleft(): returns the next value that would be returned by popleft but leaves the value in the deque (returns None if the deque is empty)
  * size(): returns the count of items in the queue (returns 0 if the queue is empty)
## Priority Queue
  * insert(value): inserts a value into the queue. Takes an optional argument for that value’s priority, set by default to whatever your lowest priority is (i.e. 0, -99, whatever).
  * pop(): removes the most important item from the queue and returns its value.
  * peek(): returns the most important item without removing it from the queue.