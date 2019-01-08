from hypothesis import strategies
from hypothesis import given


@given(strategies.integers())
def test_op(n):
    # assert(n > 0)
    # assert(n == 0)
    assert(n < 0)
    list[1 / n]
    list = []
    list[1 / (n - 1)]
    list[1 / (n + 1)]
    list.pop()
    divide("", '')
