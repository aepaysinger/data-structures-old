import pytest


from double_linked_list import DoubleLinkedList, Node

def test_dll_init():
    dll = DoubleLinkedList([1, 2, 3])

    assert dll.head.previous is None
    assert dll.head.next.previous is dll.head
    assert dll.head.value == 1
    assert dll.head.next.next.value == 3
    assert dll.head.next.next.next is None
    assert dll.head.next.next.previous is dll.head.next



def test_dll_push():
    dll = DoubleLinkedList([1 ,2 ,3])
    dll.push(4)

    assert dll.head.value == 4, "4 should be at the head of the list"
    assert dll._length == 4, f"***is should be ***"
    assert dll.head.previous is None
    assert dll.head.next.previous is dll.head


def test_dll_append():
    dll = DoubleLinkedList([1, 2, 3])
    dll.append(4)

    assert dll.head.value == 1
    assert dll.head.next.next.next.value == 4, "4 should now be the last value in the DoubleLinkedList."
    assert dll.head.next.next.next.previous.value == 3

# def test_dll_pop_1():
#     dll = DoubleLinkedList([1, 2, 3])
#     dll.pop()

#     assert dll.head.value == 2

 
# def test_dll_shift():
#     dll = DoubleLinkedList([1, 2, 3])
#     dll.shift()

#     assert dll.head.next.next is None
#     assert dll._length == 2