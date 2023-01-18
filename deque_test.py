import pytest

from deque import Deque


def test_deque_append():
    deque = Deque([2, 4, 5])
    deque.append(9)

    assert deque.items == [2, 4, 5, 9]


def test_deque_appendleft():
    deque = Deque([4, 8, 2, 7])
    deque.appendleft(1)

    assert deque.items == [1, 4, 8, 2, 7]


def test_deque_pop():
    deque = Deque([2, 6, 4])
    
    assert deque.pop() == 4
    assert deque.items == [2, 6]

    deque.pop()
    deque.pop()

    with pytest.raises(ValueError) as exc_info:
        deque.pop()
    assert str(exc_info.value) == "There are not items to pop."


def test_deque_popleft():
    deque = Deque([3, 7, 1])

    assert deque.popleft() == 3

    deque.popleft()
    deque.popleft()

    with pytest.raises(ValueError) as exc_info:
        deque.popleft()
    assert str(exc_info.value) == "There are not items to popleft."


def test_peek():
    deque = Deque([8, 2, 7])

    assert deque.peek() == 7

    deque.pop()
    deque.pop()
    deque.pop()

    assert deque.peek() == None


def test_peekleft():
    deque = Deque([9, 5, 2])

    assert deque.peekleft() == 9

    deque.pop()
    deque.pop()
    deque.pop()

    assert deque.peekleft() == None


def test_size():
    deque = Deque([4, 8, 5])

    assert deque.size() == 3

    deque.pop()
    deque.pop()
    deque.pop()

    assert deque.size() == 0