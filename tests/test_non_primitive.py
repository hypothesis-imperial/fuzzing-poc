import hypothesis.strategies as st
from hypothesis import given


# Linked list class
class LinkedList:
    # Initialise linked list
    def __init__(self):
        self.data = None
        self.next = None

    # Cons item onto linked list
    def cons(self, item):
        curr = self
        while curr.data is not None:
            curr = curr.next
        curr.data = item
        curr.next = LinkedList()

    # Return length of linked list
    def length(self):
        curr = self
        n = 0
        while curr.data is not None:
            n = n + 1
            curr = curr.next
        return n

    # Show linked list
    def show(self):
        curr = self
        while curr.data is not None:
            print(curr.data)
            curr = curr.next


# Convert array list into linked list
def convert(array_list):
    linked_list = LinkedList()
    for item in array_list:
        linked_list.cons(item)
    return linked_list


# Linked list strategies
LinkedLists = st.lists(st.integers()).map(convert)


# Positive test
@given(LinkedLists)
def test_positive(ls):
    """Test should always return success
    """
    assert ls.length() == ls.length()


# Negative test
@given(LinkedLists)
def test_negative(ls):
    """Test should always return failure
    """
    assert ls.length() == -1
