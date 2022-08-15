import pytest


from double_linked_list import DoubleLinkedList, Node


def test_dll_push():
    dll = DoubleLinkedList([1 ,2 ,3])
    dll.push(4)

    assert dll.head.value == 4, "4 should be at the head of the list"
    assert dll._length == 4, "there are 4 values."


def test_dll_append():
    dll = DoubleLinkedList([1, 2, 3])
    dll.append(4)

    assert dll.head.next.next.next.value == 4, "4 should now be the last value in the DoubleLinkedList."