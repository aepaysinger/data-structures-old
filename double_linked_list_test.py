import pytest


from double_linked_list import DoubleLinkedList, Node

def test_dll_init():
    dll = DoubleLinkedList([1, 2, 3])

    # assert dll.head.previous is None
    # assert dll.head.next.previous is dll.head
    assert dll.head.value == 3
    assert dll.head.next.next.value == 1
    assert dll.head.next.next.next is None
    assert dll.head.next.next.previous is dll.head.next


def test_dll_push():
    dll = DoubleLinkedList([1 ,2 ,3])
    dll.push(4) #[1, 2, 3, 4]

    assert dll.head.value == 4
    assert dll._length == 4
    assert dll.head.previous is None
    assert dll.head.next.previous is dll.head
    assert dll.head.next.value == 3


def test_dll_append_empty():
    dll = DoubleLinkedList([])
    dll.append(4)

    assert dll.head.value == 4
    assert dll._length == 1


def test_dll_append():
    dll = DoubleLinkedList([1, 2, 3])
    dll.append(4) 

    assert dll.head.value == 3
    assert dll.head.next.next.next.value == 4
    assert dll.head.next.next.next.previous.value == 1

def test_dll_pop_1():
    dll = DoubleLinkedList([1, 2, 3])
    assert dll.pop() == 3
    assert dll.head.value == 2
    assert dll._length == 2
    assert dll.head.previous is None
    assert dll.head.next.value == 1
    

def test_dll_pop_empty():
    dll = DoubleLinkedList()
    
    with pytest.raises(ValueError) as excinfo:
        dll.pop()

    assert str(excinfo.value) == "empty list"
    

def test_dll_shift():
    dll = DoubleLinkedList([1, 2, 3])
    dll.shift()

    assert dll.head.next.next is None
    assert dll._length == 2
    assert dll.head.value == 3
    assert dll.head.next.value == 2
    assert dll.head.previous is None


def test_dll_shift_empty():
    dll = DoubleLinkedList()

    with pytest.raises(ValueError) as excinfo:
        dll.shift()

    assert str(excinfo.value) == "empty list"
