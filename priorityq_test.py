from priorityq import PriorityQueue


def test_priority_queue_insert():
    priorityq = PriorityQueue()
    priorityq._insert("aa", -1)
    priorityq._insert("b", 2)
    priorityq._insert("a", 1)
    priorityq._insert("c", 3)

    assert priorityq.storage == [(-1, "aa"), (1, "a"), (2, "b"), (3, "c")]

    priorityq._insert("f")

    assert priorityq.storage == [(-1, "aa"), (1, "a"), (2, "b"), (3, "c"), (3, "f")]


def test_priority_queue_pop():
    priorityq = PriorityQueue()
    priorityq._insert(55, 1)
    priorityq._insert("alpha", -3)
    priorityq._insert("bravo")
    priorityq._insert(4, 2)

    assert priorityq.pop() == (-3, "alpha")
    assert priorityq.storage == [(1, 55), (1, "bravo"), (2, 4)]


def test_priority_queue_peek():
    priorityq = PriorityQueue()
    priorityq._insert("alpha")
    priorityq._insert("beta")

    assert priorityq.peek() == (0, "alpha")

    assert priorityq.storage == [(0, "alpha"), (0, "beta")]
