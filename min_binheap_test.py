from min_binheap import MinHeap


def test_minheap_find_parent_index():
    min_heap = MinHeap([5, 10, 15])
    
    assert min_heap.find_parent_index(2) == 0

def test_minheap_find_left_child_index():
    min_heap = MinHeap([5, 10, 15])

    assert min_heap.find_left_child_index(0) == 1

def test_minheap_find_right_child_index():
    min_heap = MinHeap([5, 10, 15])

    assert min_heap.find_right_child_index(0) == 2


def test_minheap_has_parent():
    min_heap = MinHeap([5, 10, 15])

    assert min_heap.has_parent(1) == True

    assert min_heap.has_parent(0) == False


def test_minheap_has_left_child():
    min_heap = MinHeap([5, 10, 15])

    assert min_heap.size == 3

    assert min_heap.has_left_child(0) == True

    assert min_heap.has_left_child(1) == False

    assert min_heap.has_left_child(2) == False
