import pytest


from que_ import Que_


def test_que_enqueue():
    que = Que_([1, 2, 3])
    que.enqueue(4)

    assert que.linked_list.head.value == 4

def test_dequeue():
    que = Que_([3, 6, 4])
    que.dequeue()

    assert que.linked_list.head.value == 6

    que.dequeue()
    que.dequeue()

    with pytest.raises(ValueError) as exc_info:
        que.dequeue()
        assert exc_info.value.args[0] == "There are no values to return"


def test_peek():
    que = Que_([9, 4, 2])

    assert que.peek() == 4


def test_size():
    que = Que_([3, 6, 3, 4, 1])

    assert que.size() == 5

    que.dequeue()
    que.dequeue()
    que.dequeue()
    que.dequeue()
    que.dequeue()

    assert que.size() == 0