from priorityq_binary_search import PriorityQueueB


def test_priority_queue_insert():
    priorityq = PriorityQueueB()
    priorityq.insert("aa", -1)
    priorityq.insert("b", 2)
    priorityq.insert("a", 1)
    priorityq.insert("c", 3)

    assert priorityq.storage == [(-1, "aa"), (1, "a"), (2, "b"), (3, "c")]

    priorityq.insert("f")

    assert priorityq.storage == [(-1, "aa"), (1, "a"), (2, "b"), (3, "c"), (3, "f")]


def test_priority_queue_pop():
    priorityq = PriorityQueueB()
    priorityq.insert(55, 1)
    priorityq.insert("alpha", -3)
    priorityq.insert("bravo")
    priorityq.insert(4, 2)

    assert priorityq.pop() == (-3, "alpha")
    assert priorityq.storage == [(1, 55), (1, "bravo"), (2, 4)]


def test_priority_queue_peek():
    priorityq = PriorityQueueB()
    priorityq.insert("alpha")
    priorityq.insert("beta")

    assert priorityq.peek() == (0, "alpha")

    assert priorityq.storage == [(0, "alpha"), (0, "beta")]
