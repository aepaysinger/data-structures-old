from priorityq import PriorityQueue


def test_priority_queue_insert():
    priorityq = PriorityQueue()
    priorityq.insert("aa", -1)
    priorityq.insert("b", 2)
    priorityq.insert("a", 1)
    priorityq.insert("c", 3)

    assert priorityq.storage == [(-1, "aa"), (1, "a"), (2, "b"), (3, "c")]

    priorityq.insert("f")

    assert priorityq.storage == [(-1, "f"), (-1, "aa"), (1, "a"), (2, "b"), (3, "c")]


def test_priority_queue_pop():
    priorityq = PriorityQueue()
    priorityq.insert(55, 1)
    priorityq.insert("alpha", -3)
    priorityq.insert("bravo")
    priorityq.insert(4, 2)

    assert priorityq.pop() == (2, 4)
    assert priorityq.storage == [(-3, "bravo"), (-3, "alpha"), (1, 55)]


def test_priority_queue_peek():
    priorityq = PriorityQueue()
    priorityq.insert("alpha")
    priorityq.insert("beta")

    assert priorityq.peek() == (0, "alpha")

    assert priorityq.storage == [(0, "beta"), (0, "alpha")]
