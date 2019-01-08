from hypothesis import given
from hypothesis.strategies import floats
from sender_receiver import Sender, Receiver


@given(floats(min_value=0, max_value=10.00000000000001))
def test_wait(wait):
    x = Sender()
    y = Receiver(wait, 0)
    x.send(y, "message")
    assert x.check() < 10
