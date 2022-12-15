import pytest

from double_linked_list import DoubleLinkedList, Node


def test_dll_init():
    dll = DoubleLinkedList([1, 2, 3])

    assert dll.head.value == 3
    assert dll.head.previous is None
    assert dll.head.next.next.value == 1
    assert dll.head.next.next.next is None
    assert dll.head.next.next.previous is dll.head.next


def test_dll_push():
    dll = DoubleLinkedList([1, 2, 3])
    dll.push(4)

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
    assert dll.head.next is None
    assert dll.head.previous is None


def test_dll_append():
    dll = DoubleLinkedList([1, 2, 3])
    dll.append(4)

    assert dll.head.value == 3
    assert dll.head.next.next.next.value == 4
    assert dll.head.next.next.next.next is None
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


def test_dll_len():
    dll = DoubleLinkedList([1, 2, 3])

    assert len(dll) == 3


def test_dll_remove():
    dll = DoubleLinkedList([])

    with pytest.raises(ValueError) as exc_info:
        dll.remove(5)

    dll = DoubleLinkedList([5])
    dll.remove(5)

    assert dll.head is None
    assert len(dll) == 0

    dll = DoubleLinkedList([3, 6])
    dll.remove(3)

    assert dll.head.value == 6
    assert dll.head.next is None
    assert dll.head.previous is None

    dll = DoubleLinkedList([3, 6])
    dll.remove(6)

    assert dll.head.value == 3
    assert dll.head.next is None
    assert dll.head.previous is None

    dll = DoubleLinkedList([3, 6, 9])
    dll.remove(6)

    assert dll.head.value == 9
    assert dll.head.next.value == 3
    assert dll.head.previous is None
    assert len(dll) == 2

def test_dll_remove_first_from_3():
    dll = DoubleLinkedList([4,8,1])
    dll.remove(1)

    assert dll.head.value == 8
    assert dll.head.previous is None
    assert dll.head.next.value == 4
    assert dll.head.next.next is None


def test_dll_remove_last_from_3():
    dll = DoubleLinkedList([4,8,1])
    dll.remove(4)

    assert dll.head.value == 1
    assert dll.head.previous is None
    assert dll.head.next.value == 8
    assert dll.head.next.next is None    


def test_dll_remove_not_in_list():
    dll = DoubleLinkedList([4, 7, 5])

    with pytest.raises(ValueError) as exc_info:
        dll.remove(3)
    assert str(exc_info.value) == "number not in list"

    assert dll.head.value == 5
    assert dll.head.next.value == 7
