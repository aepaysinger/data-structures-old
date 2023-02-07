import pytest


from min_binheap import MinHeap


def test_minheap_find_parent_index():
    min_heap = MinHeap(3, [5, 10, 15])

    assert min_heap._find_parent_index(2) == 0


def test_minheap_find_left_child_index():
    min_heap = MinHeap(3, [5, 10, 15])

    assert min_heap._find_left_child_index(0) == 1


def test_minheap_find_right_child_index():
    min_heap = MinHeap(3, [5, 10, 15])

    assert min_heap._find_right_child_index(0) == 2


def test_minheap_has_parent():
    min_heap = MinHeap(3, [5, 10, 15])

    assert min_heap._has_parent(1) == True

    assert min_heap._has_parent(0) == False


def test_minheap_has_left_child():
    min_heap = MinHeap(3, [5, 10, 15])

    assert min_heap.size == 3

    assert min_heap._has_left_child(0) == True

    assert min_heap._has_left_child(1) == False

    assert min_heap._has_left_child(2) == False


def test_minheap_has_right_child():
    min_heap = MinHeap(4, [20, 10, 30])

    assert min_heap.size == 3

    assert min_heap._has_right_child(0) == True

    assert min_heap._has_right_child(1) == False

    assert min_heap._has_right_child(2) == False


def test_parent_location():
    min_heap = MinHeap(4, [15, 10, 5])

    assert min_heap.storage[0] == 5

    with pytest.raises(ValueError) as exc_info:
        min_heap._parent_location(0)
    assert exc_info.value.args[0] == "Root Element"

    assert min_heap._parent_location(1) == 5


def test_left_child_location():
    min_heap = MinHeap(4, [5, 10, 15])

    assert min_heap.size == 3

    assert min_heap._left_child_location(0) == 10

    with pytest.raises(ValueError) as exc_info:
        min_heap._left_child_location(1)
    assert exc_info.value.args[0] == "Has no left child"


def test_right_child_location():
    min_heap = MinHeap(3, [15, 10, 5])

    assert min_heap.size == 3

    assert min_heap.storage == [5, 10, 15]

    assert min_heap._right_child_location(0) == 15

    with pytest.raises(ValueError) as exc_info:
        min_heap._right_child_location(1)
    assert exc_info.value.args[0] == "Has no right child"

    with pytest.raises(ValueError) as exc_info:
        min_heap._right_child_location(2)
    assert exc_info.value.args[0] == "Has no right child"


def test_full_heap():
    min_heap = MinHeap(4, [15, 10, 5])

    assert min_heap.size == 3

    assert min_heap._full_heap() == False

    assert min_heap.max_num_elements == 4

    min_heap.push(30)

    assert min_heap._full_heap() == True


def test_heapify_up():
    min_heap = MinHeap(4)
    min_heap.storage = [15, 10]
    min_heap.size = 2
    min_heap._heapify_up()

    assert min_heap.storage == [10, 15]


def test_swap():
    min_heap = MinHeap(4, [5, 10, 15])
    assert min_heap.storage[0] == 5
    min_heap._swap(0, 1)

    assert min_heap.storage[0] == 10


def test_push():
    min_heap = MinHeap(4, [5, 10, 15])
    min_heap.push(2)

    assert min_heap.storage[0] == 2

    with pytest.raises(ValueError) as exc_info:
        min_heap.push(16)
    assert exc_info.value.args[0] == "Full heap"


def test_pop():
    min_heap = MinHeap(3, [5, 10, 15])
    min_heap.pop()

    assert min_heap.storage[0] == 10

    min_heap.pop()
    min_heap.pop()

    with pytest.raises(ValueError) as exc_info:
        min_heap.pop()
    assert exc_info.value.args[0] == "Empty heap"
