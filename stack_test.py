import pytest

from stack import Stack


def test_push():
    sl = Stack([1, 2, 3])
    sl.push(5)

    assert sl.linked_list.head.value == 5
    assert len(sl) == 4


def test_pop():
    sl = Stack([1, 2, 3])
    sl.pop()

    assert sl.linked_list.head.value == 2
    assert len(sl) == 2

    sl.pop()
    sl.pop()

    with pytest.raises(ValueError) as exc_info:
        sl.pop()
        assert exc_info.value.args[0] == "There are no values to remove"
    assert len(sl) == 0


def test_create_empty_stack_list():
    sl = Stack()
    assert len(sl) == 0
    assert sl.linked_list.head is None
