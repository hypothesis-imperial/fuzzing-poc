from hypothesis import given
from hypothesis.strategies import floats
from sender_receiver import Sender, Receiver
DELAY = 1e-10


@given(floats(min_value=0, max_value=10))
def test_confirmaiton_time(wait):
    x = Sender()
    y = Receiver(wait + DELAY, 0)
    x.send(y, "message")
    assert x.check() < 10
