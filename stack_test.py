import pytest


from stack import Node, Stack


def test_push():
    sl = Stack([1, 2, 3])
    sl.push(5)

    assert sl.head.value == 5
    assert sl._length == 4


def test_pop():
    sl = Stack([1, 2, 3])
    sl.pop()

    assert sl.head.value == 2
    assert sl._length == 2

    sl.pop()
    sl.pop()
    
    with pytest.raises(ValueError) as exc_info:
        sl.pop()
        assert exc_info.value.args[0] == "There are no values to remove"
    assert sl._length == 0    

    