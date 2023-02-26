import pytest


from binheap import BinHeap


def test_min_heap():
    min_heap = BinHeap(6, "min", [7, 4, 1, 3])

    assert min_heap.storage == [1, 3, 4, 7]


def test_min_heap_find():
    min_heap = BinHeap(6, "min", [7, 4, 1, 3])

    assert min_heap.storage == [1, 3, 4, 7]
    assert min_heap._find_parent_index(2) == 0
    assert min_heap._find_left_child_index(0) == 1
    assert min_heap._find_right_child_index(0) == 2


def test_min_heap_has():
    min_heap = BinHeap(4, "min", [6, 2, 4, 8])

    assert min_heap.storage == [2, 6, 4, 8]
    assert min_heap._has_left_child(0) == True
    assert min_heap._has_right_child(2) == False
    assert min_heap._has_parent(3) == True
    

def test_min_heap_location():
    min_heap = BinHeap(5, "min", [8, 1, 5, 3, 9])

    assert min_heap.storage == [1, 3, 5, 8, 9]
    assert min_heap._parent_location(2) == 1
    assert min_heap._left_child_location(0) == 3
    assert min_heap._right_child_location(1) == 9
    assert min_heap._full_heap() == True


def test_min_heap_push():
    min_heap = BinHeap(5, "min", [5, 2, 6, 1])

    assert min_heap.storage == [1, 2, 6, 5]

    min_heap.push(4)

    assert min_heap.storage == [1, 2, 6, 5, 4]

    with pytest.raises(ValueError) as exc_info:
        min_heap.push(7)
    assert exc_info.value.args[0] == "Full heap" 


def test_min_heap_pop():
    min_heap = BinHeap(3, "min", [1, 3, 4])
    min_heap.pop()

    assert min_heap.storage == [3, 4]

    min_heap.pop()
    min_heap.pop()

    with pytest.raises(ValueError) as exc_info:
        min_heap.pop()
    assert exc_info.value.args[0] == "Empty heap"


def test_max_heap():
    max_heap = BinHeap(6, "max", [7, 4, 1, 3])

    assert max_heap.storage == [7, 4, 1, 3]


def test_max_heap_find():
    max_heap = BinHeap(6, "max", [1, 3, 4, 7])

    assert max_heap.storage == [7, 4, 3, 1]
    assert max_heap._find_parent_index(2) == 0
    assert max_heap._find_left_child_index(0) == 1
    assert max_heap._find_right_child_index(0) == 2


def test_max_heap_has():
    max_heap = BinHeap(4, "max", [6, 2, 4, 8])

    assert max_heap.storage == [8, 6, 4, 2]
    assert max_heap._has_left_child(0) == True
    assert max_heap._has_right_child(2) == False
    assert max_heap._has_parent(3) == True


def test_max_heap_location():
    max_heap = BinHeap(5, "max", [8, 1, 5, 3, 9])

    assert max_heap.storage == [9, 8, 5, 1, 3]
    assert max_heap._parent_location(2) == 9
    assert max_heap._left_child_location(0) == 8
    assert max_heap._right_child_location(1) == 3
    assert max_heap._full_heap() == True


def test_max_heap_push():
    max_heap = BinHeap(5, "max", [5, 2, 6, 1])

    assert max_heap.storage == [6, 2, 5, 1]

    max_heap.push(4)

    assert max_heap.storage == [6, 4, 5, 1, 2]

    with pytest.raises(ValueError) as exc_info:
        max_heap.push(7)
    assert exc_info.value.args[0] == "Full heap" 


def test_max_heap_pop():
    max_heap = BinHeap(3, "max", [4, 1, 3])
    max_heap.pop()

    assert max_heap.storage == [3, 1]

    max_heap.pop()
    max_heap.pop()

    with pytest.raises(ValueError) as exc_info:
        max_heap.pop()
    assert exc_info.value.args[0] == "Empty heap"