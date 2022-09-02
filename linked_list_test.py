import io
import pytest
import sys

from linked_list import LinkedList, Node


def test_linked_list_init():
    ll = LinkedList([1])
    value = ll.head.value
    expected = 1

    assert value == expected, f"The value should be {expected}, you got {value}"
    assert (
        ll.head.next is None
    ), f"If the LinkedList is empty your value should be None, you got {ll.head.next}"

    ll = LinkedList([1, 2, 3])
    assert ll.head.value == 3, f"The first value should be 1, you got: {ll.head.value}"
    assert (
        ll.head.next.value == 2
    ), f"The second value should be 2, you got: {ll.head.next.value}"
    assert (
        ll.head.next.next.value == 1
    ), f"The third value should be 3, you got: {ll.head.next.next.value}"
    assert (
        ll.head.next.next.next is None
    ), f"The last value should be None, you got: {ll.head.next.next.next.value}"


def test_linked_list_push():
    ll = LinkedList([1, 2, 3])
    assert ll.head.value == 3
    assert ll.head.next.value == 2
    assert ll.head.next.next.value == 1
    assert ll.head.next.next.next is None

    ll.push(4)
    assert (
        ll.head.value == 4
    ), f"Returned {ll.head.value} instead of 4, when you push a value it goes at the front of the list"
    assert ll.head.next.value == 3
    assert ll.head.next.next.value == 2
    assert ll.head.next.next.next.value == 1
    assert ll.head.next.next.next.next is None


def test_pop_linked_list():
    ll = LinkedList([1, 2, 3])
    assert ll.head.value == 3
    assert ll.head.next.value == 2
    assert ll.head.next.next.value == 1
    assert ll.head.next.next.next is None


def test_linked_list_pop_first_value():
    ll = LinkedList([1, 2, 3])
    actual = ll.pop()
    assert (
        ll.head.value == 2
    ), f"Returned {ll.head.value} instead of 2, The first value is deleted, the second value becomes the first"
    assert ll.head.next.value == 1, "Returned {ll.head.next.value} instead of 3"
    assert actual == 3, "The value that is being poped is 1 not {actual}"


def test_linked_list_pop_4():
    ll = LinkedList([1, 2, 3])
    ll.pop()
    ll.pop()
    ll.pop()
    with pytest.raises(ValueError) as exc_info:
        ll.pop()
        assert exc_info.value.args[0] == "There are no values to return"


def test_linked_list_size():
    ll = LinkedList([1, 2, 3])
    actual = ll.size()
    assert actual == 3, f"The size of the list is 3, you got {actual}"

    ll.push(6)
    assert ll.size() == 4, f"the size of the list is 4, you got {actual}"

    ll.pop()
    assert ll.size() == 3, f"the size of the list is 3, you got {actual}"
    assert ll.head.value == 3, f"the first value is 1, you got {ll.head.value}"

    ll.remove(ll.head.next)
    assert ll.size() == 2
    assert ll.head.value == 3
    assert ll.head.next.value == 1


def test_linked_list_search_with_3():
    ll = LinkedList([1, 2, 3])
    actual = ll.search(2)
    expected_value = 2
    assert (
        actual.value == expected_value
    ), f"the value is {expected_value} you got {actual.value}"
    assert actual == ll.head.next
    assert actual == Node(expected_value, None)


def test_linked_list_search_out_of_range():
    ll = LinkedList([1, 2, 3])
    actual = ll.search(4)
    expected = None
    assert actual == expected, f"Returned {actual} instead of {expected}"


def test_linked_list_remove():
    ll = LinkedList([1, 2, 3])
    ll.remove(ll.head.next)

    assert ll.head.value == 3, f"the first vaue is 3, not {ll.head.value}"
    assert ll.head.next.value == 1, f"the second value is 1, not {ll.head.next.value}"


def test_linked_list_remove_2():
    ll = LinkedList([1, 1, 2, 1, 1])
    ll.remove(ll.head.next.next.next)

    assert ll.head.value == 1
    assert ll.head.next.value == 1
    assert ll.head.next.next.value == 2
    assert ll.head.next.next.next.value == 1
    assert ll.head.next.next.next.next == None


def test_linked_list_remove_last():
    ll = LinkedList([1, 2])
    ll.remove(ll.head.next)

    assert ll.head.value == 2
    assert ll.head.next == None


def test_linked_list_remove_first():
    ll = LinkedList([1, 2])
    ll.remove(ll.head)
    assert ll.head.value == 1
    assert ll.head.next == None


def test_linked_list_remove_not_present():
    ll = LinkedList([1, 2])

    with pytest.raises(ValueError) as exc_info:
        ll.remove(LinkedList(["a", "b"]).head)
        assert exc_info.value.args[0] == "Node not present"
    assert ll.head.value == 2
    assert ll.head.next.value == 1


def test_linked_list_display():
    ll = LinkedList([1, "a", 3])
    unicode_string = ll.display()
    assert unicode_string == "(3, 'a', 1)"


def test_linked_list_len():
    ll = LinkedList([1, 2, 3])

    assert len(ll) == 3


def test_linked_list_print():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    print(LinkedList([3, 5, 1]))
    sys.stdout = sys.__stdout__

    assert (
        capturedOutput.getvalue() == "(1, 5, 3)\n"
    ), f"Printed: {capturedOutput.getvalue()}, '(1, 5, 3)\n'"
