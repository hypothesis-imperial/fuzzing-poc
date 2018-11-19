import hypothesis.strategies as st
from hypothesis import given, settings, unlimited


@given(st.integers())
def test_two_errors(v):
    assert v != 0
    assert v < 1000000
